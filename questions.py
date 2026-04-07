QUESTION_BANK = [{'id': 'calcola_media',
  'title': 'CalcolatoreMedia.calcolaMedia()',
  'prompt': "Implementa calcolaMedia(int[] sequenza) che restituisce la media dei valori dell'array.",
  'source_filename': 'CalcolatoreMedia.java',
  'starter_code': 'public class CalcolatoreMedia {\n'
                  '    public double calcolaMedia(int[] sequenza){\n'
                  '        // TODO\n'
                  '        return 0.0;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '    private static void assertEq(String n,double e,double a){ if(Math.abs(e-a)>1e-9){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        CalcolatoreMedia c = new CalcolatoreMedia();\n'
                 '        assertEq("avg1",2.5,c.calcolaMedia(new int[]{2,3}));\n'
                 '        assertEq("avg2",-2.0,c.calcolaMedia(new int[]{-1,-2,-3}));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste',
  'solution_code': 'public class CalcolatoreMedia {\n'
                   '    public double calcolaMedia(int[] sequenza){\n'
                   '        int somma = 0;\n'
                   '        for (int n : sequenza) somma += n;\n'
                   '        return (double) somma / sequenza.length;\n'
                   '    }\n'
                   '}\n'},
 {'id': 'collezione_compatta',
  'title': 'Collezione.aggiungi/elimina (array compatto)',
  'prompt': 'Completa `aggiungi(String)` e `elimina(String)` della classe Collezione con array compatto e contatore '
            '`numeroElementi`.',
  'source_filename': 'Collezione.java',
  'esonero': 1,
  'topic': 'array_liste',
  'starter_code': 'public class Collezione {\n'
                  '    private String[] elementi;\n'
                  '    private int numeroElementi;\n'
                  '\n'
                  '    public Collezione(int dimensioneMax) {\n'
                  '        this.elementi = new String[dimensioneMax];\n'
                  '        this.numeroElementi = 0;\n'
                  '    }\n'
                  '\n'
                  '    public Collezione(String... elementi) {\n'
                  '        this.elementi = elementi;\n'
                  '        this.numeroElementi = elementi.length;\n'
                  '    }\n'
                  '\n'
                  '    public int getNumeroElementi() {\n'
                  '        return this.numeroElementi;\n'
                  '    }\n'
                  '\n'
                  '    public boolean aggiungi(String elemento) {\n'
                  '        // TODO\n'
                  '        return false;\n'
                  '    }\n'
                  '\n'
                  '    public boolean elimina(String wanted) {\n'
                  '        // TODO\n'
                  '        return false;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 '\n'
                 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '\n'
                 '    private static void assertEq(String n, Object e, Object a) {\n'
                 '        if (!Objects.equals(e, a)) {\n'
                 '            failed++;\n'
                 '            System.out.println("FAIL|" + n + "|expected=" + e + "|actual=" + a);\n'
                 '        }\n'
                 '    }\n'
                 '\n'
                 '    public static void main(String[] args) {\n'
                 '        Collezione c = new Collezione(3);\n'
                 '        assertEq("add1", true, c.aggiungi("a"));\n'
                 '        assertEq("add2", true, c.aggiungi("b"));\n'
                 '        assertEq("size_after_add", 2, c.getNumeroElementi());\n'
                 '        assertEq("del_exists", true, c.elimina("a"));\n'
                 '        assertEq("size_after_del", 1, c.getNumeroElementi());\n'
                 '        assertEq("del_missing", false, c.elimina("z"));\n'
                 '        assertEq("add3", true, c.aggiungi("c"));\n'
                 '        assertEq("add4", true, c.aggiungi("d"));\n'
                 '        assertEq("full_add", false, c.aggiungi("e"));\n'
                 '\n'
                 '        Collezione c2 = new Collezione("x", "y", "z");\n'
                 '        assertEq("delete_mid", true, c2.elimina("y"));\n'
                 '        assertEq("delete_mid_size", 2, c2.getNumeroElementi());\n'
                 '        assertEq("re_add_after_delete", true, c2.aggiungi("w"));\n'
                 '        assertEq("re_add_size", 3, c2.getNumeroElementi());\n'
                 '\n'
                 '        if (failed == 0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'solution_code': 'public class Collezione {\n'
                   '    private String[] elementi;\n'
                   '    private int numeroElementi;\n'
                   '\n'
                   '    public Collezione(int dimensioneMax) {\n'
                   '        this.elementi = new String[dimensioneMax];\n'
                   '        this.numeroElementi = 0;\n'
                   '    }\n'
                   '\n'
                   '    public Collezione(String... elementi) {\n'
                   '        this.elementi = elementi;\n'
                   '        this.numeroElementi = elementi.length;\n'
                   '    }\n'
                   '\n'
                   '    public int getNumeroElementi() {\n'
                   '        return this.numeroElementi;\n'
                   '    }\n'
                   '\n'
                   '    public boolean aggiungi(String elemento) {\n'
                   '        if (numeroElementi < elementi.length) {\n'
                   '            elementi[numeroElementi] = elemento;\n'
                   '            numeroElementi++;\n'
                   '            return true;\n'
                   '        }\n'
                   '        return false;\n'
                   '    }\n'
                   '\n'
                   '    public boolean elimina(String wanted) {\n'
                   '        for (int i = 0; i < numeroElementi; i++) {\n'
                   '            if (elementi[i].equals(wanted)) {\n'
                   '                for (int j = i; j < numeroElementi - 1; j++) {\n'
                   '                    elementi[j] = elementi[j + 1];\n'
                   '                }\n'
                   '                elementi[numeroElementi - 1] = null;\n'
                   '                numeroElementi--;\n'
                   '                return true;\n'
                   '            }\n'
                   '        }\n'
                   '        return false;\n'
                   '    }\n'
                   '}\n'},
 {'id': 'conta_occorrenze_posizione',
  'title': 'ContatoreOccorrenzePosizione.contaOccorrenze()',
  'prompt': 'Implementa contaOccorrenze(sequenza,daControllare) come nel testo: output allineato agli indici di '
            'daControllare.',
  'source_filename': 'ContatoreOccorrenzePosizione.java',
  'starter_code': 'public class ContatoreOccorrenzePosizione {\n'
                  '    public int[] contaOccorrenze(String[] sequenza, String[] daControllare){\n'
                  '        // TODO\n'
                  '        return new int[daControllare.length];\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertArr(String n,int[] e,int[] a){ if(!Arrays.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+Arrays.toString(e)+"|actual="+Arrays.toString(a)); } }\n'
                 '    public static void main(String[] args){\n'
                 '        ContatoreOccorrenzePosizione c = new ContatoreOccorrenzePosizione();\n'
                 '        assertArr("example", new int[]{2,0,1}, c.contaOccorrenze(new String[]{"a","c","a","e"}, new '
                 'String[]{"a","b","c"}));\n'
                 '        assertArr("empty", new int[]{}, c.contaOccorrenze(new String[]{"x"}, new String[]{}));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste',
  'solution_code': 'public class ContatoreOccorrenzePosizione {\n'
                   '    public int[] contaOccorrenze(String[] sequenza, String[] daControllare){\n'
                   '        int[] out = new int[daControllare.length];\n'
                   '        for (int i = 0; i < daControllare.length; i++) {\n'
                   '            for (String s : sequenza) {\n'
                   '                if (daControllare[i].equals(s)) out[i]++;\n'
                   '            }\n'
                   '        }\n'
                   '        return out;\n'
                   '    }\n'
                   '}\n'},
 {'id': 'decrescente_lista',
  'title': 'Decrescente.isDecrescente(List<Integer>)',
  'prompt': 'Ritorna true se la lista e strettamente decrescente; se vuota lancia NoSuchElementException.',
  'source_filename': 'Decrescente.java',
  'starter_code': 'import java.util.*;\n'
                  'public class Decrescente {\n'
                  '    public static boolean isDecrescente(List<Integer> lista) throws NoSuchElementException {\n'
                  '        // TODO\n'
                  '        return false;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void fail(String m){ failed++; System.out.println("FAIL|test|"+m); }\n'
                 '    public static void main(String[] args){\n'
                 '        try { Decrescente.isDecrescente(new ArrayList<>()); fail("no_exception"); } '
                 'catch(NoSuchElementException ex){}\n'
                 '        try { if(!Decrescente.isDecrescente(Arrays.asList(3,2,1))) fail("dec"); '
                 'if(Decrescente.isDecrescente(Arrays.asList(3,3,1))) fail("strict"); } catch(Exception e){ '
                 'fail("unexpected"); }\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste'},
 {'id': 'lista_simmetrica',
  'title': 'ListaInteri.isSimmetrica()',
  'prompt': 'Implementa isSimmetrica(List<Integer>): true se lista simmetrica; se null lancia NoSuchElementException.',
  'source_filename': 'ListaInteri.java',
  'starter_code': 'import java.util.*;\n'
                  'public class ListaInteri {\n'
                  '    public static boolean isSimmetrica(List<Integer> lista) throws NoSuchElementException{\n'
                  '        // TODO\n'
                  '        return false;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void fail(String m){ failed++; System.out.println("FAIL|test|"+m); }\n'
                 '    public static void main(String[] args){\n'
                 '        try{ ListaInteri.isSimmetrica(null); fail("no_exception"); }catch(NoSuchElementException '
                 'ex){}\n'
                 '        try{ if(!ListaInteri.isSimmetrica(Arrays.asList(1,2,1))) fail("sym"); '
                 'if(ListaInteri.isSimmetrica(Arrays.asList(1,2,3))) fail("not_sym"); }catch(Exception e){ '
                 'fail("unexpected"); }\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste'},
 {'id': 'lista_limitata_add',
  'title': 'ListaLimitata.add()',
  'prompt': 'Implementa add(a) con regole: duplica->sposta in coda; se piena rimuovi minimo e aggiungi nuovo.',
  'source_filename': 'ListaLimitata.java',
  'starter_code': 'import java.util.*;\n'
                  'public class ListaLimitata {\n'
                  '    private List<Integer> lista = new LinkedList<>();\n'
                  '    private static final int DIM_MASSIMA = 2;\n'
                  '    public void add(int a){\n'
                  '        // TODO\n'
                  '    }\n'
                  '    public List<Integer> getLista(){ return this.lista; }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        ListaLimitata l = new ListaLimitata(); l.add(5); l.add(2); l.add(7);\n'
                 '        assertEq("full_remove_min", Arrays.asList(5,7), l.getLista());\n'
                 '        l.add(5); assertEq("duplicate_move_end", Arrays.asList(7,5), l.getLista());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste'},
 {'id': 'strettamente_decrescente',
  'title': 'Monotonia.isStrettamenteDecrescente()',
  'prompt': 'Implementa isStrettamenteDecrescente(lista). Liste di dimensione 0 o 1 sono true.',
  'source_filename': 'Monotonia.java',
  'starter_code': 'import java.util.*;\n'
                  'public class Monotonia {\n'
                  '    public static boolean isStrettamenteDecrescente(List<Integer> lista){\n'
                  '        // TODO\n'
                  '        return false;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,boolean e,boolean a){ if(e!=a){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        assertEq("empty",true,Monotonia.isStrettamenteDecrescente(Arrays.asList()));\n'
                 '        assertEq("dec",true,Monotonia.isStrettamenteDecrescente(Arrays.asList(3,2,1)));\n'
                 '        assertEq("not",false,Monotonia.isStrettamenteDecrescente(Arrays.asList(3,3,1)));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste'},
 {'id': 'conta_omonimi',
  'title': 'Persone.contaOmonimiDi()',
  'prompt': "Implementa contaOmonimiDi(nome): conta quante volte nome appare nell'array nomi (ignorando null).",
  'source_filename': 'Persone.java',
  'starter_code': 'public class Persone {\n'
                  '    private String[] nomi;\n'
                  '    public Persone(int n){ this.nomi = new String[n]; }\n'
                  '    public int contaOmonimiDi(String nome){\n'
                  '        // TODO\n'
                  '        return 0;\n'
                  '    }\n'
                  '    public void aggiungiNome(int indice,String nome){ this.nomi[indice] = nome; }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,int e,int a){ if(e!=a){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Persone p = new Persone(5); p.aggiungiNome(0,"Anna"); p.aggiungiNome(1,"Luca"); '
                 'p.aggiungiNome(3,"Anna");\n'
                 '        assertEq("anna",2,p.contaOmonimiDi("Anna")); assertEq("none",0,p.contaOmonimiDi("Mario"));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste',
  'solution_code': 'public class Persone {\n'
                   '    private String[] nomi;\n'
                   '    public Persone(int n){ this.nomi = new String[n]; }\n'
                   '    public int contaOmonimiDi(String nome){\n'
                   '        int omonimi = 0;\n'
                   '        for (String s : nomi) {\n'
                   '            if (s != null && s.equals(nome)) omonimi++;\n'
                   '        }\n'
                   '        return omonimi;\n'
                   '    }\n'
                   '    public void aggiungiNome(int indice,String nome){ this.nomi[indice] = nome; }\n'
                   '}\n'},
 {'id': 'verifica_duplicati',
  'title': 'Persone.verificaDuplicati(String)',
  'prompt': "Implementa verificaDuplicati(String nome): true se il nome compare almeno due volte nell'array nomi.",
  'source_filename': 'Persone.java',
  'starter_code': 'public class Persone {\n'
                  '    private String[] nomi;\n'
                  '    public Persone(int numeroPersone) { this.nomi = new String[numeroPersone]; }\n'
                  '    public void aggiungiNome(String nome, int indice) { this.nomi[indice] = nome; }\n'
                  '    public boolean verificaDuplicati(String nome) {\n'
                  '        // TODO\n'
                  '        return false;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '    private static void assertEq(String n, boolean e, boolean a){ if(e!=a){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Persone p = new Persone(5);\n'
                 '        p.aggiungiNome("Luca",0); p.aggiungiNome("Anna",1); p.aggiungiNome("Luca",2);\n'
                 '        assertEq("luca", true, p.verificaDuplicati("Luca"));\n'
                 '        assertEq("anna", false, p.verificaDuplicati("Anna"));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste',
  'solution_code': 'public class Persone {\n'
                   '    private String[] nomi;\n'
                   '    public Persone(int numeroPersone) { this.nomi = new String[numeroPersone]; }\n'
                   '    public void aggiungiNome(String nome, int indice) { this.nomi[indice] = nome; }\n'
                   '    public boolean verificaDuplicati(String nome) {\n'
                   '        int conta = 0;\n'
                   '        for (String s : this.nomi) {\n'
                   '            if (s != null && s.equals(nome)) {\n'
                   '                conta++;\n'
                   '                if (conta > 1) return true;\n'
                   '            }\n'
                   '        }\n'
                   '        return false;\n'
                   '    }\n'
                   '}\n'},
 {'id': 'righello_distanza',
  'title': 'Righello.distanza() punto-punto e punto-cerchio',
  'prompt': 'Completa i due overload `distanza`: tra due punti e tra punto/cerchio con formula `abs(distanzaCentro - '
            'raggio)`.',
  'source_filename': 'Righello.java',
  'esonero': 1,
  'topic': 'array_liste',
  'starter_code': 'import static java.lang.Math.sqrt;\n'
                  'import static java.lang.Math.abs;\n'
                  '\n'
                  'class Punto {\n'
                  '    private int x;\n'
                  '    private int y;\n'
                  '\n'
                  '    public Punto(int x, int y) {\n'
                  '        this.x = x;\n'
                  '        this.y = y;\n'
                  '    }\n'
                  '\n'
                  '    public int getX() { return x; }\n'
                  '    public int getY() { return y; }\n'
                  '}\n'
                  '\n'
                  'class Cerchio {\n'
                  '    private Punto centro;\n'
                  '    private int raggio;\n'
                  '\n'
                  '    public Cerchio(Punto centro, int raggio) {\n'
                  '        this.centro = centro;\n'
                  '        this.raggio = raggio;\n'
                  '    }\n'
                  '\n'
                  '    public Punto getCentro() { return centro; }\n'
                  '    public int getRaggio() { return raggio; }\n'
                  '}\n'
                  '\n'
                  'public class Righello {\n'
                  '    public double distanza(Punto p1, Punto p2) {\n'
                  '        // TODO\n'
                  '        return 0.0;\n'
                  '    }\n'
                  '\n'
                  '    public double distanza(Punto punto, Cerchio c) {\n'
                  '        // TODO\n'
                  '        return 0.0;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '\n'
                 '    private static void assertEq(String n, double e, double a) {\n'
                 '        if (Math.abs(e - a) > 1e-9) {\n'
                 '            failed++;\n'
                 '            System.out.println("FAIL|" + n + "|expected=" + e + "|actual=" + a);\n'
                 '        }\n'
                 '    }\n'
                 '\n'
                 '    public static void main(String[] args) {\n'
                 '        Righello r = new Righello();\n'
                 '\n'
                 '        Punto p1 = new Punto(0, 0);\n'
                 '        Punto p2 = new Punto(3, 4);\n'
                 '        assertEq("point_point", 5.0, r.distanza(p1, p2));\n'
                 '\n'
                 '        Cerchio c = new Cerchio(new Punto(0, 0), 5);\n'
                 '        Punto esterno = new Punto(10, 0);\n'
                 '        Punto interno = new Punto(3, 0);\n'
                 '        assertEq("point_circle_outside", 5.0, r.distanza(esterno, c));\n'
                 '        assertEq("point_circle_inside", 2.0, r.distanza(interno, c));\n'
                 '\n'
                 '        if (failed == 0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'solution_code': 'import static java.lang.Math.sqrt;\n'
                   'import static java.lang.Math.abs;\n'
                   '\n'
                   'class Punto {\n'
                   '    private int x;\n'
                   '    private int y;\n'
                   '\n'
                   '    public Punto(int x, int y) {\n'
                   '        this.x = x;\n'
                   '        this.y = y;\n'
                   '    }\n'
                   '\n'
                   '    public int getX() { return x; }\n'
                   '    public int getY() { return y; }\n'
                   '}\n'
                   '\n'
                   'class Cerchio {\n'
                   '    private Punto centro;\n'
                   '    private int raggio;\n'
                   '\n'
                   '    public Cerchio(Punto centro, int raggio) {\n'
                   '        this.centro = centro;\n'
                   '        this.raggio = raggio;\n'
                   '    }\n'
                   '\n'
                   '    public Punto getCentro() { return centro; }\n'
                   '    public int getRaggio() { return raggio; }\n'
                   '}\n'
                   '\n'
                   'public class Righello {\n'
                   '    public double distanza(Punto p1, Punto p2) {\n'
                   '        double dx = p1.getX() - p2.getX();\n'
                   '        double dy = p1.getY() - p2.getY();\n'
                   '        return sqrt(dx * dx + dy * dy);\n'
                   '    }\n'
                   '\n'
                   '    public double distanza(Punto punto, Cerchio c) {\n'
                   '        double distCentro = distanza(punto, c.getCentro());\n'
                   '        return abs(distCentro - c.getRaggio());\n'
                   '    }\n'
                   '}\n'},
 {'id': 'somma_dispari',
  'title': 'SequenzaDiInteri.sommaDispari()',
  'prompt': 'Implementa il metodo sommaDispari() che restituisce la somma degli elementi in posizione dispari '
            "dell'array sequenza.",
  'source_filename': 'SequenzaDiInteri.java',
  'starter_code': 'public class SequenzaDiInteri {\n'
                  '    private int[] sequenza;\n'
                  '\n'
                  '    public SequenzaDiInteri(int numeroInteri) {\n'
                  '        this.sequenza = new int[numeroInteri];\n'
                  '    }\n'
                  '\n'
                  '    public void setElemento(int indice, int valore) {\n'
                  '        this.sequenza[indice] = valore;\n'
                  '    }\n'
                  '\n'
                  '    public int sommaDispari() {\n'
                  '        // TODO\n'
                  '        return 0;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '    private static void assertEq(String n, int e, int a){ if(e!=a){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        SequenzaDiInteri s = new SequenzaDiInteri(5);\n'
                 '        s.setElemento(0,2); s.setElemento(1,5); s.setElemento(2,10); s.setElemento(3,-1); '
                 's.setElemento(4,9);\n'
                 '        assertEq("mix",4,s.sommaDispari());\n'
                 '        SequenzaDiInteri s2 = new SequenzaDiInteri(1); s2.setElemento(0,99);\n'
                 '        assertEq("single",0,s2.sommaDispari());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste',
  'solution_code': 'public class SequenzaDiInteri {\n'
                   '    private int[] sequenza;\n'
                   '\n'
                   '    public SequenzaDiInteri(int numeroInteri) {\n'
                   '        this.sequenza = new int[numeroInteri];\n'
                   '    }\n'
                   '\n'
                   '    public void setElemento(int indice, int valore) {\n'
                   '        this.sequenza[indice] = valore;\n'
                   '    }\n'
                   '\n'
                   '    public int sommaDispari() {\n'
                   '        int somma = 0;\n'
                   '        for (int i = 0; i < sequenza.length; i++) {\n'
                   '            if (i % 2 == 1) somma += sequenza[i];\n'
                   '        }\n'
                   '        return somma;\n'
                   '    }\n'
                   '}\n'},
 {'id': 'aggiungi_in_coda',
  'title': 'SequenzaDiStringhe.aggiungiInCoda()',
  'prompt': "Implementa aggiungiInCoda(String): aggiunge in coda solo se l'array non e pieno.",
  'source_filename': 'SequenzaDiStringhe.java',
  'starter_code': 'public class SequenzaDiStringhe {\n'
                  '    public String[] sequenza;\n'
                  '    public SequenzaDiStringhe(int dimensione){ this.sequenza = new String[dimensione]; }\n'
                  '    public void aggiungiStringa(String s, int posizione){ this.sequenza[posizione] = s; }\n'
                  '    public void aggiungiInCoda(String nuovaStringa){\n'
                  '        // TODO\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,String e,String a){ '
                 'if((e==null&&a!=null)||(e!=null&&!e.equals(a))){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        SequenzaDiStringhe s = new SequenzaDiStringhe(3);\n'
                 '        s.aggiungiStringa("a",0); s.aggiungiStringa("b",1); s.aggiungiInCoda("c");\n'
                 '        assertEq("append","c",s.sequenza[2]);\n'
                 '        SequenzaDiStringhe s2 = new SequenzaDiStringhe(2);\n'
                 '        s2.aggiungiStringa("x",0); s2.aggiungiStringa("y",1); s2.aggiungiInCoda("z");\n'
                 '        assertEq("full","y",s2.sequenza[1]);\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste',
  'solution_code': 'public class SequenzaDiStringhe {\n'
                   '    public String[] sequenza;\n'
                   '    public SequenzaDiStringhe(int dimensione){ this.sequenza = new String[dimensione]; }\n'
                   '    public void aggiungiStringa(String s, int posizione){ this.sequenza[posizione] = s; }\n'
                   '    public void aggiungiInCoda(String nuovaStringa){\n'
                   '        for (int i = 0; i < sequenza.length; i++) {\n'
                   '            if (sequenza[i] == null) {\n'
                   '                sequenza[i] = nuovaStringa;\n'
                   '                return;\n'
                   '            }\n'
                   '        }\n'
                   '    }\n'
                   '}\n'},
 {'id': 'ha_doppioni',
  'title': 'SequenzaDiStringhe.haDoppioni()',
  'prompt': "Implementa haDoppioni() che restituisce true se nell'array sequenza ci sono almeno due stringhe uguali.",
  'source_filename': 'SequenzaDiStringhe.java',
  'starter_code': 'public class SequenzaDiStringhe {\n'
                  '    private String[] sequenza;\n'
                  '    public SequenzaDiStringhe(int dimensione) { this.sequenza = new String[dimensione]; }\n'
                  '    public void aggiungiStringa(String stringa, int posizione) { this.sequenza[posizione] = '
                  'stringa; }\n'
                  '    public boolean haDoppioni() {\n'
                  '        // TODO\n'
                  '        return false;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '    private static void assertEq(String n, boolean e, boolean a){ if(e!=a){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        SequenzaDiStringhe a = new SequenzaDiStringhe(4);\n'
                 '        a.aggiungiStringa("ciao",0); a.aggiungiStringa("java",1); a.aggiungiStringa("ciao",2);\n'
                 '        assertEq("dup", true, a.haDoppioni());\n'
                 '        SequenzaDiStringhe b = new SequenzaDiStringhe(3);\n'
                 '        b.aggiungiStringa("x",0); b.aggiungiStringa("y",1); b.aggiungiStringa("z",2);\n'
                 '        assertEq("no_dup", false, b.haDoppioni());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 1,
  'topic': 'array_liste',
  'solution_code': 'public class SequenzaDiStringhe {\n'
                   '    private String[] sequenza;\n'
                   '    public SequenzaDiStringhe(int dimensione) { this.sequenza = new String[dimensione]; }\n'
                   '    public void aggiungiStringa(String stringa, int posizione) { this.sequenza[posizione] = '
                   'stringa; }\n'
                   '    public boolean haDoppioni() {\n'
                   '        for (int i = 0; i < sequenza.length - 1; i++) {\n'
                   '            for (int j = i + 1; j < sequenza.length; j++) {\n'
                   '                if (sequenza[i] != null && sequenza[i].equals(sequenza[j])) return true;\n'
                   '            }\n'
                   '        }\n'
                   '        return false;\n'
                   '    }\n'
                   '}\n'},
 {'id': 'autovettura_costruttori',
  'title': 'Autovettura costruttori',
  'prompt': 'Completa la classe Autovettura: costruttore con parametro assegna modello, costruttore vuoto lascia '
            'modello null.',
  'source_filename': 'Autovettura.java',
  'starter_code': 'public class Autovettura {\n'
                  '    private String modello;\n'
                  '    public Autovettura(String modello){\n'
                  '        // TODO\n'
                  '    }\n'
                  '    public Autovettura(){\n'
                  '        // TODO\n'
                  '    }\n'
                  '    public String getModello(){ return modello; }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Autovettura a = new Autovettura("Panda");\n'
                 '        Autovettura b = new Autovettura();\n'
                 '        assertEq("model","Panda",a.getModello());\n'
                 '        assertEq("null",null,b.getModello());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'biblioteca_ordinata',
  'title': 'Biblioteca.elencoOrdinatoPerAnnoTitolo()',
  'prompt': 'Senza cambiare Libro, implementa comparator per anno poi titolo e metodo elencoOrdinatoPerAnnoTitolo().',
  'source_filename': 'Biblioteca.java',
  'starter_code': 'import java.util.*;\n'
                  'class Libro implements Comparable<Libro>{\n'
                  '    private String titolo; private int anno;\n'
                  '    public Libro(String titolo,int anno){ this.titolo=titolo; this.anno=anno; }\n'
                  '    public String getTitolo(){ return titolo; } public int getAnno(){ return anno; }\n'
                  '    public int compareTo(Libro l){ return this.getAnno()-l.getAnno(); }\n'
                  '    public String toString(){ return this.getTitolo(); }\n'
                  '}\n'
                  'class ComparatoreLibroPerAnnoTitolo implements Comparator<Libro>{\n'
                  '    public int compare(Libro l1, Libro l2){\n'
                  '        // TODO\n'
                  '        return 0;\n'
                  '    }\n'
                  '}\n'
                  'public class Biblioteca {\n'
                  '    private List<Libro> elenco = new ArrayList<>();\n'
                  '    public void aggiungiLibro(Libro libro){ this.elenco.add(libro); }\n'
                  '    public List<Libro> elencoOrdinatoPerAnnoTitolo(){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Biblioteca b = new Biblioteca(); b.aggiungiLibro(new Libro("B",2000)); b.aggiungiLibro(new '
                 'Libro("A",2000)); b.aggiungiLibro(new Libro("C",1999));\n'
                 '        List<Libro> l = b.elencoOrdinatoPerAnnoTitolo();\n'
                 '        assertEq("first","C",l.get(0).getTitolo()); assertEq("second","A",l.get(1).getTitolo());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'area_trapezio',
  'title': 'CalcolatoreAreaTrapezio.calcolaArea()',
  'prompt': 'Implementa calcolaArea(baseMinore,baseMaggiore,altezza). Se baseMinore > baseMaggiore ritorna -1.',
  'source_filename': 'CalcolatoreAreaTrapezio.java',
  'starter_code': 'public class CalcolatoreAreaTrapezio {\n'
                  '    public double calcolaArea(double baseMinore, double baseMaggiore, double altezza){\n'
                  '        // TODO\n'
                  '        return 0.0;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '    private static void assertEq(String n,double e,double a){ if(Math.abs(e-a)>1e-9){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        CalcolatoreAreaTrapezio c = new CalcolatoreAreaTrapezio();\n'
                 '        assertEq("ok",15.0,c.calcolaArea(4,6,3));\n'
                 '        assertEq("invalid",-1.0,c.calcolaArea(8,5,3));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'conto_deposita',
  'title': 'ContoCorrente.deposita()',
  'prompt': 'Implementa deposita(data,versamento): aggiorna dataUltimoVersamento e aumenta totale.',
  'source_filename': 'ContoCorrente.java',
  'starter_code': 'public class ContoCorrente {\n'
                  '    private String dataUltimoVersamento;\n'
                  '    private int totale;\n'
                  '    public ContoCorrente(String dataUltimoVersamento,int totale){ '
                  'this.dataUltimoVersamento=dataUltimoVersamento; this.totale=totale; }\n'
                  '    public void deposita(String data,int versamento){\n'
                  '        // TODO\n'
                  '    }\n'
                  '    public String getDataUltimoVersamento(){ return dataUltimoVersamento; }\n'
                  '    public int getTotale(){ return totale; }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        ContoCorrente cc = new ContoCorrente("2026-01-01",100);\n'
                 '        cc.deposita("2026-04-04",50);\n'
                 '        assertEq("data","2026-04-04",cc.getDataUltimoVersamento());\n'
                 '        assertEq("totale",150,cc.getTotale());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'immatricolazioni_comparator',
  'title': 'Immatricolazioni + Comparator eta/matricola',
  'prompt': 'Implementa compare() in ComparatoreStudentePerEtaMatricola e elencoOrdinatoPerEtaMatricola().',
  'source_filename': 'Immatricolazioni.java',
  'starter_code': 'import java.util.*;\n'
                  'class Studente implements Comparable<Studente>{\n'
                  '    private String matricola; private int eta;\n'
                  '    public Studente(String matricola,int eta){ this.matricola=matricola; this.eta=eta; }\n'
                  '    public String getMatricola(){ return matricola; } public int getEta(){ return eta; }\n'
                  '    public int compareTo(Studente s){ return this.getEta()-s.getEta(); }\n'
                  '}\n'
                  'class ComparatoreStudentePerEtaMatricola implements Comparator<Studente>{\n'
                  '    public int compare(Studente p1,Studente p2){\n'
                  '        // TODO\n'
                  '        return 0;\n'
                  '    }\n'
                  '}\n'
                  'public class Immatricolazioni {\n'
                  '    private List<Studente> elenco = new ArrayList<>();\n'
                  '    public void aggiungiStudente(Studente s){ elenco.add(s); }\n'
                  '    public List<Studente> elencoOrdinatoPerEtaMatricola(){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void fail(String m){ failed++; System.out.println("FAIL|test|"+m); }\n'
                 '    public static void main(String[] args){\n'
                 '        Immatricolazioni i = new Immatricolazioni();\n'
                 '        i.aggiungiStudente(new Studente("M2",20)); i.aggiungiStudente(new Studente("M1",20)); '
                 'i.aggiungiStudente(new Studente("M3",19));\n'
                 '        List<Studente> l = i.elencoOrdinatoPerEtaMatricola();\n'
                 '        if(!l.get(0).getMatricola().equals("M3")) fail("eta");\n'
                 '        if(!l.get(1).getMatricola().equals("M1")) fail("matricola");\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'mese_stagionale',
  'title': 'Mese.corrispondenzaStagionale()',
  'prompt': 'Completa enum Mese.corrispondenzaStagionale(): deve restituire il mese opposto di stagione (+6).',
  'source_filename': 'Mese.java',
  'starter_code': 'enum Mese {\n'
                  '    GENNAIO, FEBBRAIO, MARZO,\n'
                  '    APRILE, MAGGIO, GIUGNO,\n'
                  '    LUGLIO, AGOSTO, SETTEMBRE,\n'
                  '    OTTOBRE, NOVEMBRE, DICEMBRE;\n'
                  '\n'
                  '    public Mese corrispondenzaStagionale(){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '    private static void assertEq(String n, Mese e, Mese a){ if(e!=a){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        assertEq("jan", Mese.LUGLIO, Mese.GENNAIO.corrispondenzaStagionale());\n'
                 '        assertEq("aug", Mese.FEBBRAIO, Mese.AGOSTO.corrispondenzaStagionale());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'motocicletta_equals_hash',
  'title': 'Motocicletta equals/hashCode',
  'prompt': 'Correggi Motocicletta implementando equals(Object) e hashCode coerenti.',
  'source_filename': 'Motocicletta.java',
  'starter_code': 'public class Motocicletta {\n'
                  '    private String modello; private int cilindrata;\n'
                  '    public Motocicletta(String modello,int cilindrata){ this.modello=modello; '
                  'this.cilindrata=cilindrata; }\n'
                  '    public String getModello(){ return modello; } public int getCilindrata(){ return cilindrata; }\n'
                  '    @Override public boolean equals(Object obj){\n'
                  '        // TODO\n'
                  '        return false;\n'
                  '    }\n'
                  '    @Override public int hashCode(){\n'
                  '        // TODO\n'
                  '        return 0;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void fail(String m){ failed++; System.out.println("FAIL|test|"+m); }\n'
                 '    public static void main(String[] args){\n'
                 '        Motocicletta a=new Motocicletta("X",1000), b=new Motocicletta("X",1000), c=new '
                 'Motocicletta("X",900);\n'
                 '        if(!a.equals(b)) fail("eq"); if(a.equals(c)) fail("neq");\n'
                 '        HashSet<Motocicletta> s = new HashSet<>(); s.add(a); s.add(b); if(s.size()!=1) '
                 'fail("hash");\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'persona_comparable_desc',
  'title': 'Persona Comparable inverso',
  'prompt': 'Usando Comparable, ordina per cognome in ordine alfabetico inverso e restituisci un TreeSet.',
  'source_filename': 'Persona.java',
  'starter_code': 'import java.util.*;\n'
                  'public class Persona implements Comparable<Persona> {\n'
                  '    private String cognome;\n'
                  '    public Persona(String cognome){ this.cognome = cognome; }\n'
                  '    public String getCognome(){ return cognome; }\n'
                  '    public int compareTo(Persona p){\n'
                  '        // TODO\n'
                  '        return 0;\n'
                  '    }\n'
                  '    public static TreeSet<Persona> getInsiemeOrdinato(List<Persona> lista){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        TreeSet<Persona> s = Persona.getInsiemeOrdinato(Arrays.asList(new Persona("Rossi"),new '
                 'Persona("Bianchi"),new Persona("Verdi")));\n'
                 '        Iterator<Persona> it = s.iterator();\n'
                 '        assertEq("f1","Verdi",it.next().getCognome());\n'
                 '        assertEq("f2","Rossi",it.next().getCognome());\n'
                 '        assertEq("f3","Bianchi",it.next().getCognome());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'persona_comparator_no_comparable',
  'title': 'Persona.getInsiemeOrdinato() senza Comparable',
  'prompt': 'Senza Comparable, usa Comparator per ordinare cognomi in ordine inverso e restituire TreeSet.',
  'source_filename': 'PersonaComparator.java',
  'starter_code': 'import java.util.*;\n'
                  'class Persona {\n'
                  '    private String cognome;\n'
                  '    public Persona(String cognome){ this.cognome = cognome; }\n'
                  '    public String getCognome(){ return cognome; }\n'
                  '    public static TreeSet<Persona> getInsiemeOrdinato(List<Persona> listaPersona){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n'
                  'public class PersonaComparator { }\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void fail(String m){ failed++; System.out.println("FAIL|test|"+m); }\n'
                 '    public static void main(String[] args){\n'
                 '        TreeSet<Persona> s = Persona.getInsiemeOrdinato(Arrays.asList(new Persona("Rossi"),new '
                 'Persona("Bianchi"),new Persona("Verdi")));\n'
                 '        Iterator<Persona> it = s.iterator();\n'
                 '        if(!it.next().getCognome().equals("Verdi")) fail("first");\n'
                 '        if(!it.next().getCognome().equals("Rossi")) fail("second");\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'soldato_costruttore',
  'title': 'Soldato extends Persona',
  'prompt': 'Implementa il costruttore di Soldato usando super(nome,cognome) e assegnando grado.',
  'source_filename': 'Soldato.java',
  'starter_code': 'class Persona {\n'
                  '    private String nome; private String cognome;\n'
                  '    public Persona(String nome,String cognome){ this.nome=nome; this.cognome=cognome; }\n'
                  '    public String getNome(){ return nome; } public String getCognome(){ return cognome; }\n'
                  '}\n'
                  'public class Soldato extends Persona {\n'
                  '    private String grado;\n'
                  '    public Soldato(String nome,String cognome,String grado){\n'
                  '        // TODO\n'
                  '    }\n'
                  '    public String getGrado(){ return this.grado; }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ '
                 'if((e==null&&a!=null)||(e!=null&&!e.equals(a))){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Soldato s = new Soldato("Mario","Rossi","Caporale");\n'
                 '        assertEq("nome","Mario",s.getNome()); assertEq("grado","Caporale",s.getGrado());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'spedizione_equals_hashcode',
  'title': 'Spedizione.equals/hashCode',
  'prompt': 'Implementa equals e hashCode in base a destinazione e codice.',
  'source_filename': 'Spedizione.java',
  'starter_code': 'public class Spedizione {\n'
                  '    private String destinazione;\n'
                  '    private int codice;\n'
                  '    public Spedizione(String destinazione,int codice){ this.destinazione=destinazione; '
                  'this.codice=codice; }\n'
                  '    public String getDestinazione(){ return destinazione; }\n'
                  '    public int getCodice(){ return codice; }\n'
                  '    @Override public boolean equals(Object obj){\n'
                  '        // TODO\n'
                  '        return false;\n'
                  '    }\n'
                  '    @Override public int hashCode(){\n'
                  '        // TODO\n'
                  '        return 0;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void fail(String m){ failed++; System.out.println("FAIL|test|"+m); }\n'
                 '    public static void main(String[] args){\n'
                 '        Spedizione a = new Spedizione("Roma",10);\n'
                 '        Spedizione b = new Spedizione("Roma",10);\n'
                 '        Spedizione c = new Spedizione("Milano",10);\n'
                 '        if(!a.equals(b)) fail("eq_true");\n'
                 '        if(a.equals(c)) fail("eq_false");\n'
                 '        HashSet<Spedizione> s = new HashSet<>(); s.add(a); s.add(b); if(s.size()!=1) fail("hash");\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'immatricolazioni_compareto',
  'title': 'Studente.compareTo + Immatricolazioni sort naturale',
  'prompt': 'Completa compareTo in Studente (eta poi matricola) e usa Collections.sort in '
            'elencoOrdinatoPerEtaMatricola().',
  'source_filename': 'ImmatricolazioniNaturale.java',
  'starter_code': 'import java.util.*;\n'
                  'class Studente implements Comparable<Studente>{\n'
                  '    private String matricola; private int eta;\n'
                  '    public Studente(String matricola,int eta){ this.matricola=matricola; this.eta=eta; }\n'
                  '    public String getMatricola(){ return matricola; } public int getEta(){ return eta; }\n'
                  '    public int compareTo(Studente that){\n'
                  '        // TODO\n'
                  '        return 0;\n'
                  '    }\n'
                  '}\n'
                  'public class ImmatricolazioniNaturale {\n'
                  '    private List<Studente> elenco = new ArrayList<>();\n'
                  '    public void aggiungiStudente(Studente s){ elenco.add(s); }\n'
                  '    public List<Studente> elencoOrdinatoPerEtaMatricola(){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void fail(String m){ failed++; System.out.println("FAIL|test|"+m); }\n'
                 '    public static void main(String[] args){\n'
                 '        ImmatricolazioniNaturale i = new ImmatricolazioniNaturale();\n'
                 '        i.aggiungiStudente(new Studente("M2",20)); i.aggiungiStudente(new Studente("M1",20)); '
                 'i.aggiungiStudente(new Studente("M3",19));\n'
                 '        List<Studente> l = i.elencoOrdinatoPerEtaMatricola();\n'
                 '        if(!l.get(0).getMatricola().equals("M3")) fail("eta"); '
                 'if(!l.get(1).getMatricola().equals("M1")) fail("mat");\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'studente_equals',
  'title': 'Studente.equals(Object)',
  'prompt': 'Correggi/completa equals(Object) in Studente in base a nome e matricola.',
  'source_filename': 'Studente.java',
  'starter_code': 'public class Studente {\n'
                  '    private String nome; private int matricola;\n'
                  '    public Studente(String nome,int matricola){ this.nome=nome; this.matricola=matricola; }\n'
                  '    @Override public boolean equals(Object obj){\n'
                  '        // TODO\n'
                  '        return false;\n'
                  '    }\n'
                  '    public String getNome(){ return nome; }\n'
                  '    public int getMatricola(){ return matricola; }\n'
                  '}\n',
  'test_runner': 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void fail(String m){ failed++; System.out.println("FAIL|test|"+m); }\n'
                 '    public static void main(String[] args){\n'
                 '        Studente a=new Studente("Tom",1), b=new Studente("Tom",1), c=new Studente("Tom",2);\n'
                 '        if(!a.equals(b)) fail("eq_true"); if(a.equals(c)) fail("eq_false");\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 2,
  'topic': 'altro'},
 {'id': 'conta_occorrenze',
  'title': 'ContatoreOccorrenze.conta(List<T>)',
  'prompt': 'Implementa il metodo statico conta(List<T>) che produce una mappa elemento->numero occorrenze.',
  'source_filename': 'ContatoreOccorrenze.java',
  'starter_code': 'import java.util.*;\n'
                  'public class ContatoreOccorrenze {\n'
                  '    public static <T> Map<T, Integer> conta(List<T> l1) {\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '    private static void assertEq(String n, Object e, Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Map<String,Integer> m = ContatoreOccorrenze.conta(Arrays.asList("a","b","a","a","c"));\n'
                 '        assertEq("a",3,m.get("a")); assertEq("b",1,m.get("b")); assertEq("size",3,m.size());\n'
                 '        Map<Integer,Integer> m2 = ContatoreOccorrenze.conta(Arrays.asList(2,2,3));\n'
                 '        assertEq("2",2,m2.get(2));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe',
  'solution_code': 'import java.util.*;\n'
                   'public class ContatoreOccorrenze {\n'
                   '    public static <T> Map<T, Integer> conta(List<T> l1) {\n'
                   '        Map<T, Integer> mappa = new HashMap<>();\n'
                   '        for (T t : l1) {\n'
                   '            mappa.put(t, mappa.getOrDefault(t, 0) + 1);\n'
                   '        }\n'
                   '        return mappa;\n'
                   '    }\n'
                   '}\n'},
 {'id': 'controlla_doppioni',
  'title': 'ControllaOccorrenze.controllaDoppioni()',
  'prompt': 'Data una lista, restituisci mappa elemento->true/false se compare almeno due volte.',
  'source_filename': 'ControllaOccorrenze.java',
  'starter_code': 'import java.util.*;\n'
                  'public class ControllaOccorrenze {\n'
                  '    public static <T> Map<T,Boolean> controllaDoppioni(List<T> l1){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Map<String,Boolean> m = '
                 'ControllaOccorrenze.controllaDoppioni(Arrays.asList("a","b","a","c"));\n'
                 '        assertEq("a",true,m.get("a")); assertEq("b",false,m.get("b"));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe'},
 {'id': 'submap',
  'title': 'CreatoreMappe.subMap()',
  'prompt': 'Implementa subMap(m,c): restituisce nuova mappa con sole chiavi presenti nella collezione c.',
  'source_filename': 'CreatoreSubMappe.java',
  'starter_code': 'import java.util.*;\n'
                  'public class CreatoreSubMappe {\n'
                  '    public static <T,V> Map<T,V> subMap(Map<T,V> m, Collection<T> c){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Map<Integer,String> m = new HashMap<>(); m.put(1,"a"); m.put(2,"b"); m.put(3,"c");\n'
                 '        Map<Integer,String> s = CreatoreSubMappe.subMap(m, Arrays.asList(1,3));\n'
                 '        assertEq("size",2,s.size()); assertEq("v3","c",s.get(3));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe'},
 {'id': 'creatore_mappe_unisci',
  'title': 'CreatoreMappe.unisci() con eccezione',
  'prompt': 'Implementa unisci(l1,l2): associa elementi per indice; se dimensioni diverse lancia '
            'DimensioneDiversaException.',
  'source_filename': 'CreatoreMappe.java',
  'starter_code': 'import java.util.*;\n'
                  'class DimensioneDiversaException extends Exception {}\n'
                  'public class CreatoreMappe {\n'
                  '    public static Map<Integer,String> unisci(List<Integer> l1,List<String> l2) throws '
                  'DimensioneDiversaException {\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void fail(String m){ failed++; System.out.println("FAIL|test|"+m); }\n'
                 '    public static void main(String[] args){\n'
                 '        try{ Map<Integer,String> m = CreatoreMappe.unisci(Arrays.asList(1,2), '
                 'Arrays.asList("a","b")); if(!"b".equals(m.get(2))) fail("map"); }catch(Exception e){ '
                 'fail("unexpected"); }\n'
                 '        try{ CreatoreMappe.unisci(Arrays.asList(1), Arrays.asList("a","b")); fail("no_exception"); '
                 '}catch(DimensioneDiversaException e){} catch(Exception e){ fail("wrong_exception"); }\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe'},
 {'id': 'prodotti_default_m1',
  'title': 'OperazioniProdotti.getProdotto2quantita() con default -1',
  'prompt': 'Implementa getProdotto2quantita(cod2prod,cod2qta): se manca quantita per un prodotto, inserisci -1.',
  'source_filename': 'OperazioniProdotti.java',
  'starter_code': 'import java.util.*;\n'
                  'class Prodotto {\n'
                  '    private String codice; private int peso;\n'
                  '    public Prodotto(String codice, int peso){ this.codice=codice; this.peso=peso; }\n'
                  '    public String getCodice(){ return codice; }\n'
                  '    public int getPeso(){ return peso; }\n'
                  '    @Override public int hashCode(){ return codice.hashCode(); }\n'
                  '    @Override public boolean equals(Object o){ Prodotto that=(Prodotto)o; return '
                  'this.getCodice().equals(that.getCodice()); }\n'
                  '}\n'
                  'public class OperazioniProdotti {\n'
                  '    public Map<Prodotto,Integer> getProdotto2quantita(Map<String,Prodotto> cod2prod, '
                  'Map<String,Integer> cod2qta){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '    private static void assertEq(String n, Object e, Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Map<String,Prodotto> p = new HashMap<>(); p.put("A",new Prodotto("A",10)); p.put("B",new '
                 'Prodotto("B",20));\n'
                 '        Map<String,Integer> q = new HashMap<>(); q.put("A",3);\n'
                 '        Map<Prodotto,Integer> out = new OperazioniProdotti().getProdotto2quantita(p,q);\n'
                 '        assertEq("size",2,out.size()); assertEq("A",3,out.get(new Prodotto("A",0))); '
                 'assertEq("B",-1,out.get(new Prodotto("B",0)));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe',
  'solution_code': 'import java.util.*;\n'
                   'class Prodotto {\n'
                   '    private String codice; private int peso;\n'
                   '    public Prodotto(String codice, int peso){ this.codice=codice; this.peso=peso; }\n'
                   '    public String getCodice(){ return codice; }\n'
                   '    public int getPeso(){ return peso; }\n'
                   '    @Override public int hashCode(){ return codice.hashCode(); }\n'
                   '    @Override public boolean equals(Object o){ Prodotto that=(Prodotto)o; return '
                   'this.getCodice().equals(that.getCodice()); }\n'
                   '}\n'
                   'public class OperazioniProdotti {\n'
                   '    public Map<Prodotto,Integer> getProdotto2quantita(Map<String,Prodotto> cod2prod, '
                   'Map<String,Integer> cod2qta){\n'
                   '        Map<Prodotto,Integer> out = new HashMap<>();\n'
                   '        for (String k : cod2prod.keySet()) {\n'
                   '            out.put(cod2prod.get(k), cod2qta.containsKey(k) ? cod2qta.get(k) : -1);\n'
                   '        }\n'
                   '        return out;\n'
                   '    }\n'
                   '}\n'},
 {'id': 'prodotti_only_present',
  'title': 'OperazioniProdotti.getProdotto2quantita() solo presenti',
  'prompt': 'Variante: includi in output solo prodotti con quantita presente in cod2qta.',
  'source_filename': 'OperazioniProdottiFiltrata.java',
  'starter_code': 'import java.util.*;\n'
                  'class Prodotto {\n'
                  '    private String codice; private int peso;\n'
                  '    public Prodotto(String codice,int peso){ this.codice=codice; this.peso=peso; }\n'
                  '    public String getCodice(){ return codice; }\n'
                  '    public int getPeso(){ return peso; }\n'
                  '    @Override public int hashCode(){ return codice.hashCode(); }\n'
                  '    @Override public boolean equals(Object o){ Prodotto p=(Prodotto)o; return '
                  'this.getCodice().equals(p.getCodice()); }\n'
                  '}\n'
                  'public class OperazioniProdottiFiltrata {\n'
                  '    public Map<Prodotto,Integer> getProdotto2quantita(Map<String,Prodotto> cod2prod, '
                  'Map<String,Integer> cod2qta){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Map<String,Prodotto> p = new HashMap<>(); p.put("A",new Prodotto("A",10)); p.put("B",new '
                 'Prodotto("B",20));\n'
                 '        Map<String,Integer> q = new HashMap<>(); q.put("B",4);\n'
                 '        Map<Prodotto,Integer> out = new OperazioniProdottiFiltrata().getProdotto2quantita(p,q);\n'
                 '        assertEq("size",1,out.size()); assertEq("B",4,out.get(new Prodotto("B",0)));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe'},
 {'id': 'studenti_voti_presenti',
  'title': 'OperazioniStudenti.getStudente2voto()',
  'prompt': 'Implementa getStudente2voto(mat2stud,mat2voto): mappa solo studenti che hanno voto presente.',
  'source_filename': 'OperazioniStudenti.java',
  'starter_code': 'import java.util.*;\n'
                  'class Studente {\n'
                  '    private String matricola; private int eta;\n'
                  '    public Studente(String matricola,int eta){ this.matricola=matricola; this.eta=eta; }\n'
                  '    public String getMatricola(){ return matricola; }\n'
                  '    public int getEta(){ return eta; }\n'
                  '    @Override public int hashCode(){ return matricola.hashCode(); }\n'
                  '    @Override public boolean equals(Object o){ Studente s=(Studente)o; return '
                  'this.getMatricola().equals(s.getMatricola()); }\n'
                  '}\n'
                  'public class OperazioniStudenti {\n'
                  '    public Map<Studente,Integer> getStudente2voto(Map<String,Studente> mat2stud, '
                  'Map<String,Integer> mat2voto){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed = 0;\n'
                 '    private static void assertEq(String n, Object e, Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Map<String,Studente> s = new HashMap<>(); s.put("M1",new Studente("M1",20)); s.put("M2",new '
                 'Studente("M2",21));\n'
                 '        Map<String,Integer> v = new HashMap<>(); v.put("M2",27);\n'
                 '        Map<Studente,Integer> out = new OperazioniStudenti().getStudente2voto(s,v);\n'
                 '        assertEq("size",1,out.size()); assertEq("M2",27,out.get(new Studente("M2",99)));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe'},
 {'id': 'inverti_mappa',
  'title': 'OperazioniSuMappe.invertiMappa()',
  'prompt': 'Implementa invertiMappa: inverti chiavi/valori; se valori duplicati, somma le chiavi originali.',
  'source_filename': 'OperazioniSuMappe.java',
  'starter_code': 'import java.util.*;\n'
                  'public class OperazioniSuMappe {\n'
                  '    public static Map<String,Integer> invertiMappa(Map<Integer,String> mappaVecchia){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        Map<Integer,String> m = new HashMap<>(); m.put(1,"A"); m.put(2,"B"); m.put(3,"A");\n'
                 '        Map<String,Integer> out = OperazioniSuMappe.invertiMappa(m);\n'
                 '        assertEq("A",4,out.get("A")); assertEq("B",2,out.get("B"));\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe'},
 {'id': 'autore2canzoni',
  'title': 'RaggruppatoreCanzoniPerAutore.autore2canzoni()',
  'prompt': 'Raggruppa le canzoni per autore in una mappa autore -> lista canzoni.',
  'source_filename': 'RaggruppatoreCanzoniPerAutore.java',
  'starter_code': 'import java.util.*;\n'
                  'class Canzone { private String titolo; private String autore; public Canzone(String titolo,String '
                  'autore){ this.titolo=titolo; this.autore=autore; } public String getAutore(){ return autore; } '
                  'public String getTitolo(){ return titolo; } }\n'
                  'public class RaggruppatoreCanzoniPerAutore {\n'
                  '    private List<Canzone> elencoCanzoni = new ArrayList<>();\n'
                  '    public void aggiungiCanzone(Canzone c){ this.elencoCanzoni.add(c); }\n'
                  '    public Map<String,List<Canzone>> autore2canzoni(){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        RaggruppatoreCanzoniPerAutore r = new RaggruppatoreCanzoniPerAutore();\n'
                 '        r.aggiungiCanzone(new Canzone("C1","A1")); r.aggiungiCanzone(new Canzone("C2","A1")); '
                 'r.aggiungiCanzone(new Canzone("C3","A2"));\n'
                 '        Map<String,List<Canzone>> m = r.autore2canzoni();\n'
                 '        assertEq("keys",2,m.size()); assertEq("a1",2,m.get("A1").size());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe'},
 {'id': 'regista2film',
  'title': 'RaggruppatoreFilmPerRegista.regista2film()',
  'prompt': 'Raggruppa i film per regista in una mappa regista -> lista film.',
  'source_filename': 'RaggruppatoreFilmPerRegista.java',
  'starter_code': 'import java.util.*;\n'
                  'class Film { private String titolo; private String regista; public Film(String titolo,String '
                  'regista){ this.titolo=titolo; this.regista=regista; } public String getTitolo(){ return titolo; } '
                  'public String getRegista(){ return regista; } }\n'
                  'public class RaggruppatoreFilmPerRegista {\n'
                  '    private List<Film> elencoFilm = new ArrayList<>();\n'
                  '    public void aggiungiProdotto(Film film){ this.elencoFilm.add(film); }\n'
                  '    public Map<String,List<Film>> regista2film(){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        RaggruppatoreFilmPerRegista r = new RaggruppatoreFilmPerRegista();\n'
                 '        r.aggiungiProdotto(new Film("F1","R1")); r.aggiungiProdotto(new Film("F2","R1")); '
                 'r.aggiungiProdotto(new Film("F3","R2"));\n'
                 '        Map<String,List<Film>> m = r.regista2film();\n'
                 '        assertEq("keys",2,m.size()); assertEq("r1",2,m.get("R1").size());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe'},
 {'id': 'autore2libri',
  'title': 'RaggruppatoreLibriPerAutore.autore2libri()',
  'prompt': 'Raggruppa i libri per autore in una mappa autore -> lista libri.',
  'source_filename': 'RaggruppatoreLibriPerAutore.java',
  'starter_code': 'import java.util.*;\n'
                  'class Libro { private String titolo; private String autore; public Libro(String titolo,String '
                  'autore){ this.titolo=titolo; this.autore=autore; } public String getAutore(){ return autore; } '
                  'public String getTitolo(){ return titolo; } }\n'
                  'public class RaggruppatoreLibriPerAutore {\n'
                  '    private List<Libro> elencoLibri = new ArrayList<>();\n'
                  '    public void aggiungiLibro(Libro l){ this.elencoLibri.add(l); }\n'
                  '    public Map<String,List<Libro>> autore2libri(){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        RaggruppatoreLibriPerAutore r = new RaggruppatoreLibriPerAutore();\n'
                 '        r.aggiungiLibro(new Libro("T1","A1")); r.aggiungiLibro(new Libro("T2","A1")); '
                 'r.aggiungiLibro(new Libro("T3","A2"));\n'
                 '        Map<String,List<Libro>> m = r.autore2libri();\n'
                 '        assertEq("keys",2,m.size()); assertEq("a1",2,m.get("A1").size());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe'},
 {'id': 'marca2prodotti',
  'title': 'RaggruppatoreProdottiPerMarca.marca2prodotto()',
  'prompt': 'Raggruppa i prodotti per marca in una mappa marca -> lista prodotti.',
  'source_filename': 'RaggruppatoreProdottiPerMarca.java',
  'starter_code': 'import java.util.*;\n'
                  'class Prodotto { private String codice; private String marca; public Prodotto(String codice,String '
                  'marca){ this.codice=codice; this.marca=marca; } public String getCodice(){ return codice; } public '
                  'String getMarca(){ return marca; } }\n'
                  'public class RaggruppatoreProdottiPerMarca {\n'
                  '    private List<Prodotto> elencoProdotti = new ArrayList<>();\n'
                  '    public void aggiungiProdotto(Prodotto p){ this.elencoProdotti.add(p); }\n'
                  '    public Map<String,List<Prodotto>> marca2prodotto(){\n'
                  '        // TODO\n'
                  '        return null;\n'
                  '    }\n'
                  '}\n',
  'test_runner': 'import java.util.*;\n'
                 'public class TestRunner {\n'
                 '    private static int failed=0;\n'
                 '    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; '
                 'System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }\n'
                 '    public static void main(String[] args){\n'
                 '        RaggruppatoreProdottiPerMarca r = new RaggruppatoreProdottiPerMarca();\n'
                 '        r.aggiungiProdotto(new Prodotto("P1","M1")); r.aggiungiProdotto(new Prodotto("P2","M1")); '
                 'r.aggiungiProdotto(new Prodotto("P3","M2"));\n'
                 '        Map<String,List<Prodotto>> m = r.marca2prodotto();\n'
                 '        assertEq("keys",2,m.size()); assertEq("m1",2,m.get("M1").size());\n'
                 '        if(failed==0) System.out.println("ALL_TESTS_PASSED");\n'
                 '    }\n'
                 '}\n',
  'esonero': 3,
  'topic': 'mappe'}]
