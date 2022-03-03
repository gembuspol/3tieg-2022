import random
import pygame

class Jablko():
    #konstruktor klasy
    def __init__(self):
        self.pozycjaJablka=[(1,1)]
        self.losujPozycje()
    def setPozycja(self,x,y):
        self.pozycjaJablka[0]=(x,y)
    def getPozycja(self):
        return self.pozycjaJablka[-1]
    def losujPozycje(self):
        #losowanie pozycji jabłka
        appleX=random.randint(0,21)*20+10
        appleY=random.randint(0,21)*20+10
        self.setPozycja(appleX,appleY)
    def rysujJablko(self,oknoGry):
        pygame.draw.circle(oknoGry,(128,0,0),(self.pozycjaJablka[0][0],self.pozycjaJablka[0][1]),10)