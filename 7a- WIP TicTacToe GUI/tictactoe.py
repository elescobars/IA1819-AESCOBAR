import sys
import pygame
import numpy as np

pygame.init()

ANCHO_VENTANA = 600  # px
ALTURA_VENTANA = 600  # px
ANCHO_LINEA = 5  # px
ANCHO_LINEA_GANADOR = 10 # px
RADIO_CIRCULO = 40  # px
ANCHO_CIRCULO = 10  # px
ANCHO_CRUZ = 20  # px
PADDING_CRUZ = 25  # px
TABLERO_FILAS = 5
TABLERO_COLUMNAS = 5

# colores en constantes
COLOR_FONDO = (68, 71, 90)  # rgb
COLOR_LINEA = (40, 42, 54)  # rgb
COLOR_CIRCULOS = (139, 233, 253)  # rgb
COLOR_CRUCES = (255, 85, 85)  # rgb

jugador = 1
juego_terminado = False

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTURA_VENTANA))
pygame.display.set_caption("TicTacToe 5x5 PvP")
screen.fill(COLOR_FONDO)

# tablero
tablero = np.zeros((TABLERO_FILAS, TABLERO_COLUMNAS))


def dibuja_lineas():
    # linea horizontal 1
    pygame.draw.line(screen, COLOR_LINEA, (0, 120), (600, 120), ANCHO_LINEA)
    # linea horizontal 2
    pygame.draw.line(screen, COLOR_LINEA, (0, 240), (600, 240), ANCHO_LINEA)
    # linea horizontal 3
    pygame.draw.line(screen, COLOR_LINEA, (0, 360), (600, 360), ANCHO_LINEA)
    # linea horizontal 4
    pygame.draw.line(screen, COLOR_LINEA, (0, 480), (600, 480), ANCHO_LINEA)
    # linea vertical 1
    pygame.draw.line(screen, COLOR_LINEA, (120, 0), (120, 600), ANCHO_LINEA)
    # linea vertical 2
    pygame.draw.line(screen, COLOR_LINEA, (240, 0), (240, 600), ANCHO_LINEA)
    # linea vertical 3
    pygame.draw.line(screen, COLOR_LINEA, (360, 0), (360, 600), ANCHO_LINEA)
    # linea vertical 4
    pygame.draw.line(screen, COLOR_LINEA, (480, 0), (480, 600), ANCHO_LINEA)


# funcion para marcar espacios en el tablero dependiendo de quien los selecciona
def marcar_espacio(fila, columna, jugador):
    tablero[fila][columna] = jugador


# funcion que comprueba si el espacio determinado por fila y columna esta disponible
def espacio_disponible(fila, columna):
    return tablero[fila][columna] == 0


# funcion que recorre el tablero y determina si esta lleno o no
def tablero_lleno():
    for fil in range(TABLERO_FILAS):
        for col in range(TABLERO_COLUMNAS):
            if tablero[fil][col] == 0:
                return False
    return True


def busca_ganador(jugador):
    # busca ganador vertical
    for col in range(TABLERO_COLUMNAS):
        if (
            tablero[0][col] == jugador
            and tablero[1][col] == jugador
            and tablero[2][col] == jugador
            and tablero[3][col] == jugador
            and tablero[4][col] == jugador
        ):
            dibuja_linea_ganador_vert(col, jugador)
            return True

    # busca ganador horizontal
    for fil in range(TABLERO_FILAS):
        if (
            tablero[fil][0] == jugador
            and tablero[fil][1] == jugador
            and tablero[fil][2] == jugador
            and tablero[fil][3] == jugador
            and tablero[fil][4] == jugador
        ):
            dibuja_linea_ganador_horz(fil, jugador)
            return True

    # busca ganador en la diagonal ascendente
    if (
        tablero[4][0] == jugador
        and tablero[3][1] == jugador
        and tablero[2][2] == jugador
        and tablero[1][3] == jugador
        and tablero[0][4] == jugador
    ):
        dibuja_linea_ganador_diag_asc(jugador)
        return True

    # busca ganador en la diagonal descendente
    if (
        tablero[0][0] == jugador
        and tablero[1][1] == jugador
        and tablero[2][2] == jugador
        and tablero[3][3] == jugador
        and tablero[4][4] == jugador
    ):
        dibuja_linea_ganador_diag_desc(jugador)
        return True

    # aun no hay ganador
    return False


