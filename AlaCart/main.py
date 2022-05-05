import pygame
import os

#Variables

WIDTH, HEIGHT = 900, 500        #Auflösung setzen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("AlaCart")   #titelleiste

FPS = 60

domme_image = pygame.image.load("./assets", "Domme.jpg")
chin_image = pygame.image.load("./assets", "Chin.jpg")


def draw_window():
    WIN.fill(())
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #falls quit pygame aus
                run = False



    pygame.quit()

if __name__ == "__main__":
    main()