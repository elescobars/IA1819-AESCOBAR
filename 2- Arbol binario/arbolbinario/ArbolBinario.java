package arbolbinario;

import java.io.PrintStream;
import java.util.LinkedList;
import java.util.Queue;

public class ArbolBinario {
    Nodo raiz;

    private Nodo agregarRecursivo(Nodo actual, int valor) {
        if (actual == null) {
            return new Nodo(valor);
        }

        if (valor < actual.valor) {
            actual.izquierda = agregarRecursivo(actual.izquierda, valor);
        } else if (valor > actual.valor) {
            actual.derecha = agregarRecursivo(actual.derecha, valor);
        } else {
            return actual;
        }

        return actual;
    }

    private boolean buscaNodoRecursivo(Nodo actual, int valor) {
        if (actual == null) {
            return false;
        }
        if (valor == actual.valor) {
            return true;
        }
        // Utilizando la busqueda en pre orden, pues visita primero los nodos izquierdos
        return valor < actual.valor ? buscaNodoRecursivo(actual.izquierda, valor)
                : buscaNodoRecursivo(actual.derecha, valor);
    }

    // Imprimen los nodos en el orden en que son visitados
    private void recorrerEnOrdenRecursivo(Nodo nodo) {
        if (nodo != null) {
            recorrerEnOrdenRecursivo(nodo.izquierda);
            System.out.println(nodo.valor);
            recorrerEnOrdenRecursivo(nodo.derecha);
        }
    }

    private void recorrerEnPreOrdenRecursivo(Nodo nodo) {
        if (nodo != null) {
            System.out.println(nodo.valor);
            recorrerEnPreOrdenRecursivo(nodo.izquierda);
            recorrerEnPreOrdenRecursivo(nodo.derecha);
        }
    }

    private void recorrerEnPostOrdenRecursivo(Nodo nodo) {
        if (nodo != null) {
            recorrerEnPostOrdenRecursivo(nodo.izquierda);
            recorrerEnPostOrdenRecursivo(nodo.derecha);
            System.out.println(nodo.valor);
        }
    }

    private void recorrerParaImpresion(StringBuilder sb, String espacio, String apuntador, Nodo nodo) {
        if (nodo != null) {
            sb.append(espacio);
            sb.append(apuntador);
            sb.append("Nodo ");
            sb.append(nodo.valor);
            sb.append("\n");

            StringBuilder pb = new StringBuilder(espacio);
            pb.append("│  ");

            String espacioAmbos = pb.toString();
            String espacioDerecha = "└──";
            String espacioIzquierda = (nodo.derecha != null) ? "├──" : "└──";

            recorrerParaImpresion(sb, espacioAmbos, espacioIzquierda, nodo.izquierda);
            recorrerParaImpresion(sb, espacioAmbos, espacioDerecha, nodo.derecha);
        }
    }

    public void agregar(int valor) {
        raiz = agregarRecursivo(raiz, valor);
    }

    public boolean buscaNodo(int valor) {
        return buscaNodoRecursivo(raiz, valor);
    }

    // Busquedas en profundidad
    public void recorrerEnOrden() {
        recorrerEnOrdenRecursivo(raiz);
    }

    public void recorrerEnPreOrden() {
        recorrerEnPreOrdenRecursivo(raiz);
    }

    public void recorrerEnPostOrden() {
        recorrerEnPostOrdenRecursivo(raiz);
    }

    // Busqueda en anchura
    public void recorrerEnAnchura() {
        if (raiz == null) {
            return;
        }

        Queue<Nodo> nodos = new LinkedList<>();
        nodos.add(raiz);

        while (!nodos.isEmpty()) {
            Nodo nodo = nodos.remove();
            System.out.println(nodo.valor);

            if (nodo.izquierda != null) {
                nodos.add(nodo.izquierda);
            }

            if (nodo.derecha != null) {
                nodos.add(nodo.derecha);
            }
        }
    }

    public void imprimir(PrintStream os) {
        StringBuilder sb = new StringBuilder();
        recorrerParaImpresion(sb, "", "", raiz);
        os.print(sb.toString());
    }

    public boolean vacio() {
        if (raiz == null) {
            return true;
        }

        return false;
    }
}
