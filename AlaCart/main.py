import pygame
import os

#Variables

WIDTH, HEIGHT = 1920, 1080        #Auflösung setzen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("AlaCart")   #titelleiste

FPS = 60

#colors

white = 255, 255, 255

#Karten import

card_res_x = 200
card_res_y = 279
domme_image = pygame.image.load(os.path.join("Assets", "Domme.jpg"))
chin_image = pygame.image.load(os.path.join("Assets", "Chin.jpg"))
bean_image = pygame.image.load(os.path.join("Assets", "bean.jpg"))
karsten_image = pygame.image.load(os.path.join("Assets", "karsten.jpg"))
peter_image = pygame.image.load(os.path.join("Assets", "peter.jpg"))
sponge_image = pygame.image.load(os.path.join("Assets", "sponge.jpg"))
trump_image = pygame.image.load(os.path.join("Assets", "trump.jpg"))
wow_image = pygame.image.load(os.path.join("Assets", "wow.jpg"))


domme_card = pygame.transform.scale(domme_image, (card_res_x, card_res_y))
chin_card = pygame.transform.scale(chin_image, (card_res_x, card_res_y))
karsten_card = pygame.transform.scale(karsten_image, (card_res_x, card_res_y))
peter_card = pygame.transform.scale(peter_image, (card_res_x, card_res_y))
sponge_card = pygame.transform.scale(sponge_image, (card_res_x, card_res_y))
trump_card = pygame.transform.scale(trump_image, (card_res_x, card_res_y))
wow_card = pygame.transform.scale(wow_image, (card_res_x, card_res_y))
bean_card = pygame.transform.scale(bean_image, (card_res_x, card_res_y))



#checkt ob maus karte berührt

def check_touch(card, res_x, res_y):
    mx, my = pygame.mouse.get_pos()
    cardx_t = card.x + res_x
    cardy_t = card.y + res_y

    if mx >= card.x and mx <= cardx_t:
        if my >= card.y and my <= cardy_t:
            return(True)

        else:
            return (False)
    else:
        return (False)


def draw_window():
    WIN.fill(white)
    pygame.display.update()


def main():

    #domme_pos = pygame.Rect(400, 300, card_res_x, card_res_y) example for Rect

    clock = pygame.time.Clock()
    run = True
    while run:

        mx, my = pygame.mouse.get_pos()
        loc = [mx, my]



        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #falls quit pygame aus
                run = False 
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()