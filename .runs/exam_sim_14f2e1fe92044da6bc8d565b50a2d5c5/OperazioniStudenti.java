import java.util.*;
class Studente {
    private String matricola; private int eta;
    public Studente(String matricola,int eta){ this.matricola=matricola; this.eta=eta; }
    public String getMatricola(){ return matricola; }
    public int getEta(){ return eta; }
    @Override public int hashCode(){ return matricola.hashCode(); }
    @Override public boolean equals(Object o){ Studente s=(Studente)o; return this.getMatricola().equals(s.getMatricola()); }
}
public class OperazioniStudenti {
    public Map<Studente,Integer> getStudente2voto(Map<String,Studente> mat2stud, Map<String,Integer> mat2voto){
        // TODO
        return null;
    }
}