def dibuja_linea_ganador_vert(col, jugador):
    posX = col * 120 + 60

    if jugador == 1:
        color = COLOR_CIRCULOS
    elif jugador == 2:
        color = COLOR_CRUCES

    pygame.draw.line(screen, color, (posX, 15), (posX, ALTURA_VENTANA - 15), ANCHO_LINEA_GANADOR)


def dibuja_linea_ganador_horz(fil, jugador):
    posY = fil * 120 + 60

    if jugador == 1:
        color = COLOR_CIRCULOS
    elif jugador == 2:
        color = COLOR_CRUCES

    pygame.draw.line(screen, color, (15, posY), (ANCHO_VENTANA - 15, posY), ANCHO_LINEA_GANADOR)


def dibuja_linea_ganador_diag_asc(jugador):
    if jugador == 1:
        color = COLOR_CIRCULOS
    elif jugador == 2:
        color = COLOR_CRUCES

    pygame.draw.line(screen, color, (15, ALTURA_VENTANA - 15), (ANCHO_VENTANA - 15, 15), ANCHO_LINEA_GANADOR)


def dibuja_linea_ganador_diag_desc(jugador):
    if jugador == 1:
        color = COLOR_CIRCULOS
    elif jugador == 2:
        color = COLOR_CRUCES

    pygame.draw.line(screen, color, (15, 15), (ANCHO_VENTANA - 15, ALTURA_VENTANA - 15), ANCHO_LINEA_GANADOR)


def dibuja_figuras():
    for fil in range(TABLERO_FILAS):
        for col in range(TABLERO_COLUMNAS):
            if tablero[fil][col] == 1:
                # ancho de la ventana dividida entre 5, despues ancho de la ventana dividida entre 10
                pygame.draw.circle(
                    screen,
                    COLOR_CIRCULOS,
                    (int(col * 120 + 60), int(fil * 120 + 60)),
                    RADIO_CIRCULO,
                    ANCHO_CIRCULO,
                )
            elif tablero[fil][col] == 2:
                pygame.draw.line(
                    screen,
                    COLOR_CRUCES,
                    (col * 120 + PADDING_CRUZ, fil * 120 + 120 - PADDING_CRUZ),
                    (col * 120 + 120 - PADDING_CRUZ, fil * 120 + PADDING_CRUZ),
                    ANCHO_CRUZ,
                )
                pygame.draw.line(
                    screen,
                    COLOR_CRUCES,
                    (col * 120 + PADDING_CRUZ, fil * 120 + PADDING_CRUZ),
                    (col * 120 + 120 - PADDING_CRUZ, fil * 120 + 120 - PADDING_CRUZ),
                    ANCHO_CRUZ,
                )


def reiniciar():
    screen.fill(COLOR_FONDO)
    dibuja_lineas()
    for fil in range(TABLERO_FILAS):
        for col in range(TABLERO_COLUMNAS):
            tablero[fil][col] = 0


dibuja_lineas()

jugador = 1
juego_terminado = False

# main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not juego_terminado:
            mouseX = event.pos[0]  # coordenada x
            mouseY = event.pos[1]  # coordenada y
            fil_click = int(mouseY // 120)
            col_click = int(mouseX // 120)

            if espacio_disponible(fil_click, col_click):
                if jugador == 1:
                    marcar_espacio(fil_click, col_click, 1)
                    if busca_ganador(jugador):
                        juego_terminado = True
                    jugador = 2
                elif jugador == 2:
                    marcar_espacio(fil_click, col_click, 2)
                    if busca_ganador(jugador):
                        juego_terminado = True
                    jugador = 1
                dibuja_figuras()
                # mostrar el estado del juego en el tablero de consola
                # print(tablero)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reiniciar()
                jugador = 1
                juego_terminado = False

    pygame.display.update()
