import pygame
import time

PRETO=(0,0,0)
BRANCO=(255,255,255)
VERMELHO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)

largurajanela=800
alturajanela=700

def mover(figura,dimensaojanela):
    bordaesquerda=0
    bordadireita=dimensaojanela[0]
    bordasuperior=0
    bordaeinferior=dimensaojanela[1]

    if figura['objeto'].top <bordasuperior or figura['objeto'].bottom>bordaeinferior:
        figura['vel'][1]=-figura['vel'][1]