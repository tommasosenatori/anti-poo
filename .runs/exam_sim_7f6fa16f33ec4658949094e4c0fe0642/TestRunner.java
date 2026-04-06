public class TestRunner {
    private static int failed = 0;
    private static void assertEq(String n,double e,double a){ if(Math.abs(e-a)>1e-9){ failed++; System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }
    public static void main(String[] args){
        CalcolatoreAreaTrapezio c = new CalcolatoreAreaTrapezio();
        assertEq("ok",15.0,c.calcolaArea(4,6,3));
        assertEq("invalid",-1.0,c.calcolaArea(8,5,3));
        if(failed==0) System.out.println("ALL_TESTS_PASSED");
    }
}
