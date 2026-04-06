# Simulatore Esame Java (Localhost)

## Avvio

1. Apri un terminale in questa cartella.
2. Esegui:

```powershell
python server.py
```

3. Apri il browser su:

```text
http://127.0.0.1:8000
```

## Cosa fa

- Genera un quiz con 10 domande random da una banca locale di 36 tracce (derivate dal PDF che hai fornito).
- Puoi selezionare l'esonero (`1`, `2`, `3`) e ottenere 10 domande random solo di quella prova.
- Ogni domanda ha test nascosti.
- Il codice Java viene compilato e testato localmente con test nascosti.
- Editor stile IDE (Monaco): evidenziazione sintassi Java, auto-closing parentesi/virgolette, indentazione con TAB, suggerimenti base.
- Mostra:
  - box rosso per errori di compilazione/logica/runtime
  - box verde se tutti i test passano
- Timer in alto a sinistra.
- Navigazione avanti/indietro tra domande.

## Requisito importante

Serve un **JDK** installato (deve esistere `javac`).
Se hai solo il JRE, i test non potranno essere eseguiti.

## Catalogo esercizi

- [ESERCIZI_CATALOGO.md](c:\Users\tomma\OneDrive - Universita degli Studi Roma Tre\Desktop\ANTI-POO\exam-sim\ESERCIZI_CATALOGO.md)
- [ESERCIZI_CATALOGO.txt](c:\Users\tomma\OneDrive - Universita degli Studi Roma Tre\Desktop\ANTI-POO\exam-sim\ESERCIZI_CATALOGO.txt)

In `questions.py` ogni domanda ora ha:
- `esonero`: `1`, `2`, `3`
- `topic`: `array_liste`, `mappe`, `altro`
