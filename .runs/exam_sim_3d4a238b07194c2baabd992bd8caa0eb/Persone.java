public class Persone {
    private String[] nomi;
    public Persone(int numeroPersone) { this.nomi = new String[numeroPersone]; }
    public void aggiungiNome(String nome, int indice) { this.nomi[indice] = nome; }
    public boolean verificaDuplicati(String nome) {
        // TODO
        return false;
    }
}
