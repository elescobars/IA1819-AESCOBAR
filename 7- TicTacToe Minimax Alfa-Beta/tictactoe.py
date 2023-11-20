from random import choice
from math import inf

tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def TableroJuego(tablero):
    simbolos = {1: "X", -1: "O", 0: " "}
    for x in tablero:
        for y in x:
            car = simbolos[y]
            print(f"| {car} |", end="")
        print("\n" + "---------------")
    print("===============")


def LimpiaTablero(tablero):
    for x, fil in enumerate(tablero):
        for y, col in enumerate(fil):
            tablero[x][y] = 0


def JugadorGanador(tablero, jugador):
    conditions = [
        [tablero[0][0], tablero[0][1], tablero[0][2]],
        [tablero[1][0], tablero[1][1], tablero[1][2]],
        [tablero[2][0], tablero[2][1], tablero[2][2]],
        [tablero[0][0], tablero[1][0], tablero[2][0]],
        [tablero[0][1], tablero[1][1], tablero[2][1]],
        [tablero[0][2], tablero[1][2], tablero[2][2]],
        [tablero[0][0], tablero[1][1], tablero[2][2]],
        [tablero[0][2], tablero[1][1], tablero[2][0]],
    ]

    if [jugador, jugador, jugador] in conditions:
        return True

    return False


def JuegoGanado(tablero):
    return JugadorGanador(tablero, 1) or JugadorGanador(tablero, -1)


def ImprimeResultado(tablero):
    if JugadorGanador(tablero, 1):
        print("Gana la X! " + "\n")

    elif JugadorGanador(tablero, -1):
        print("Gana la O! " + "\n")

    else:
        print("Empate!" + "\n")


def Vacios(tablero):
    vacio = []
    for x, fil in enumerate(tablero):
        for y, col in enumerate(fil):
            if tablero[x][y] == 0:
                vacio.append([x, y])

    return vacio


def TableroLleno(tablero):
    if len(Vacios(tablero)) == 0:
        return True
    return False


def SetMovimiento(tablero, x, y, jugador):
    tablero[x][y] = jugador


def MovimientoJugador(tablero):
    e = True
    movimientos = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
    }
    while e:
        try:
            movimiento = int(input("Seleccione una casilla del 1-9: "))
            if movimiento < 1 or movimiento > 9:
                print("Movimiento invalido! Intente de nuevo")
            elif not (movimientos[movimiento] in Vacios(tablero)):
                print("La casilla ya esta tomada!")
            else:
                SetMovimiento(
                    tablero, movimientos[movimiento][0], movimientos[movimiento][1], 1
                )
                TableroJuego(tablero)
                e = False
        except (KeyError, ValueError):
            print("Ingrese un numero!")


def ObtenPuntuacion(tablero):
    if JugadorGanador(tablero, 1):
        return 10

    elif JugadorGanador(tablero, -1):
        return -10

    else:
        return 0


def MinimaxAlfaBeta(tablero, profundidad, alfa, beta, jugador):
    fil = -1
    col = -1
    if profundidad == 0 or JuegoGanado(tablero):
        return [fil, col, ObtenPuntuacion(tablero)]

    else:
        for celda in Vacios(tablero):
            SetMovimiento(tablero, celda[0], celda[1], jugador)
            puntuacion = MinimaxAlfaBeta(tablero, profundidad - 1, alfa, beta, -jugador)
            if jugador == 1:
                # X is always the max jugador
                if puntuacion[2] > alfa:
                    alfa = puntuacion[2]
                    fil = celda[0]
                    col = celda[1]

            else:
                if puntuacion[2] < beta:
                    beta = puntuacion[2]
                    fil = celda[0]
                    col = celda[1]

            SetMovimiento(tablero, celda[0], celda[1], 0)

            if alfa >= beta:
                break

        if jugador == 1:
            return [fil, col, alfa]

        else:
            return [fil, col, beta]


def Compara_O(tablero):
    if len(Vacios(tablero)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        SetMovimiento(tablero, x, y, -1)
        TableroJuego(tablero)

    else:
        resultado = MinimaxAlfaBeta(tablero, len(Vacios(tablero)), -inf, inf, -1)
        SetMovimiento(tablero, resultado[0], resultado[1], -1)
        TableroJuego(tablero)


def Compara_X(tablero):
    if len(Vacios(tablero)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        SetMovimiento(tablero, x, y, 1)
        TableroJuego(tablero)

    else:
        resultado = MinimaxAlfaBeta(tablero, len(Vacios(tablero)), -inf, inf, 1)
        SetMovimiento(tablero, resultado[0], resultado[1], 1)
        TableroJuego(tablero)


def HacerMovimiento(tablero, jugador, modo):
    if modo == 1:
        if jugador == 1:
            MovimientoJugador(tablero)

        else:
            Compara_O(tablero)
    else:
        if jugador == 1:
            Compara_O(tablero)
        else:
            Compara_X(tablero)


# Modo de juego de jugador vs IA que inicia el flujo recursivo de Minimax
def JugadorVersusIA():
    while True:
        try:
            orden = int(
                input("Seleccione 1 para jugar primero y 2 para jugar segundo: ")
            )
            if not (orden == 1 or orden == 2):
                print("Por favor elija 1 o 2!")
            else:
                break
        except (KeyError, ValueError):
            print("Ingrese un numero!")

    LimpiaTablero(tablero)
    if orden == 2:
        jugadorActual = -1
    else:
        jugadorActual = 1

    while not (TableroLleno(tablero) or JuegoGanado(tablero)):
        HacerMovimiento(tablero, jugadorActual, 1)
        jugadorActual *= -1

    ImprimeResultado(tablero)


# Llamada principal
print("=================================================")
print("Juego del gato utilizando Minimax con poda Alfa-B")
print("=================================================")
JugadorVersusIA()
