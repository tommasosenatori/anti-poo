public class TestRunner {
    private static int failed = 0;
    private static void assertEq(String n, Mese e, Mese a){ if(e!=a){ failed++; System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }
    public static void main(String[] args){
        assertEq("jan", Mese.LUGLIO, Mese.GENNAIO.corrispondenzaStagionale());
        assertEq("aug", Mese.FEBBRAIO, Mese.AGOSTO.corrispondenzaStagionale());
        if(failed==0) System.out.println("ALL_TESTS_PASSED");
    }
}
