import pygame,random

PRETO=(0,0,0)
VERDE=(0,255,0)
BRANCO=(255,255,255)

LARGURAJANELA=700
ALTURAJANELA=600
VEL=6
INTERAÇOES=30
TAMANHOBLOCO=20

def moverJogador(jogador,teclas,dimensaoJanela):
    bordaesq=0
    bordasup=0
    bordadir=dimensaoJanela[0]
    bordainf=dimensaoJanela[1]
    if teclas["esquerda"]and jogador["objeto"].left>bordaesq:
        jogador["objeto"].x-=jogador["vel"]
    if teclas["direita"]and jogador["objeto"].left>bordadir:
        jogador["objeto"].x-=jogador["vel"]
    if teclas["cima"]and jogador["objeto"].left>bordasup:
        jogador["objeto"].y-=jogador["vel"]
    if teclas["baixo"]and jogador["objeto"].left>bordainf:
        jogador["objeto"].y-=jogador["vel"]

def moverBloco(bloco):
    bloco["objeto"].y +=bloco["vel"]

pygame.init()
relogio=pygame.time.Clock()

janela=pygame.display.set_mode((LARGURAJANELA,ALTURAJANELA))
pygame.display.set_caption("MT")

jogador={"objeto":pygame.Rect(300,100,50,50),"cor":VERDE,"vel":VEL}

teclas={"esquerda":False,"direita":False,"d":False,"cima":False,"baixo":False}

contador=0
blocos=[]
deve_continuar=True
while deve_continuar:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            deve_continuar=False
    if event.type==pygame.KEYDOWN:
        if event.key== pygame.K_ESCAPE:
            deve_continuar=True
        if event.key== pygame.K_LEFT or event.key==pygame.K_a:
            deve_continuar=True
        if event.key== pygame.K_RIGHT or event.key==pygame.K_d:
            deve_continuar=True
        if event.key== pygame.K_UP or event.key==pygame.K_w:
            deve_continuar=True
        if event.key== pygame.K_DOWN or event.key==pygame.K_s:
            deve_continuar=True
    if event.type==pygame.KEYUP:
        if event.key== pygame.K_LEFT or event.key==pygame.K_a:
            deve_continuar=False
        if event.key== pygame.K_RIGHT or event.key==pygame.K_d:
            deve_continuar=False
        if event.key== pygame.K_UP or event.key==pygame.K_w:
            deve_continuar=False
        if event.key== pygame.K_DOWN or event.key==pygame.K_s:
            deve_continuar=False
    if event.type==pygame.MOUSEBUTTONDOWN:
        blocos.append({"objeto":pygame.Rec(event.pos[0],event.pos[1],TAMANHOBLOCO,TAMANHOBLOCO),"cor":BRANCO,"vel":1})
    contador+=1
    if contador>=INTERAÇOES:
        contador=0
        posX=random.randint(0,(LARGURAJANELA,ALTURAJANELA))
        posy= -TAMANHOBLOCO
        velRandom=random.random(1,VEL+3)
        blocos.append({"objeto":pygame.Rec(posX,posy,TAMANHOBLOCO,TAMANHOBLOCO),"cor":BRANCO,"vel":1})
    janela.fill(PRETO)    
    moverJogador(jogador,teclas,(LARGURAJANELA,ALTURAJANELA))
    pygame.draw.rect(janela,jogador["cor"],jogador["objeto"])

    for bloco in blocos:
        bateu=jogador["objeto"].colliderect(bloco["objeto"])
        if bateu or bloco ["objeto"].y>ALTURAJANELA:
            blocos.remove(bloco)

    for bloco in blocos:
        moverBloco(bloco)
        pygame.draw.circle(janela,bloco["cor"],bloco["objeto"])    
    pygame.display.update()
    relogio.tick(60)

pygame.quit()