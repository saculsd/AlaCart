import pygame
import os

#Variables

WIDTH, HEIGHT = 1920, 1080        #Auflösung setzen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("AlaCart")   #titelleiste

FPS = 4

#colors

white = 255, 255, 255

#Karten import

card_res_x = 200
card_res_y = 279
domme_image = pygame.image.load(os.path.join("Assets", "Domme.jpg"))
chin_image = pygame.image.load(os.path.join("Assets", "Chin.jpg"))

domme_card = pygame.transform.scale(domme_image, (card_res_x, card_res_y))
chin_card = pygame.transform.scale(chin_image, (card_res_x, card_res_y))

#checkt ob maus karte berührt

def check_touch(card):
    mx, my = pygame.mouse.get_pos()
    cardx_t = card.x + card_res_x
    cardy_t = card.y - card_res_y

    if mx >= card.x and mx <= cardx_t:
        if my <= card.y and my >= cardy_t:
            return("touch")

        else:
            return ("no touch")
    else:
        return ("no touch")


def draw_window(domme_pos, chin_pos):
    WIN.fill(white)
    WIN.blit(domme_card, (domme_pos.x, domme_pos.y))
    WIN.blit(chin_card, (chin_pos.x, chin_pos.y))
    pygame.display.update()


def main():

    domme_pos = pygame.Rect(0, 800, card_res_x, card_res_y)  # 0, 1080 [200, 800]
    chin_pos = pygame.Rect(600, 700, card_res_x, card_res_y)

    clock = pygame.time.Clock()
    run = True
    while run:

        mx, my = pygame.mouse.get_pos()
        loc = [mx, my]

        print(check_touch(domme_pos) + str(loc))

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #falls quit pygame aus
                run = False
        draw_window(domme_pos, chin_pos)

    pygame.quit()

if __name__ == "__main__":
    main()