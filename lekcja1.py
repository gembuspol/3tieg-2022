import pygame
import random

def main():
    pygame.init()
    OknoGry=pygame.display.set_mode((440,440),0,32)
    pygame.display.set_caption("3tieg")
    run=True
    zmienna=100
    zmienna2=100
    #losowanie pozycji jabłka
    appleX=random.randint(0,21)*20+10
    appleY=random.randint(0,21)*20+10
    
    while(run):
        OknoGry.fill((0,0,0))
        pygame.time.delay(100)
        for zdarzenie in pygame.event.get():
            if zdarzenie.type==pygame.QUIT:
                run=False
            elif zdarzenie.type==pygame.KEYDOWN:
                if zdarzenie.key==pygame.K_LEFT:
                    zmienna2=zmienna2-20
                elif zdarzenie.key==pygame.K_RIGHT:
                    zmienna2=zmienna2+20
                elif zdarzenie.key==pygame.K_UP:
                    zmienna=zmienna-20
                elif zdarzenie.key==pygame.K_DOWN:
                    zmienna=zmienna +20
        #tworzenie kwadratu jako weza
        r=pygame.Rect((zmienna2,zmienna),(20,20))
        pygame.draw.rect(OknoGry,(255,0,0),r)
        #tworzenie jablka za pomoca kola
        pygame.draw.circle(OknoGry,(128,0,0),(appleX,appleY),10)
        #sprawdzenie czy waz zjada jablko
        if (zmienna+10==appleY and zmienna2+10==appleX):
            pygame.draw.circle(OknoGry,(128,128,128),(appleX,appleY),10)
        #zmienna=zmienna +20
        if zmienna>420:
            zmienna=0
        #zmienna2=zmienna2 +20
        if zmienna2>420:
            zmienna2=0
        if zmienna2<0:
            zmienna2=420
        if zmienna<0:
            zmienna=420    
        pygame.display.update()

main()