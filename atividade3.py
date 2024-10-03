import pygame

pygame.init()
PI=3.1416
VERDE=(0,255,0)
BRANCO=(255,255,255)
VERMELHO=(255,0,0)
janela=pygame.display.set_mode((800,800))

pygame.display.set_caption("Free Fire 2")
janela.fill(BRANCO)
deve_continuar=True
font_path="BarlowCondensed-Italic.ttf"
fonte=pygame.font.Font(font_path,48)
texto=fonte.render("ola mundo ",True,VERMELHO,BRANCO)
janela.blit(texto,[300,350])
pygame.draw.circle(janela,VERDE,[300,251],100)
pygame.draw.line(janela,BRANCO,[220,250],[380,250],100)
pygame.draw.circle(janela,VERDE,[300,251],50,10)
pygame.draw.polygon(janela,VERMELHO,([400,200],[420,280],[380, 280]),0)
pygame.draw.polygon(janela,VERMELHO,([480,280],[420,280],[430, 320]),0)
pygame.draw.polygon(janela,VERMELHO,([430,320],[480,400],[400, 340]),0)
pygame.draw.polygon(janela,VERMELHO,([400,340],[330,400],[360, 330]),0)
pygame.draw.polygon(janela,VERMELHO,([360,330],[480,400],[400, 200]),0)
pygame.draw.polygon(janela,VERMELHO,([360,330],[290,320],[400, 280]),0)
pygame.draw.rect(janela,VERMELHO,(20,20,60,40),0)
pygame.draw.arc(janela,VERMELHO,(250,75,150,125),PI/2,3*PI,2)
pygame.draw.arc(janela,VERDE,(250,75,150,125),-PI/2*PI/2,2)


pygame.draw.ellipse(janela,VERMELHO,(400,250,40,80),1)



pygame.display.update()

while deve_continuar:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            deve_continuar=False
pygame.quit()
