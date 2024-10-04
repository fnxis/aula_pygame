import pygame,random

IMAGEMSONIC=pygame.image.load("img/R.png")
IMAGEMFUNDO=pygame.image.load("img/fundo.png")
IMAGEMMOEDA=pygame.image.load("img/moedas.png")

LARGURAMOEDA=80
ALTURAMOEDA=30
LARGURASONIC=240
ALTURASONIC=140
LARGURAJANELA=800
ALTURAJANELA=700
VEL=6
INTERACAO=30

IMAGEMFUNDO=pygame.transform.scale(IMAGEMFUNDO,(LARGURAJANELA,ALTURAJANELA))
IMAGEMMOEDA=pygame.transform.scale(IMAGEMMOEDA,(LARGURAMOEDA,ALTURAMOEDA))
IMAGEMSONIC=pygame.transform.scale(IMAGEMSONIC,(LARGURASONIC,ALTURASONIC))


def moverJogador(jogador,teclas,dimensaoJanela):
    bordaesq=0
    bordasup=0
    bordadir=dimensaoJanela[0]
    bordainf=dimensaoJanela[1]
    if teclas["esquerda"]and jogador["objeto"].left>bordaesq:
        jogador["objeto"].x-=jogador["vel"]
    if teclas["direita"]and jogador["objeto"].left<bordadir:
        jogador["objeto"].x+=jogador["vel"]
    if teclas["cima"]and jogador["objeto"].left>bordasup:
        jogador["objeto"].y-=jogador["vel"]
    if teclas["baixo"]and jogador["objeto"].left<bordainf:
        jogador["objeto"].y+=jogador["vel"]

def moverMoeda(moeda):
    moeda["objeto"].x -=moeda["vel"]

pygame.init()
relogio=pygame.time.Clock()

janela=pygame.display.set_mode((LARGURAJANELA,ALTURAJANELA))
pygame.display.set_caption("SONIC")

jogador={"objeto":pygame.Rect(300,100,LARGURASONIC,ALTURASONIC),"imagem":IMAGEMSONIC,"vel":VEL,"colisaoRect":pygame.Rect(300+50,100+50,LARGURASONIC-100,ALTURASONIC-100)}

teclas={"esquerda":False,"direita":False,"d":False,"cima":False,"baixo":False}
somComer=pygame.mixer.Sound('mp3/moedaSom.mp3')
pygame.mixer.music.load("mp3/musicafundo.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1,0.0)
somAtivado=True





contador=0
moedas=[]
deve_continuar=True
while deve_continuar:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            deve_continuar=False

    
    if event.type==pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            deve_continuar=False
        if event.key == pygame.K_m:
            if somAtivado:
                pygame.mixer.music.stop()
                somAtivado=False
            else:
                pygame.mixer.music.play(-1,0.0)
                somAtivado=True



    if event.type==pygame.MOUSEBUTTONDOWN:
        moedas.append({"objeto":pygame.Rect(event.pos[0],event.pos[1],LARGURAMOEDA,ALTURAMOEDA),"imagem":IMAGEMMOEDA,"vel":VEL-3})
    
    teclas=pygame.key.get_pressed()
    teclas={
        "esquerda":teclas[pygame.K_LEFT] or teclas[pygame.K_a],
        "direita":teclas[pygame.K_RIGHT] or teclas[pygame.K_d],
        "cima":teclas[pygame.K_UP] or teclas[pygame.K_w],
        "baixo":teclas[pygame.K_DOWN] or teclas[pygame.K_s]
    }

    contador+=1
    if contador>=INTERACAO:
        contador=0
        posX=random.randint(0,(ALTURAJANELA-ALTURAMOEDA))
        posy= -ALTURAMOEDA
        velRandom=random.randint(VEL-3,VEL+3)
        moedas.append({"objeto":pygame.Rect(posX,posy,LARGURAMOEDA,ALTURAMOEDA),"imagem":IMAGEMMOEDA,"vel":velRandom})

    janela.blit(IMAGEMFUNDO,(0,0))    

    moverJogador(jogador,teclas,(LARGURAJANELA,ALTURAJANELA))

    janela.blit(jogador["imagem"],jogador["objeto"])
    for moeda in moedas:
        bateu=jogador["colisaoRect"].colliderect(moeda["objeto"])
        if bateu and somAtivado:
            somComer.play()
        if bateu or moeda["objeto"].x>LARGURAJANELA:
            moedas.remove(moeda)
    jogador["colisaoRect"].topleft=(jogador['objeto'].x+100,jogador["objeto"].y+100)

    for moeda in moedas:
        moverMoeda(moeda)
        janela.blit(moeda["imagem"],moeda["objeto"])    

    pygame.display.update()
    relogio.tick(60)

pygame.quit()