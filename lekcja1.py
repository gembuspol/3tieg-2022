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
                    obiektWaz.setKierunek((-1,0))
                elif zdarzenie.key==pygame.K_RIGHT:
                    obiektWaz.setKierunek((1,0))
                elif zdarzenie.key==pygame.K_UP:
                    obiektWaz.setKierunek((0,-1))
                elif zdarzenie.key==pygame.K_DOWN:
                    obiektWaz.setKierunek((0,1))
        #wykonanie ruchu za każdym razem wykonania pętli        
        obiektWaz.ruch()
        obiektWaz.rysowanie(OknoGry)
        
        #tworzenie jablka za pomoca kola
        #pygame.draw.circle(OknoGry,(128,0,0),(appleX,appleY),10)
        
        #sprawdzenie czy waz zjada jablko
        poz=obiektWaz.getPosition()
        for obiektApple in obiektJablko[::]:
            pozJablko=obiektApple.getPozycja()
            if (poz[1]+10==pozJablko[1] and poz[0]+10==pozJablko[0]):
                obiektWaz.zjadanie()
            #wylosowanie nowej pozycji jablka
                obiektApple.losujPozycje()
            #appleX=random.randint(0,21)*20+10
            #appleY=random.randint(0,21)*20+10
            #pygame.draw.circle(OknoGry,(128,128,128),(appleX,appleY),10)
            
        #wypisanie punktow na ekran
        czcionka=pygame.font.SysFont('comicsans',30)
        tekst=czcionka.render("Zdobyłes punkty: {0}".format(obiektWaz.punkty),1,(0,255,0))
        OknoGry.blit(tekst, (10,10))
        
        #pobieranie pozycji głowy
        glowa=obiektWaz.getPosition()
        #sprawdzanie przejścia przez krawędź okna
        #prawa częśc okna
        if glowa[0]>420:
            obiektWaz.setPosition(0,glowa[1])
        #lewa część okna
        if glowa[0]<0:
            obiektWaz.setPosition(420,glowa[1])
        #dół ekranu
        if glowa[1]>420:
            obiektWaz.setPosition(glowa[0],0)
        #góra ekranu
        if glowa[1]<0:
            obiektWaz.setPosition(glowa[0],420)
          
        pygame.display.update()

main()