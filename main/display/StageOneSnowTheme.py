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
    FPS = 300

    #define some colors
    BLACK =  (0,0,0,255)
    WHITE = (255,255,255,255)

    bg = pygame.image.load('drawable/bkgd_winter2.jpg').convert()
    bgWidth, bgHeight = bg.get_rect().size

    stageWidth = bgWidth*2
    stagePosX = 0

    startScrollingPosX = HW

    circleRadius = 25
    circlePosX = circleRadius

    playerPosX = circleRadius
    playerPosY = 485
    playerVelocityX = 0

    playerVelocityY = 50
    m = 5

    x = 0


    isjump = False


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

        else:
            playerVelocityX = -1

        if isjump:
            # 힘을 계산한다( F = 0.5 * m * v*v )
            if playerVelocityY > 0:
                F = (0.5 * m * playerVelocityY * playerVelocityY*0.002)
            else:
                F = -(0.5 * m * playerVelocityY * playerVelocityY*0.00006)

            # 포지션을 바꾼다.
            playerPosY = playerPosY - F
            print("Y 좌표 :",playerPosY-circleRadius)

            # 가속을 바꾼다.
            playerVelocityY = playerVelocityY - 1
            print("V : ",playerVelocityY)
            print("힘(F) : ",F)

            # 만약 바닥에 닿았을 경우, 가속을 리셋한다.
            if playerPosY >= 485:
                playerPosY = 485
                isjump = False
                playerVelocityY = 50

            #여기에 time.sleep(0.0159) 넣으면 주인공 빼고 느려짐 모두

        #player의 x좌표 바꿈.
        playerPosX += playerVelocityX
        if playerPosX > stageWidth-circleRadius:playerPosX=stageWidth-circleRadius
        if playerPosX < circleRadius:playerPosX=circleRadius
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

        pygame.draw.circle(DS, WHITE, (playerPosX,int(playerPosY-circleRadius)),circleRadius,0)

        pygame.display.update()
        CLOCK.tick(FPS)
        DS.fill(BLACK)
