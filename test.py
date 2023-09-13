if oldposR[0][0] < oldposR[1][0] and oldposR[1][0] < oldposR[2][0]:#LR
                screen.blit(bSSL,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][0] > oldposR[1][0] and oldposR[1][0] > oldposR[2][0]:#RL
                screen.blit(bSSR,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] < oldposR[1][1] and oldposR[1][1] < oldposR[2][1]:#UD
                screen.blit(bSSU,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] > oldposR[1][1] and oldposR[1][1] > oldposR[2][1]:#DU
                screen.blit(bSSD,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][0] < oldposR[1][0] and oldposR[1][1] < oldposR[2][1]:#LD
                screen.blit(bSsLD,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][0] < oldposR[1][0] and oldposR[1][1] > oldposR[2][1]:#LU
                screen.blit(bSbLU,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][0] > oldposR[1][0] and oldposR[1][1] < oldposR[2][1]:#RD
                screen.blit(bSbRD,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][0] > oldposR[1][0] and oldposR[1][1] > oldposR[2][1]:#RU
                screen.blit(bSsRU,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] < oldposR[1][1] and oldposR[1][0] < oldposR[2][0]:#UR
                screen.blit(bSbRU,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] < oldposR[1][1] and oldposR[1][0] > oldposR[2][0]:#UL
                screen.blit(bSsLU,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] > oldposR[1][1] and oldposR[1][0] < oldposR[2][0]:#DR
                screen.blit(bSsRD,(oldposR[1][0]*30,oldposR[1][1]*30))
            elif oldposR[0][1] > oldposR[1][1] and oldposR[1][0] > oldposR[2][0]:#DL
                screen.blit(bSbLD,(oldposR[1][0]*30,oldposR[1][1]*30))