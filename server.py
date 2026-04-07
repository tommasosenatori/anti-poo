import json
import os
import random
import shutil
import subprocess
import threading
import time
import uuid
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from questions import QUESTION_BANK

ROOT = Path(__file__).parent
INDEX_FILE = ROOT / "index.html"

SESSIONS = {}
LOCK = threading.Lock()
QUIZ_SIZE = 10
COMPILE_TIMEOUT = 10
RUN_TIMEOUT = 10
RUNS_DIR = ROOT / ".runs"
RUNS_DIR.mkdir(exist_ok=True)


def find_executable(name, candidates):
    p = shutil.which(name)
    if p:
        return p
    for c in candidates:
        if Path(c).exists():
            return c
    java_home = os.environ.get("JAVA_HOME")
    if java_home:
        path = Path(java_home) / "bin" / f"{name}.exe"
        if path.exists():
            return str(path)
    return None


JAVAC = find_executable(
    "javac",
    [
        r"C:\Program Files\Java\jdk-21\bin\javac.exe",
        r"C:\Program Files\Java\jdk-17\bin\javac.exe",
        r"C:\Program Files\Java\jdk-11\bin\javac.exe",
        r"C:\Program Files\Eclipse Adoptium\jdk-17.0.18.8-hotspot\bin\javac.exe",
        r"C:\Program Files\Eclipse Adoptium\jdk-21.0.2.13-hotspot\bin\javac.exe",
        r"C:\Program Files\Eclipse Adoptium\jdk-17.0.10.7-hotspot\bin\javac.exe",
    ],
)
JAVA = find_executable(
    "java",
    [
        r"C:\Program Files\Java\jdk-21\bin\java.exe",
        r"C:\Program Files\Java\jdk-17\bin\java.exe",
        r"C:\Program Files\Java\jdk-11\bin\java.exe",
        r"C:\Program Files\Eclipse Adoptium\jdk-17.0.18.8-hotspot\bin\java.exe",
        r"C:\Program Files (x86)\Common Files\Oracle\Java\java8path_target_214873953\java.exe",
    ],
)
if JAVAC:
    sibling_java = str(Path(JAVAC).with_name("java.exe"))
    if Path(sibling_java).exists():
        JAVA = sibling_java


def sanitize(text):
    if not text:
        return ""
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


