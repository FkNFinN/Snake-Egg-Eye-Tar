import map
import pygame

#########################################################################################

pygame.init

bSH = pygame.image.load("BsnakeHead.png")
bSHD = pygame.transform.rotate(bSH, 180)
bSHR = pygame.transform.rotate(bSH, 270)
bSHL = pygame.transform.rotate(bSH, 90)

bSSU = pygame.image.load("bSST.png")
bSSD = pygame.transform.rotate(bSSU, 180)
bSSL = pygame.transform.rotate(bSSU, 90)
bSSR = pygame.transform.rotate(bSSU, 270)

bSbLU = pygame.image.load("bSLU.png")
bSbRD = pygame.transform.rotate(bSbLU, 180)
bSbLD = pygame.transform.rotate(bSbLU, 90)
bSbRU = pygame.transform.rotate(bSbLU, 270)

bSsLD = pygame.image.load("bSLD.png")
bSsRD = pygame.transform.rotate(bSsLD, 90)
bSsLU = pygame.transform.rotate(bSsLD, 270)
bSsRU = pygame.transform.rotate(bSsLD, 180)

bST = pygame.image.load("BsnakeTail.png")
bSTD = pygame.transform.rotate(bST, 180)
bSTR = pygame.transform.rotate(bST, 270)
bSTL = pygame.transform.rotate(bST, 90)

#Red
rSH = pygame.image.load("RedSnakeHead.png")
rSHD = pygame.transform.rotate(rSH, 180)
rSHR = pygame.transform.rotate(rSH, 270)
rSHL = pygame.transform.rotate(rSH, 90)

rSSU = pygame.image.load("rSST.png")
rSSD = pygame.transform.rotate(rSSU, 180)
rSSL = pygame.transform.rotate(rSSU, 90)
rSSR = pygame.transform.rotate(rSSU, 270)

rSbLU = pygame.image.load("rSLU.png")
rSbRD = pygame.transform.rotate(rSbLU, 180)
rSbLD = pygame.transform.rotate(rSbLU, 90)
rSbRU = pygame.transform.rotate(rSbLU, 270)

rSsLD = pygame.image.load("rSLD.png")
rSsRD = pygame.transform.rotate(rSsLD, 90)
rSsLU = pygame.transform.rotate(rSsLD, 270)
rSsRU = pygame.transform.rotate(rSsLD, 180)

rST = pygame.image.load("RsnakeTail.png")
rSTD = pygame.transform.rotate(rST, 180)
rSTR = pygame.transform.rotate(rST, 270)
rSTL = pygame.transform.rotate(rST, 90)

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

