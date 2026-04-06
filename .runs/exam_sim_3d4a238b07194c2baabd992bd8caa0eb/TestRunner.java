public class TestRunner {
    private static int failed = 0;
    private static void assertEq(String n, boolean e, boolean a){ if(e!=a){ failed++; System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }
    public static void main(String[] args){
        Persone p = new Persone(5);
        p.aggiungiNome("Luca",0); p.aggiungiNome("Anna",1); p.aggiungiNome("Luca",2);
        assertEq("luca", true, p.verificaDuplicati("Luca"));
        assertEq("anna", false, p.verificaDuplicati("Anna"));
        if(failed==0) System.out.println("ALL_TESTS_PASSED");
    }
}
