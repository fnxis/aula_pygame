import pygame

PRETO=(0,0,0)
BRANCO=(255,255,255)
VERMELHO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
AMARELO=(255,255,0)

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
relogio=pygame.time.Clock()
janela=pygame.display.set_mode((LARGURAJANELA,ALTURAJANELA))
pygame.display.set_caption("colisão")

f1={'objeto':pygame.Rect(375,80,40,80),"cor":VERMELHO,"vel":[0,2],"forma":"ELIPSE"}
f2={'objeto':pygame.Rect(175,200,20,20),"cor":VERDE,"vel":[0,3],"forma":"ELIPSE"}
f3={'objeto':pygame.Rect(275,150,60,60),"cor":AZUL,"vel":[0,1],"forma":"RETANGULO"}
f4={'objeto':pygame.Rect(75,150,80,40),"cor":PRETO,"vel":[0,4],"forma":"RETANGULO"}

fig=[f1,f2,f3,f4]
bola={'objeto':pygame.Rect(270,330,30,30),"cor":AMARELO,"vel":[3,3],"forma":"BOLA"}





deve_continuar=True
while deve_continuar:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            deve_continuar=False
    janela.fill(BRANCO)
    for figura in fig:
        mover(figura,(LARGURAJANELA,ALTURAJANELA))
        pygame.draw.rect(janela,figura["cor"],figura["objeto"])
        mudaCor=bola["objeto"].colliderect(figura["objeto"])
        if mudaCor:
            bola["cor"]=figura["cor"]
    mover(bola,(LARGURAJANELA,ALTURAJANELA))
    pygame.draw.ellipse(janela,bola["cor"],bola["objeto"])
    pygame.display.update()
    relogio.tick(1000)
pygame.quit()