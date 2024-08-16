import pygame

pygame.init()

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))

player = pygame.image.load('./img/turtle.png')
player = pygame.transform.scale(player, (100, 100))
bag = pygame.image.load('./img/TrashBag.png')
bag = pygame.transform.scale(bag, (120, 120))
background = pygame.image.load('./img/water.jpg')
background = pygame.transform.scale(background, (800, 800))

run = True
x = 100 
y = 100
z = 120
t = 120


player_width = 100
player_height = 100

while run:
    screen.blit(background, (0, 0))

    screen.blit(player, (x, y))

    screen.blit(bag, (z, t))

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] == True:
        x -= 1
    elif key[pygame.K_RIGHT] == True:
        x+=1
    elif key[pygame.K_DOWN] == True:
        y += 1
    elif key[pygame.K_UP] == True:
        y -= 1

    if x < 0:
        x = 0
    if x > screenWidth - player_width:
        x = screenWidth - player_width
    if y < 0:
        y = 0
    if y > screenHeight - player_height:
        y = screenHeight - player_height

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()