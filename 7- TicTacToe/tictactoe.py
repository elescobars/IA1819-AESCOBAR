import pygame, sys
import numpy as np

pygame.init()

ANCHO_VENTANA = 600  # px
ALTURA_VENTANA = 600  # px
ANCHO_LINEA = 10  # px
TABLERO_FILAS = 3
TABLERO_COLUMNAS = 3

# colores en constantes
COLOR_FONDO = (68, 71, 90)  # rgb
COLOR_LINEA = (40, 42, 54)  # rgb

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTURA_VENTANA))
pygame.display.set_caption("Gato Minimax")
screen.fill(COLOR_FONDO)

# tablero
tablero = np.zeros((TABLERO_FILAS, TABLERO_COLUMNAS))


def dibuja_lineas():
    # linea horizontal 1
    pygame.draw.line(screen, COLOR_LINEA, (0, 200), (600, 200), ANCHO_LINEA)
    # linea horizontal 2
    pygame.draw.line(screen, COLOR_LINEA, (0, 400), (600, 400), ANCHO_LINEA)
    # linea vertical 1
    pygame.draw.line(screen, COLOR_LINEA, (200, 0), (200, 600), ANCHO_LINEA)
    # linea vertical 2
    pygame.draw.line(screen, COLOR_LINEA, (400, 0), (400, 600), ANCHO_LINEA)


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


dibuja_lineas()

jugador = 1

# loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # coordenada x
            mouseY = event.pos[1]  # coordenada y
            fil_click = int(mouseY // 200)
            col_click = int(mouseX // 200)

            if espacio_disponible(fil_click, col_click):
                if jugador == 1:
                    marcar_espacio(fil_click, col_click, 1)
                    jugador = 2
                elif jugador == 2:
                    marcar_espacio(fil_click, col_click, 2)
                    jugador = 1

    pygame.display.update()
