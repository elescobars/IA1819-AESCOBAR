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
print(tablero)


def dibuja_lineas():
    # linea horizontal 1
    pygame.draw.line(screen, COLOR_LINEA, (0, 200), (600, 200), ANCHO_LINEA)
    # linea horizontal 2
    pygame.draw.line(screen, COLOR_LINEA, (0, 400), (600, 400), ANCHO_LINEA)
    # linea vertical 1
    pygame.draw.line(screen, COLOR_LINEA, (200, 0), (200, 600), ANCHO_LINEA)
    # linea vertical 2
    pygame.draw.line(screen, COLOR_LINEA, (400, 0), (400, 600), ANCHO_LINEA)


def marcar_espacio(fila, columna, jugador):
    tablero[fila][columna] = jugador


dibuja_lineas()

# loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
