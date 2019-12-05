import pygame
from pygame.locals import *
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN =(77, 51, 25)
EGGS = (255, 217, 179)

IMG1_SIZE = 80
IMG2_SIZE = 20
IMG3_SIZE = 70
SCREEN = (800, 400)
MAX_X = 800
MAX_Y = 400
speed = 50
#eggs coordinates
#1
q = 77
#2
z = 299
#3
r = 495
#basket`s coordinates
x=499
y=320
#Ініціалізація екрану
pygame.init()
sc = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("CATCH THE EGGS")
#Background
background_image = pygame.image.load("/Users/marta/Desktop/Game/images/clouds.jpg")
sc.blit(background_image, [0, 0])

#Basket
basket = pygame.image.load("/Users/marta/Desktop/Game/images/basket.png")
basket = pygame.transform.scale(basket,(IMG1_SIZE,IMG1_SIZE))

volf = pygame.image.load('/Users/marta/Desktop/Game/images/volf.png')
volf = pygame.transform.scale(volf,(170,200))
#Hens
hen1 = pygame.image.load("/Users/marta/Desktop/Game/images/hen1.jpeg")
hen1 = pygame.transform.scale(hen1,(IMG3_SIZE,IMG3_SIZE))

hen2 = pygame.image.load("/Users/marta/Desktop/Game/images/hen1.jpeg")
hen2 = pygame.transform.scale(hen2,(IMG3_SIZE,IMG3_SIZE))

hen3 = pygame.image.load("/Users/marta/Desktop/Game/images/hen1.jpeg")
hen3 = pygame.transform.scale(hen3,(IMG3_SIZE,IMG3_SIZE))
#egg
egg=pygame.image.load("/Users/marta/Desktop/Game/images/egg.png").convert()
egg=pygame.transform.scale(egg,(IMG2_SIZE, IMG2_SIZE))

egg_list = []
for i in range(1):
    q1 = random.randrange(0, 400)
    egg_list.append([q, q1])
eggs_list2 = []
for i in range(2):
    z1 = random.randrange(0, 400)
    eggs_list2.append([z, z1])
eggs_list3 = []
for i in range(2):
    r1 = random.randrange(0, 400)
    eggs_list3.append([r, r1])


#Головний_цикл_гри
# pause = 0
score = 0
run = True
while run:
    pygame.time.delay(110)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    # badtimer -= 1
    # point = pygame.sprite.collide_mask(player, ring)
    # if point:
    #     score = score + 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500  - speed:
        x += speed

    background_image = pygame.image.load("/Users/marta/Desktop/Game/images/clouds.jpg")
    sc.blit(background_image, [0, 0])

    for i in range(len(egg_list)):
        # Draw the snow flake
        egg = pygame.draw.circle(sc, EGGS, egg_list[i], 8)
        # Move the snow flake down one pixel
        egg_list[i][1] += 3
        # If the snow flake has moved off the bottom of the screen
        if egg_list[i][1] > 400:
            # Reset it just above the top
            q1 = random.randrange(-50, -10)
            egg_list[i][1] = q1
        if q1 > y :
            run = False
            pygame.quit()
            
    for i in range(len(eggs_list2)):
        # pygame.draw.ellipse(sc, EGGS, eggs_list2[i], (0,0,45,76), 8)
        egg = pygame.draw.circle(sc, EGGS, eggs_list2[i], 8,7)
        # sc.blit(egg,eggs_list2[i],[z,z1])
        eggs_list2[i][1] += 5
        if eggs_list2[i][1] > 400:
            z1 = random.randrange(-50, -10)
            eggs_list2[i][1] = z1
    
    for i in range(len(eggs_list3)):
        egg = pygame.draw.circle(sc, EGGS, eggs_list3[i], 8)
        # sc.blit(egg,[z,z1])
        eggs_list3[i][1] += 3
        if eggs_list2[i][1] > 400:
            r1 = random.randrange(-50, -10)
            eggs_list2[i][1] = r1
  
    # # Проверить, столкнулся ли с чем-нибудь блок игрока
    # blocks_hit_list = pygame.sprite.spritecollide(basket, egg, False)
    # if len(blocks_hit_list) > 0:
    #     score +=len(blocks_hit_list)
    #     print( score )
    
    pygame.draw.line(sc, BROWN, [0, 70], [600, 70], 5)
    
    sc.blit(basket,[x,y])
    sc.blit(hen1,[50,0])
    sc.blit(hen2,[270,0])
    sc.blit(hen3,[470,0])
    sc.blit(hen3,[470,0])
    sc.blit(volf,[620,200])
    
    pygame.display.flip()
    pygame.display.update()
    # if pygame.sprite.collide_mask(egg, basket):
    #     egg.bounce()
    #Display scores:
    font = pygame.font.Font(None, 54)
    text = font.render('Score:', 5, WHITE)
    sc.blit(text, (610,10))

pygame.quit()