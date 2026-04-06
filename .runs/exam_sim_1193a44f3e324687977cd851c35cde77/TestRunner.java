import java.util.*;
public class TestRunner {
    private static int failed=0;
    private static void assertEq(String n,Object e,Object a){ if(!Objects.equals(e,a)){ failed++; System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }
    public static void main(String[] args){
        Map<Integer,String> m = new HashMap<>(); m.put(1,"A"); m.put(2,"B"); m.put(3,"A");
        Map<String,Integer> out = OperazioniSuMappe.invertiMappa(m);
        assertEq("A",4,out.get("A")); assertEq("B",2,out.get("B"));
        if(failed==0) System.out.println("ALL_TESTS_PASSED");
    }
}