while on:
    if level == 1:#################################################################################################

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
            #B head
            if dirB == 1:
                screen.blit(bSHR,bSnake)
            elif dirB == 2:
                screen.blit(bSHD,bSnake)
            elif dirB == 3:
                screen.blit(bSHL,bSnake)
            elif dirB == 4:
                screen.blit(bSH,bSnake)
            
            #B body 1
            if posB[0] < oldposB[0][0] and oldposB[0][0] < oldposB[1][0]:#LR
                screen.blit(bSSL,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[0] > oldposB[0][0] and oldposB[0][0] > oldposB[1][0]:#RL
                screen.blit(bSSR,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[1] < oldposB[0][1] and oldposB[0][1] < oldposB[1][1]:#UD
                screen.blit(bSSU,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[1] > oldposB[0][1] and oldposB[0][1] > oldposB[1][1]:#DU
                screen.blit(bSSD,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[0] < oldposB[0][0] and oldposB[0][1] < oldposB[1][1]:#LD
                screen.blit(bSsLD,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[0] < oldposB[0][0] and oldposB[0][1] > oldposB[1][1]:#LU
                screen.blit(bSbLU,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[0] > oldposB[0][0] and oldposB[0][1] < oldposB[1][1]:#RD
                screen.blit(bSbRD,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[0] > oldposB[0][0] and oldposB[0][1] > oldposB[1][1]:#RU
                screen.blit(bSsRU,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[1] < oldposB[0][1] and oldposB[0][0] < oldposB[1][0]:#UR
                screen.blit(bSbRU,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[1] < oldposB[0][1] and oldposB[0][0] > oldposB[1][0]:#UL
                screen.blit(bSsLU,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[1] > oldposB[0][1] and oldposB[0][0] < oldposB[1][0]:#DR
                screen.blit(bSsRD,(oldposB[0][0]*30,oldposB[0][1]*30))
            elif posB[1] > oldposB[0][1] and oldposB[0][0] > oldposB[1][0]:#DL
                screen.blit(bSbLD,(oldposB[0][0]*30,oldposB[0][1]*30))

            #B body 2
            if oldposB[0][0] < oldposB[1][0] and oldposB[1][0] < oldposB[2][0]:#LR
                screen.blit(bSSL,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][0] > oldposB[1][0] and oldposB[1][0] > oldposB[2][0]:#RL
                screen.blit(bSSR,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][1] < oldposB[1][1] and oldposB[1][1] < oldposB[2][1]:#UD
                screen.blit(bSSU,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][1] > oldposB[1][1] and oldposB[1][1] > oldposB[2][1]:#DU
                screen.blit(bSSD,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][0] < oldposB[1][0] and oldposB[1][1] < oldposB[2][1]:#LD
                screen.blit(bSsLD,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][0] < oldposB[1][0] and oldposB[1][1] > oldposB[2][1]:#LU
                screen.blit(bSbLU,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][0] > oldposB[1][0] and oldposB[1][1] < oldposB[2][1]:#RD
                screen.blit(bSbRD,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][0] > oldposB[1][0] and oldposB[1][1] > oldposB[2][1]:#RU
                screen.blit(bSsRU,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][1] < oldposB[1][1] and oldposB[1][0] < oldposB[2][0]:#UR
                screen.blit(bSbRU,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][1] < oldposB[1][1] and oldposB[1][0] > oldposB[2][0]:#UL
                screen.blit(bSsLU,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][1] > oldposB[1][1] and oldposB[1][0] < oldposB[2][0]:#DR
                screen.blit(bSsRD,(oldposB[1][0]*30,oldposB[1][1]*30))
            elif oldposB[0][1] > oldposB[1][1] and oldposB[1][0] > oldposB[2][0]:#DL
                screen.blit(bSbLD,(oldposB[1][0]*30,oldposB[1][1]*30))

            #B tail
            if oldposB[1][0] < oldposB[2][0]:
                screen.blit(bSTL,(oldposB[2][0]*30,oldposB[2][1]*30))
            elif oldposB[1][0] > oldposB[2][0]:
                screen.blit(bSTR,(oldposB[2][0]*30,oldposB[2][1]*30))
            elif oldposB[1][1] < oldposB[2][1]:
                screen.blit(bST,(oldposB[2][0]*30,oldposB[2][1]*30))
            elif oldposB[1][1] > oldposB[2][1]:
                screen.blit(bSTD,(oldposB[2][0]*30,oldposB[2][1]*30))
            
            #R head
            if dirR == 1:
                screen.blit(rSHR,rSnake)
            elif dirR == 2:
                screen.blit(rSHD,rSnake)
            elif dirR == 3:
                screen.blit(rSHL,rSnake)
            elif dirR == 4:
                screen.blit(rSH,rSnake)
            
            #R body 1
            if posR[0] < oldposR[0][0] and oldposR[0][0] < oldposR[1][0]:#LR
                screen.blit(rSSL,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[0] > oldposR[0][0] and oldposR[0][0] > oldposR[1][0]:#RL
                screen.blit(rSSR,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[1] < oldposR[0][1] and oldposR[0][1] < oldposR[1][1]:#UD
                screen.blit(rSSU,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[1] > oldposR[0][1] and oldposR[0][1] > oldposR[1][1]:#DU
                screen.blit(rSSD,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[0] < oldposR[0][0] and oldposR[0][1] < oldposR[1][1]:#LD
                screen.blit(rSsLD,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[0] < oldposR[0][0] and oldposR[0][1] > oldposR[1][1]:#LU
                screen.blit(rSbLU,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[0] > oldposR[0][0] and oldposR[0][1] < oldposR[1][1]:#RD
                screen.blit(rSbRD,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[0] > oldposR[0][0] and oldposR[0][1] > oldposR[1][1]:#RU
                screen.blit(rSsRU,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[1] < oldposR[0][1] and oldposR[0][0] < oldposR[1][0]:#UR
                screen.blit(rSbRU,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[1] < oldposR[0][1] and oldposR[0][0] > oldposR[1][0]:#UL
                screen.blit(rSsLU,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[1] > oldposR[0][1] and oldposR[0][0] < oldposR[1][0]:#DR
                screen.blit(rSsRD,(oldposR[0][0]*30,oldposR[0][1]*30))
            elif posR[1] > oldposR[0][1] and oldposR[0][0] > oldposR[1][0]:#DL
                screen.blit(rSbLD,(oldposR[0][0]*30,oldposR[0][1]*30))

            #R body 2
            if oldposR[0][0] < oldposR[1][0] and oldposR[1][0] < oldposR[2][0]:#LR
                screen.blit(rSSL,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][0] > oldposR[1][0] and oldposR[1][0] > oldposR[2][0]:#RL
                screen.blit(rSSR,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] < oldposR[1][1] and oldposR[1][1] < oldposR[2][1]:#UD
                screen.blit(rSSU,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] > oldposR[1][1] and oldposR[1][1] > oldposR[2][1]:#DU
                screen.blit(rSSD,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][0] < oldposR[1][0] and oldposR[1][1] < oldposR[2][1]:#LD
                screen.blit(rSsLD,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][0] < oldposR[1][0] and oldposR[1][1] > oldposR[2][1]:#LU
                screen.blit(rSbLU,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][0] > oldposR[1][0] and oldposR[1][1] < oldposR[2][1]:#RD
                screen.blit(rSbRD,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][0] > oldposR[1][0] and oldposR[1][1] > oldposR[2][1]:#RU
                screen.blit(rSsRU,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] < oldposR[1][1] and oldposR[1][0] < oldposR[2][0]:#UR
                screen.blit(rSbRU,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] < oldposR[1][1] and oldposR[1][0] > oldposR[2][0]:#UL
                screen.blit(rSsLU,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] > oldposR[1][1] and oldposR[1][0] < oldposR[2][0]:#DR
                screen.blit(rSsRD,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] > oldposR[1][1] and oldposR[1][0] > oldposR[2][0]:#DL
                screen.blit(rSbLD,(oldposR[1][0]*30,oldposR[1][1]*30))

            #R tail
            if oldposR[1][0] < oldposR[2][0]:
                screen.blit(rSTL,(oldposR[2][0]*30,oldposR[2][1]*30))
            elif oldposR[1][0] > oldposR[2][0]:
                screen.blit(rSTR,(oldposR[2][0]*30,oldposR[2][1]*30))
            elif oldposR[1][1] < oldposR[2][1]:
                screen.blit(rST,(oldposR[2][0]*30,oldposR[2][1]*30))
            elif oldposR[1][1] > oldposR[2][1]:
                screen.blit(rSTD,(oldposR[2][0]*30,oldposR[2][1]*30))

            #gem
            if map.M1[posB[1]][posB[0]] == 'G' or map.M1[posR[1]][posR[0]] == 'G':
                gemMp.play()
                level += 1;
                run = False
                pygame.display.update()
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

    elif level == 2:#################################################################################################
        on = False

pygame.quit()