import pygame
import random
import waz
import jablko

def main():
    pygame.init()
    OknoGry=pygame.display.set_mode((440,440),0,32)
    pygame.display.set_caption("3tieg")
    run=True
    iloscJablek=3
    #wywołanie klasy waz
    obiektWaz1=waz.Waz()
    obiektWaz2=waz.Waz()
    #tworzenie kilku jablek
    obiektJablko=[]
    for nrJablko in range(0,iloscJablek):
        obiektJablko.append(jablko.Jablko())
    
    #losowanie pozycji jabłka
    appleX=random.randint(0,21)*20+10
    appleY=random.randint(0,21)*20+10
    
    while(run):
        OknoGry.fill((0,0,0))
        
        for obiektApple in obiektJablko[::]:
            obiektApple.rysujJablko(OknoGry)
        #obiektJablko.rysujJablko(OknoGry)
        pygame.time.delay(200)
        #obsługa ruchu weża obiektu obiket waz
        for zdarzenie in pygame.event.get():
            if zdarzenie.type==pygame.QUIT:
                run=False
            elif zdarzenie.type==pygame.KEYDOWN:
                if zdarzenie.key==pygame.K_LEFT:
                    obiektWaz1.setKierunek((-1,0))
                elif zdarzenie.key==pygame.K_RIGHT:
                    obiektWaz1.setKierunek((1,0))
                elif zdarzenie.key==pygame.K_UP:
                    obiektWaz1.setKierunek((0,-1))
                elif zdarzenie.key==pygame.K_DOWN:
                    obiektWaz1.setKierunek((0,1))
                elif zdarzenie.key==pygame.K_a:
                    obiektWaz2.setKierunek((-1,0))
                elif zdarzenie.key==pygame.K_d:
                    obiektWaz2.setKierunek((1,0))
                elif zdarzenie.key==pygame.K_w:
                    obiektWaz2.setKierunek((0,-1))
                elif zdarzenie.key==pygame.K_s:
                    obiektWaz2.setKierunek((0,1))
        #wykonanie ruchu za każdym razem wykonania pętli        
        obiektWaz1.ruch()
        obiektWaz1.rysowanie(OknoGry)
        obiektWaz2.ruch()
        obiektWaz2.rysowanie(OknoGry)
        
        #tworzenie jablka za pomoca kola
        #pygame.draw.circle(OknoGry,(128,0,0),(appleX,appleY),10)
        
        #sprawdzenie czy waz zjada jablko
        poz1=obiektWaz1.getPosition()
        poz2=obiektWaz2.getPosition()
        for obiektApple in obiektJablko[::]:
            pozJablko=obiektApple.getPozycja()
            if (poz1[1]+10==pozJablko[1] and poz1[0]+10==pozJablko[0]):
                obiektWaz1.zjadanie()
            if (poz2[1]+10==pozJablko[1] and poz2[0]+10==pozJablko[0]):
                obiektWaz2.zjadanie()
            #wylosowanie nowej pozycji jablka
                obiektApple.losujPozycje()
            #appleX=random.randint(0,21)*20+10
            #appleY=random.randint(0,21)*20+10
            #pygame.draw.circle(OknoGry,(128,128,128),(appleX,appleY),10)
            
        #wypisanie punktow na ekran
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst=czcionka.render("Punkty gracz 1: {0}".format(obiektWaz1.punkty),1,(0,255,0))
        tekst2=czcionka.render("Punkty gracz 2: {0}".format(obiektWaz2.punkty),1,(0,255,0))
        OknoGry.blit(tekst, (10,10))
        OknoGry.blit(tekst2, (10,30))
        
        #pobieranie pozycji głowy
        glowa1=obiektWaz1.getPosition()
        glowa2=obiektWaz2.getPosition()
        #sprawdzanie przejścia przez krawędź okna
        #prawa częśc okna
        if glowa1[0]>420:
            obiektWaz1.setPosition(0,glowa1[1])
        #lewa część okna
        if glowa1[0]<0:
            obiektWaz1.setPosition(420,glowa1[1])
        #dół ekranu
        if glowa1[1]>420:
            obiektWaz1.setPosition(glowa1[0],0)
        #góra ekranu
        if glowa1[1]<0:
            obiektWaz1.setPosition(glowa1[0],420)
        
        if glowa2[0]>420:
            obiektWaz2.setPosition(0,glowa2[1])
        #lewa część okna
        if glowa2[0]<0:
            obiektWaz2.setPosition(420,glowa2[1])
        #dół ekranu
        if glowa2[1]>420:
            obiektWaz2.setPosition(glowa2[0],0)
        #góra ekranu
        if glowa2[1]<0:
            obiektWaz2.setPosition(glowa2[0],420)


        pygame.display.update()

main()