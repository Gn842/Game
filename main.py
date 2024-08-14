import pygame

pygame.init()

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))

player = pygame.image.load('./img/turtle.png')
player = pygame.transform.scale(player, (100, 100))
background = pygame.image.load('./img/water.jpg')
background = pygame.transform.scale(background, (800, 800))

run = True
x= 100 
y = 100
while run:
    screen.blit(background, (0, 0))

    screen.blit(player, (x, y))

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] == True:
        x -= 1
    elif key[pygame.K_RIGHT] == True:
        x+=1
    elif key[pygame.K_DOWN] == True:
        y += 1
    elif key[pygame.K_UP] == True:
        y -= 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()