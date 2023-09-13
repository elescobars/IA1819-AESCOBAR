package arbolbinario;

public class App {
    
    public static void main(String[] args) {

        ArbolBinario ab = new ArbolBinario();
        ab.agregar(6);
        ab.agregar(4);
        ab.agregar(8);
        ab.agregar(3);
        ab.agregar(5);
        ab.agregar(7);
        ab.agregar(9);

        int valorPrueba = 6;
        System.out.println("El arbol contiene un " + valorPrueba + ": " + ab.buscaNodo(valorPrueba));

        System.out.println("Recorrido del arbol: ");
        ab.recorrerEnAnchura();

    }

}
