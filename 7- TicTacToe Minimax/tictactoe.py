import sys
import pygame
import numpy as np

from constantes import *

pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTURA_VENTANA))
pygame.display.set_caption("TicTacToe 5x5 Minimax")
screen.fill(COLOR_FONDO)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()