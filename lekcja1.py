import pygame

def main():
    pygame.init()
    OknoGry=pygame.display.set_mode((440,440),0,32)
    pygame.display.set_caption("3tieg")
    run=True
    zmienna=100
    while(run):
        OknoGry.fill((0,0,0))
        pygame.time.delay(100)
        for zdarzenie in pygame.event.get():
            if zdarzenie.type==pygame.QUIT:
                run=False
        r=pygame.Rect((220,zmienna),(20,20))
        pygame.draw.rect(OknoGry,(255,0,0),r)
        zmienna=zmienna +20
        if zmienna>440:
            zmienna=0
        pygame.display.update()

main()