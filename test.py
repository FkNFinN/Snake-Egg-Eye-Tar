import map
import pygame

#########################################################################################

pygame.init

bSH = pygame.image.load("BsnakeHead.png")
gem1 = pygame.image.load("gem1.png")
gem2 = pygame.image.load("gem2.png")
map11 = pygame.image.load("map11.png")
map12 = pygame.image.load("map12.png")

size_x = 600
size_y = 450
screen = pygame.display.set_mode((size_x, size_y))

#########################################################################################

pygame.mixer.init()
music = pygame.mixer.music.load("Sound.mp3") 
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  

gemMp = pygame.mixer.Sound("Gem.mp3")

#########################################################################################

level = 1

shine = True
on = True

dirB = 4
posB = [17,10]
oldposB = [[17,11],[17,12],[17,13]]
bSnake = pygame.Rect(posB[0]*30,posB[1]*30,30,30)

dirR = 4
posR = [2,10]
oldposR = [[2,11],[2,12],[2,13]]
rSnake = pygame.Rect(posR[0]*30,posR[1]*30,30,30)

screen.blit(map12, (0, 0))
screen.blit(gem2, (90,90))

run = True
while run:
    #key
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        if dirB != 1:
            dirB = 3
    elif key[pygame.K_RIGHT] == True:
        if dirB != 3:
            dirB = 1
    elif key[pygame.K_UP] == True:
        if dirB != 2:
            dirB = 4
    elif key[pygame.K_DOWN] == True:
        if dirB != 4:
            dirB = 2
    #Redsnake
    if key[pygame.K_a] == True:
        if dirR != 1:
            dirR = 3
    elif key[pygame.K_d] == True:
        if dirR != 3:
            dirR = 1
    elif key[pygame.K_w] == True:
        if dirR != 2:
            dirR = 4
    elif key[pygame.K_s] == True:
        if dirR != 4:
            dirR = 2

    oldposB[2][0] = oldposB[1][0]
    oldposB[2][1] = oldposB[1][1]
    oldposB[1][0] = oldposB[0][0]
    oldposB[1][1] = oldposB[0][1]
    oldposB[0][0] = posB[0]
    oldposB[0][1] = posB[1]

    oldposR[2][0] = oldposR[1][0]
    oldposR[2][1] = oldposR[1][1]
    oldposR[1][0] = oldposR[0][0]
    oldposR[1][1] = oldposR[0][1]
    oldposR[0][0] = posR[0]
    oldposR[0][1] = posR[1]

    #move
    if dirB == 1:
        bSnake.move_ip(30,0)
        posB[0] += 1
    elif dirB == 2:
        bSnake.move_ip(0,30)
        posB[1] += 1
    elif dirB == 3:
        bSnake.move_ip(-30,0)
        posB[0] -= 1
    elif dirB == 4:
        bSnake.move_ip(0,-30)
        posB[1] -= 1

    if dirR == 1:
        rSnake.move_ip(30,0)
        posR[0] += 1
    elif dirR == 2:
        rSnake.move_ip(0,30)
        posR[1] += 1
    elif dirR == 3:
        rSnake.move_ip(-30,0)
        posR[0] -= 1
    elif dirR == 4:
        rSnake.move_ip(0,-30)
        posR[1] -= 1

    #Check collision
    if map.M1[posB[1]][posB[0]] == 'A' or map.M1[posR[1]][posR[0]] == 'A' or (posB[0] == posR[0] and posB[1] == posR[1]) or (posB[0] == oldposR[0][0] and posB[1] == oldposR[0][1]) or (posB[0] == oldposR[1][0] and posB[1] == oldposR[1][1]) or (posB[0] == oldposR[2][0] and posB[1] == oldposR[2][1]) or (posR[0] == posB[0] and posR[1] == posB[1]) or (posR[0] == oldposB[0][0] and posR[1] == oldposB[0][1]) or (posR[0] == oldposB[1][0] and posR[1] == oldposB[1][1]) or (posR[0] == oldposB[2][0] and posR[1] == oldposB[2][1]):
        dirB = 4
        posB = [17,10]
        oldposB = [[17,11],[17,12],[17,13]]
        bSnake = pygame.Rect(posB[0]*30,posB[1]*30,30,30)

        dirR = 4
        posR = [2,10]
        oldposR = [[2,11],[2,12],[2,13]]
        rSnake = pygame.Rect(posR[0]*30,posR[1]*30,30,30)

    #generate snake
    screen.blit(bSH,bSnake)
    pygame.draw.rect(screen, (50,70,150), pygame.Rect(oldposB[0][0]*30,oldposB[0][1]*30, 30, 30))
    pygame.draw.rect(screen, (50,90,150), pygame.Rect(oldposB[1][0]*30,oldposB[1][1]*30, 30, 30))
    pygame.draw.rect(screen, (50,110,150), pygame.Rect(oldposB[2][0]*30,oldposB[2][1]*30, 30, 30))

    pygame.draw.rect(screen, (150,50,50), rSnake) #RGB
    pygame.draw.rect(screen, (150,70,50), pygame.Rect(oldposR[0][0]*30,oldposR[0][1]*30, 30, 30))
    pygame.draw.rect(screen, (150,90,50), pygame.Rect(oldposR[1][0]*30,oldposR[1][1]*30, 30, 30))
    pygame.draw.rect(screen, (150,110,50), pygame.Rect(oldposR[2][0]*30,oldposR[2][1]*30, 30, 30))
    
    #gem
    if map.M1[posB[1]][posB[0]] == 'G' or map.M1[posR[1]][posR[0]] == 'G':
        gemMp.play()
        level += 1;
        run = False
        pygame.time.delay(2000)
    
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            on = False

    pygame.display.update()

    if shine:
        screen.blit(map11, (0, 0))
        screen.blit(gem1, (90,90))
        shine = not shine
    else:
        screen.blit(map12, (0, 0))
        screen.blit(gem2, (90,90))
        shine = not shine

    pygame.time.delay(400)
pygame.quit()