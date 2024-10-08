import pygame
import time

PRETO=(0,0,0)
BRANCO=(255,255,255)
VERMELHO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)

LARGURAJANELA=800
ALTURAJANELA=700

def mover(figura,dimensaojanela):
    bordaesquerda=0
    bordadireita=dimensaojanela[0]
    bordasuperior=0
    bordaeinferior=dimensaojanela[1]
    if figura['objeto'].top <bordasuperior or figura['objeto'].bottom>bordaeinferior:
        figura['vel'][1]=-figura['vel'][1]
    if figura['objeto'].left <bordaesquerda or figura['objeto'].right>bordadireita:
        figura['vel'][0]=-figura['vel'][0]
    figura['objeto'].x += figura['vel'][0]
    figura['objeto'].y += figura['vel'][1]

pygame.init()
janela=pygame.display.set_mode((LARGURAJANELA,ALTURAJANELA))
pygame.display.set_caption("animaçao")

f1={'objeto':pygame.Rect(300,80,40,80),"cor":VERMELHO,"vel":[0,-5],"forma":"ELIPSE"}
f2={'objeto':pygame.Rect(200,200,20,20),"cor":VERDE,"vel":[5,5],"forma":"ELIPSE"}
f3={'objeto':pygame.Rect(100,150,60,60),"cor":AZUL,"vel":[-5,5],"forma":"RETANGULO"}
f4={'objeto':pygame.Rect(200,150,80,40),"cor":PRETO,"vel":[5,0],"forma":"RETANGULO"}

fig=[f1,f2,f3,f4]





deve_continuar=True
while deve_continuar:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            deve_continuar=False
    janela.fill(BRANCO)
    for figura in fig:
        mover(figura,(LARGURAJANELA,ALTURAJANELA))
        if figura["forma"]=="RETANGULO":
            pygame.draw.rect(janela,figura["cor"],figura["objeto"])
        elif figura["forma"]=="ELIPSE":
            pygame.draw.ellipse(janela,figura["cor"],figura["objeto"])
    pygame.display.update()
    time.sleep(0.02)
pygame.quit()