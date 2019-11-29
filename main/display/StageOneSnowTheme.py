import pygame
from pygame.locals import *
import sys
import os
import time

class StageOneSnowTheme:
    def events():
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    W,H = 900, 646
    HW, HH = W/2, H/2
    AREA = W+H

    os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

    pygame.init()
    os.chdir(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
    CLOCK = pygame.time.Clock()
    DS = pygame.display.set_mode((W,H))
    pygame.display.set_caption("BackgroundScrolling with Player")
    FPS = 500

    #define some colors
    BLACK =  (0,0,0,255)
    WHITE = (255,255,255,255)
    GREEN = (0,255,0,255)

    bg = pygame.image.load('drawable/bkgd_winter2.jpg').convert()
    bgWidth, bgHeight = bg.get_rect().size

    stageWidth = bgWidth*2
    stagePosX = 0

    startScrollingPosX = HW

    circleRadius = 25
    circlePosX = circleRadius

    playerPosX = circleRadius +50
    playerPosY = 485
    playerVelocityX = 0

    playerVelocityY = 100
    playerVelocityDouble = 200
    m = 5

    x = 0


    isjump = False
    doublejump = False
    doubleCheck = False


    while True:
        events()

        k=pygame.key.get_pressed()
        if k[K_RIGHT] or k[K_LEFT] or k[K_UP]:
            if k[K_RIGHT]:
                playerVelocityX = 2
            if k[K_LEFT]:
                playerVelocityX = -2
            if k[K_UP]:
                isjump = True
                print("click")
            if k[K_SPACE]:
                if isjump == True:
                    if playerVelocityY<0:
                        doublejump = True

        else:
            playerVelocityX = -1

        if not doublejump :
            if isjump:
                # 힘을 계산한다( F = 0.5 * m * v*v )
                if playerVelocityY > 0:
                    F = (0.5 * m * playerVelocityY * playerVelocityY*0.0002)
                else:
                    F = -(0.5 * m * playerVelocityY * playerVelocityY*0.00004)

                # 포지션을 바꾼다.
                playerPosY = playerPosY - F

                # 가속을 바꾼다.
                playerVelocityY = playerVelocityY - 1

                # 만약 바닥에 닿았을 경우, 가속을 리셋한다.
                if playerPosY >= 485:
                    playerPosY = 485
                    isjump = False
                    playerVelocityY = 100

                #여기에 time.sleep(0.0159) 넣으면 주인공 빼고 느려짐 모두

        elif doublejump:
            # 힘을 계산한다( F = 0.5 * m * v*v )
            if playerVelocityDouble > 0:
                F = (0.5 * m * playerVelocityDouble* playerVelocityDouble*0.000033)
            else:
                F = -(0.5 * m * playerVelocityDouble * playerVelocityDouble*0.0005)

            # 포지션을 바꾼다.
            playerPosY = playerPosY - F

            # 가속을 바꾼다.
            playerVelocityDouble = playerVelocityDouble- 1

            # 만약 바닥에 닿았을 경우, 가속을 리셋한다.
            if playerPosY >= 485:
                playerPosY = 485
                isjump = False
                playerVelocityY = 100
                playerVelocityDouble = 200
                doublejump = False

            #여기에 time.sleep(0.0159) 넣으면 주인공 빼고 느려짐 모두

        #player의 x좌표 바꿈.
        playerPosX += playerVelocityX

        if playerPosX > stageWidth-circleRadius:playerPosX=stageWidth-circleRadius
        if playerPosX < circleRadius+25:playerPosX=circleRadius+25
        if playerPosX >= 800-circleRadius:playerPosX=800-circleRadius
        if playerPosX < startScrollingPosX:circlePosX=playerPosX
        elif playerPosX>stagePosX-startScrollingPosX:circlePosX=playerPosX-stagePosX+W
        else:
            circlePosX=startScrollingPosX
            stagePosX += -playerVelocityX
        stagePosX -= 0.8


        rel_x = stagePosX%bgWidth
        DS.blit(bg,(rel_x-bgWidth,0))
        if rel_x<W:
            DS.blit(bg,(rel_x,0))

        if not doublejump :
            pygame.draw.circle(DS, WHITE, (playerPosX,int(playerPosY-circleRadius)),circleRadius,0)
        elif doublejump :
            pygame.draw.circle(DS, GREEN, (playerPosX, int(playerPosY - circleRadius)), circleRadius, 0)

        pygame.display.update()
        CLOCK.tick(FPS)
        DS.fill(BLACK)
