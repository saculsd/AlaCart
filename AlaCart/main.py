import pygame
import os
from network import Network


#Variables

WIDTH, HEIGHT = 1920, 1080        #Auflösung setzen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("AlaCart")   #titelleiste

FPS = 60

last_color = 0, 0, 0
#colors

white = 255, 255, 255
white_ovwr = 254, 255, 255
black = 0, 0, 0

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

    last_color = None

def draw_window(color):
    global last_color
    if last_color != color:
        WIN.fill(color)

    last_color = color
    pygame.display.update()


def draw_text(text, positionx, postitiony, größe):
    pygame.init()
    myfont = pygame.font.SysFont("Comic Sans MS", größe)
    textsurface = myfont.render(text, False, black)
    WIN.blit(textsurface, (positionx, postitiony))
    pygame.display.update()






def main():

    #domme_pos = pygame.Rect(400, 300, card_res_x, card_res_y) example for Rect

    draw_window(white)


    clock = pygame.time.Clock()
    run = True

    n = Network()
    players = n.players
    print(players)
    rply = "wait-ok"

    if players == 1:
        i_player = 1
    else:
        i_player = 2

    while run:

# maus pos grab für checkTouch()

        mx, my = pygame.mouse.get_pos()
        loc = [mx, my]
#networking und überprüfen ob 2 spieler verbunden sind



        if int(players) >= 3:
            pygame.quit()

        if players == 2 or rply == "ready-ok":
            #print("Alle da, du bist Spieler: " + str(i_player))
            draw_window(white_ovwr)
            draw_text("Alle Spieler verbunden", 450, 100, 80)
            rply = n.send("ready")


        elif rply == "wait-ok":
            #print ("Warte, du bist Spieler: " + str(i_player))
            draw_window(white)
            draw_text("Warte auf Spieler 2...", 450, 100, 80)
            rply = n.send("wait")





        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #falls quit pygame aus
                run = False 

    pygame.quit()

if __name__ == "__main__":
    main()