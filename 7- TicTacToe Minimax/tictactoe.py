import sys
import pygame
import numpy as np

from constantes import *

pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTURA_VENTANA))
pygame.display.set_caption("TicTacToe 5x5 Minimax")
screen.fill(COLOR_FONDO)


class Tablero:
    def __init__(self):
        self.cuadros = np.zeros((FILAS, COLUMNAS))
        self.cuadrados_vacios = self.cuadros
        self.cuadrados_marcados = 0


    def estado_final(self):
        '''
            regresa 0 si no hay ganador aun
            regresa 1 si gana el jugador 1
            regresa 2 si gana el jugador 2
        '''
        # gana vertical
        for col in range(COLUMNAS):
            if (
                self.cuadros[0][col] 
                == self.cuadros[1][col] 
                == self.cuadros[2][col] 
                == self.cuadros[3][col] 
                == self.cuadros[4][col] 
                != 0
            ):
                return self.cuadros[0][col]
            
        # gana horizontal
        for fil in range(FILAS):
            if (
                self.cuadros[fil][0] 
                == self.cuadros[fil][1]
                == self.cuadros[fil][2]
                == self.cuadros[fil][3]
                == self.cuadros[fil][4]
                != 0
            ):
                return self.cuadros[fil][0]
            
        # gana diagonal desc
        if (
            self.cuadros[0][0]
            == self.cuadros[1][1]
            == self.cuadros[2][2]
            == self.cuadros[3][3]
            == self.cuadros[4][4]
            != 0
        ):
            return self.cuadros[2][2]
        
        # gana diagonal asc
        if (
            self.cuadros[4][0]
            == self.cuadros[3][1]
            == self.cuadros[2][2]
            == self.cuadros[1][3]
            == self.cuadros[0][4]
            != 0
        ):
            return self.cuadros[2][2]
        
        # no hay ganador aun
        return 0


    def marcar_cuadro(self, fil, col, jugador):
        self.cuadros[fil][col] = jugador
        self.cuadrados_marcados += 1


    def cuadrado_vacio(self, fil, col):
        return self.cuadros[fil][col] == 0


    def get_cuadrados_vacios(self):
        cuadrados_vacios = []
        for fil in range(FILAS):
            for col in range(COLUMNAS):
                if self.cuadrado_vacio(fil, col):
                    cuadrados_vacios.append((fil, col))


    def lleno(self):
        return self.cuadrados_marcados == 25


    def vacio(self):
        return self.cuadrados_marcados == 0


class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.jugador = 1 # 1: circulos, 2: cruces
        self.dbj_lineas()


    def dbj_lineas(self):
        for x in range(1, COLUMNAS):
            pygame.draw.line( # lineas verticales
                screen, 
                COLOR_LINEA, 
                (TAM_CUADRO * x, 0), 
                (TAM_CUADRO * x, ALTURA_VENTANA), 
                GROSOR_LINEA
            )
        for x in range(1, FILAS):
            pygame.draw.line( # lineas horizontales
                screen,
                COLOR_LINEA,
                (0, TAM_CUADRO * x),
                (ANCHO_VENTANA, TAM_CUADRO * x),
                GROSOR_LINEA
            )


    def sig_turno(self):
        self.jugador = self.jugador % 2 + 1


    def dbj_figura(self, fil, col):
        if self.jugador == 1:
            # dibuja circulo
            centro = (
                col * TAM_CUADRO + TAM_CUADRO // 2,
                fil * TAM_CUADRO + TAM_CUADRO // 2
            )
            pygame.draw.circle(
                screen,
                COLOR_CIRCULOS,
                centro,
                RADIO,
                GROSOR_CIRCULO
            )
            pass
        elif self.jugador == 2:
            # dibuja cruz
            # linea desc
            inicio_desc = (
                col * TAM_CUADRO + ESPACIO,
                fil * TAM_CUADRO + ESPACIO
            )
            fin_desc = (
                col * TAM_CUADRO + TAM_CUADRO - ESPACIO,
                fil * TAM_CUADRO + TAM_CUADRO - ESPACIO
            )
            pygame.draw.line(
                screen,
                COLOR_CRUCES,
                inicio_desc,
                fin_desc,
                GROSOR_CRUZ
            )

            # linea asc
            inicio_asc = (
                col * TAM_CUADRO + ESPACIO,
                fil * TAM_CUADRO + TAM_CUADRO - ESPACIO
            )
            fin_asc = (
                col * TAM_CUADRO + TAM_CUADRO - ESPACIO,
                fil * TAM_CUADRO + ESPACIO
            )
            pygame.draw.line(
                screen,
                COLOR_CRUCES,
                inicio_asc,
                fin_asc,
                GROSOR_CRUZ
            )


def main():
    juego = Juego()
    tablero = juego.tablero

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                fil = pos[1] // TAM_CUADRO
                col = pos[0] // TAM_CUADRO
                if tablero.cuadrado_vacio(fil, col):
                    tablero.marcar_cuadro(fil, col, juego.jugador)
                    juego.dbj_figura(fil, col)
                    juego.sig_turno()

        pygame.display.update()


main()