def run_submission(question, code):
    if not JAVA:
        return {"status": "environment_error", "message": "Java runtime non trovato."}
    if not JAVAC:
        return {"status": "environment_error", "message": "Compilatore javac non trovato. Installa un JDK."}

    tmp_path = RUNS_DIR / f"exam_sim_{uuid.uuid4().hex}"
    tmp_path.mkdir(parents=True, exist_ok=False)
    try:
        src_name = question["source_filename"]
        (tmp_path / src_name).write_text(code, encoding="utf-8")
        (tmp_path / "TestRunner.java").write_text(question["test_runner"], encoding="utf-8")

        try:
            cp = subprocess.run(
                [JAVAC, src_name, "TestRunner.java"],
                cwd=str(tmp_path),
                capture_output=True,
                text=True,
                timeout=COMPILE_TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            return {"status": "compile_error", "message": "Timeout in compilazione."}
        except Exception as ex:
            return {"status": "compile_error", "message": f"Errore compilazione: {ex}"}

        if cp.returncode != 0:
            msg = sanitize((cp.stderr or "") + "\n" + (cp.stdout or ""))
            return {"status": "compile_error", "message": msg or "Errore compilazione."}

        try:
            rp = subprocess.run(
                [JAVA, "-cp", str(tmp_path), "TestRunner"],
                cwd=str(tmp_path),
                capture_output=True,
                text=True,
                timeout=RUN_TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            return {"status": "runtime_error", "message": "Timeout in esecuzione test."}
        except Exception as ex:
            return {"status": "runtime_error", "message": f"Errore esecuzione: {ex}"}

        out = sanitize((rp.stdout or "") + "\n" + (rp.stderr or ""))
        lines = [x.strip() for x in out.splitlines() if x.strip()]
        fails = []
        runtime = []
        passed = False
        for line in lines:
            if line == "ALL_TESTS_PASSED":
                passed = True
            elif line.startswith("FAIL|"):
                p = line.split("|", 3)
                if len(p) == 4:
                    fails.append({"test": p[1], "details": f"{p[2]} | {p[3]}"})
                else:
                    fails.append({"test": "unknown", "details": line})
            elif line.startswith("RUNTIME|"):
                p = line.split("|", 2)
                if len(p) == 3:
                    runtime.append({"test": p[1], "details": p[2]})
                else:
                    runtime.append({"test": "unknown", "details": line})

        if passed and not fails and not runtime:
            return {"status": "success", "message": "Compilazione OK. Tutti i test nascosti sono passati."}
        if runtime and not fails:
            return {"status": "runtime_error", "message": "Errore runtime durante i test.", "runtime_failures": runtime}
        if not fails and not runtime:
            return {
                "status": "runtime_error",
                "message": "I test non hanno prodotto un esito valido.",
                "runtime_failures": [{"test": "runner", "details": out or "Nessun output dal test runner."}],
            }
        return {
            "status": "logic_error",
            "message": "Compilazione OK, ma alcuni test nascosti non passano.",
            "failed_tests": fails,
            "runtime_failures": runtime,
        }
    finally:
        shutil.rmtree(tmp_path, ignore_errors=True)


class Handler(BaseHTTPRequestHandler):
    def _json(self, payload, code=HTTPStatus.OK):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _html(self, html, code=HTTPStatus.OK):
        data = html.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query or "")
        if path in ("/", "/index.html"):
            self._html(INDEX_FILE.read_text(encoding="utf-8"))
            return
        if path == "/api/catalog":
            rows = []
            for q in QUESTION_BANK:
                rows.append(
                    {
                        "id": q["id"],
                        "title": q["title"],
                        "esonero": q.get("esonero", 2),
                        "topic": q.get("topic", "altro"),
                    }
                )
            counts = {
                "by_esonero": {"1": 0, "2": 0, "3": 0},
                "by_topic": {"array_liste": 0, "altro": 0, "mappe": 0},
                "total": len(rows),
            }
            for row in rows:
                counts["by_esonero"][str(row["esonero"])] += 1
                counts["by_topic"][row["topic"]] += 1
            self._json({"counts": counts, "questions": rows})
            return
        if path == "/api/start":
            requested = query.get("esonero", [None])[0]
            selected_esonero = None
            pool = QUESTION_BANK
            if requested in ("1", "2", "3"):
                selected_esonero = int(requested)
                pool = [q for q in QUESTION_BANK if q.get("esonero", 2) == selected_esonero]
            if not pool:
                self._json({"error": "Nessuna domanda disponibile per il filtro scelto."}, code=HTTPStatus.BAD_REQUEST)
                return
            selected = random.sample(pool, k=min(QUIZ_SIZE, len(pool)))
            sid = str(uuid.uuid4())
            with LOCK:
                SESSIONS[sid] = {
                    "question_ids": [q["id"] for q in selected],
                    "started_at": time.time(),
                    "esonero": selected_esonero,
                }
            public_questions = []
            for q in selected:
                public_questions.append(
                    {
                        "id": q["id"],
                        "title": q["title"],
                        "prompt": q["prompt"],
                        "starter_code": q["starter_code"],
                        "esonero": q.get("esonero", 2),
                        "topic": q.get("topic", "altro"),
                    }
                )
            self._json(
                {
                    "session_id": sid,
                    "questions": public_questions,
                    "quiz_size": len(public_questions),
                    "selected_esonero": selected_esonero,
                    "java_available": bool(JAVA),
                    "javac_available": bool(JAVAC),
                }
            )
            return
        self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def do_POST(self):
        endpoint = urlparse(self.path).path
        if endpoint not in ("/api/submit", "/api/solution"):
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")
            return
        clen = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(clen)
        try:
            payload = json.loads(body.decode("utf-8"))
        except Exception:
            self._json({"error": "JSON non valido"}, code=HTTPStatus.BAD_REQUEST)
            return

        sid = payload.get("session_id")
        qid = payload.get("question_id")
        if not sid or not qid:
            self._json({"error": "Payload incompleto"}, code=HTTPStatus.BAD_REQUEST)
            return

        with LOCK:
            session = SESSIONS.get(sid)
        if not session:
            self._json({"error": "Sessione non valida"}, code=HTTPStatus.BAD_REQUEST)
            return
        if qid not in session["question_ids"]:
            self._json({"error": "Domanda non valida in questa sessione"}, code=HTTPStatus.BAD_REQUEST)
            return

        question = next((q for q in QUESTION_BANK if q["id"] == qid), None)
        if not question:
            self._json({"error": "Domanda non trovata"}, code=HTTPStatus.BAD_REQUEST)
            return

        if endpoint == "/api/solution":
            solution = question.get("solution_code")
            if not solution:
                self._json({"status": "not_available", "message": "Soluzione non disponibile per questa domanda."})
                return
            self._json(
                {
                    "status": "ok",
                    "question_id": qid,
                    "title": question.get("title"),
                    "solution_code": solution,
                }
            )
            return

        code = payload.get("code", "")
        if not isinstance(code, str):
            self._json({"error": "Payload incompleto"}, code=HTTPStatus.BAD_REQUEST)
            return
        self._json(run_submission(question, code))

    def log_message(self, fmt, *args):
        return


def run_server(host="127.0.0.1", port=8000):
    srv = ThreadingHTTPServer((host, port), Handler)
    print(f"Exam simulator attivo su http://{host}:{port}")
    print(f"Java: {'OK' if JAVA else 'MANCANTE'} | javac: {'OK' if JAVAC else 'MANCANTE'}")
    srv.serve_forever()


if __name__ == "__main__":
    run_server()
