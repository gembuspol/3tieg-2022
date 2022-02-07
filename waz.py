import pygame

class Waz():
    #konstruktor klasy
    #tworzy podstawowe elementy klasy podczas wywołania jej
    def __init__(self):
        self.__pozycja=[(100,100)]
        self.dlugoscWeza=1
        self.punkty=0
    def getPosition(self):
        return self.__pozycja[0]
    def ruch(self,x,y):
         #sprawdzenie czy waz nie zjada siebie
        for location in self.__pozycja[::]:
            if x==location[0] and y==location[1]:
                    self.__pozycja=[(x,y)]
                    self.dlugoscWeza=1
                    self.punkty=0
        #dodanie nowej pozycji weza
        self.__pozycja.append((x,y))
    #funkcja rysująca węża
    #jako parametry wywołania używa self - samej siebie oraz OknoGry- tam gdzie będziemy rysować węża
    def rysowanie(self, OknoGry):
        #rysowanie węża z pozycji
        for poz in self.__pozycja[::-1]:
            r=pygame.Rect((poz[0],poz[1]),(20,20))
            pygame.draw.rect(OknoGry,(255,0,0),r)