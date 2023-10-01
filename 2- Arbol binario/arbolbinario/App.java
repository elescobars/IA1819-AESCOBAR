package arbolbinario;

public class App {

    public static void main(String[] args) {

        ArbolBinario arbolVacio = new ArbolBinario();
        if (arbolVacio.vacio()) {
            System.out.println("El arbolVacio esta vacio!");
        } else {
            System.out.println("El arbolVacio no esta vacio!");
        }

        ArbolBinario ab = new ArbolBinario();
        ab.agregar(18);
        ab.agregar(22);
        ab.agregar(16);
        ab.agregar(14);
        ab.agregar(17);
        ab.agregar(24);
        ab.agregar(21);

        int valorPrueba = 24;
        System.out.println("\nBusqueda en el arbol: el arbol contiene un " + valorPrueba + "? " + ab.buscaNodo(valorPrueba));

        System.out.println("\nRecorrido del arbol: ");
        ab.recorrerEnAnchura();

        System.out.println("\nImpresion del arbol binario:");
        ab.imprimir(System.out);
    }

}
