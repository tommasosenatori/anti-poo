import java.util.*;
public class TestRunner {
    private static int failed = 0;
    private static void assertEq(String n, Object e, Object a){ if(!Objects.equals(e,a)){ failed++; System.out.println("FAIL|"+n+"|expected="+e+"|actual="+a);} }
    public static void main(String[] args){
        Map<String,Studente> s = new HashMap<>(); s.put("M1",new Studente("M1",20)); s.put("M2",new Studente("M2",21));
        Map<String,Integer> v = new HashMap<>(); v.put("M2",27);
        Map<Studente,Integer> out = new OperazioniStudenti().getStudente2voto(s,v);
        assertEq("size",1,out.size()); assertEq("M2",27,out.get(new Studente("M2",99)));
        if(failed==0) System.out.println("ALL_TESTS_PASSED");
    }
}
