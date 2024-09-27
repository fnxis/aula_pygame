import pygame

pygame.init()

janela=pygame.display.set_mode((777,777))
pygame.display.set_caption("Free Fire 2")
deve_continuar=True
while deve_continuar:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            deve_continuar=False