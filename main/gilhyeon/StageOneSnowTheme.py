import pygame
from pygame.locals import *
import sys
import os
from pygame import mixer

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
    PASTEL_BLUE = (217,241,255,200)
    PASTEL_RED = (255,114,114,255)
    PASTEL_GRAY = (80,78,82,255)
    GOLD = (189,150,25,255)

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

    playerVelocityY = 90
    playerVelocityDouble = 180
    m = 5

    x = 0

    score = 0

    isjump = False
    doublejump = False
    doubleCheck = False

    present = pygame.image.load("drawable/sled.png")
    present = pygame.transform.scale(present,(120,150))

    gameoverback = pygame.image.load("drawable/gameoverBack.jpg")
    gameoverback = pygame.transform.scale(gameoverback,(1147,646))

    #Monster
    monsterNumber = 0
    monsterPosX = 1000
    monsterPosY = 355
    monster_die = pygame.image.load("drawable/big-bang.png")
    monster_die = pygame.transform.scale(monster_die,(100,100))

    monster_left = pygame.image.load("drawable/alien.png")
    monsterWidth,monsterHeight = monster_left.get_rect().size

    monster_right = pygame.image.load("drawable/alien2.png")

    isMonsterDie = False

    stolen = False
    game_over = False

    fontObj = pygame.font.Font("drawable/amatic/AmaticSC-Regular.ttf",140)
    textSurfaceObj = fontObj.render("Game Over ! ",True,GOLD)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (475,480)

    fontObj2 = pygame.font.Font("drawable/seoul_hangang.ttf", 23)
    textSurfaceObj2 = fontObj2.render("다시 시작하기 위해서는 화면을 클릭해주세요", True, WHITE)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (460, 610)

    fontObj3 = pygame.font.Font("drawable/amatic/AmaticSC-Regular.ttf", 50)

    christmas_music = "drawable/music2.mp3"
    mixer.init()
    mixer.music.load(christmas_music)
    mixer.music.play(-1)

    monster_touch_music = pygame.mixer.Sound("drawable/monster_touch.wav")

    while True:
        events()
        monster_touch_music = pygame.mixer.Sound("drawable/monster_touch.wav")

        #사용자 클릭 이벤트
        k=pygame.key.get_pressed()
        if stolen == False :
            if k[K_RIGHT] or k[K_LEFT] or k[K_UP] or k[K_SPACE]:
                if k[K_RIGHT]:
                    playerVelocityX = 2
                if k[K_LEFT]:
                    playerVelocityX = -2
                if k[K_UP]:
                    isjump = True
                if k[K_SPACE]:
                    if isjump == True:
                        if playerVelocityY<0:
                            doublejump = True

            else:
                playerVelocityX = -1

        #배경 스크롤링
        if playerPosX < startScrollingPosX:
            circlePosX = playerPosX
        elif playerPosX > stagePosX - startScrollingPosX:
            circlePosX = playerPosX - stagePosX + W
        else:
            circlePosX = startScrollingPosX
            stagePosX += -playerVelocityX
        stagePosX -= 0.8
        rel_x = stagePosX % bgWidth
        DS.blit(bg, (rel_x - bgWidth, 0))
        if rel_x < W:
            DS.blit(bg, (rel_x, 0))

        if stolen == False:
            textSurfaceObj3 = fontObj3.render(("Monster to beat    " + str(score) + " / 20"), True, GOLD)
            textRectObj3 = textSurfaceObj3.get_rect()
            textRectObj3.center = (475, 50)
            DS.blit(textSurfaceObj3, textRectObj3)

            # 플레이어 일반 점프
            if not doublejump:
                if isjump:
                    # 힘을 계산한다( F = 0.5 * m * v*v )
                    if playerVelocityY > 0:
                        F = (0.5 * m * playerVelocityY * playerVelocityY * 0.0002)
                    else:
                        F = -(0.5 * m * playerVelocityY * playerVelocityY * 0.00004)

                    playerPosY = playerPosY - F

                    playerVelocityY = playerVelocityY - 1

                    if playerPosY >= 485:
                        playerPosY = 485
                        isjump = False
                        playerVelocityY = 90

            # 플레이어 더블 점프
            elif doublejump:
                # 힘을 계산한다( F = 0.5 * m * v*v )
                if playerVelocityDouble > 0:
                    F = (0.5 * m * playerVelocityDouble * playerVelocityDouble * 0.000033)
                else:
                    F = -(0.5 * m * playerVelocityDouble * playerVelocityDouble * 0.0005)

                playerPosY = playerPosY - F

                playerVelocityDouble = playerVelocityDouble - 1

                if playerPosY >= 485:
                    playerPosY = 485
                    isjump = False
                    playerVelocityY = 90
                    playerVelocityDouble = 180
                    doublejump = False
                    m = 5

            playerPosX += playerVelocityX

            # 배경 한계선 설정
            if playerPosX > stageWidth - circleRadius: playerPosX = stageWidth - circleRadius
            if playerPosX < circleRadius + 25: playerPosX = circleRadius + 25
            if playerPosX >= 800 - circleRadius: playerPosX = 800 - circleRadius


            # 점프 상태에 따른 색 변화
            if not doublejump:
                pygame.draw.circle(DS, WHITE, (playerPosX, int(playerPosY - circleRadius)), circleRadius, 0)
            elif doublejump:
                if playerVelocityDouble <= 8:
                    pygame.draw.circle(DS, PASTEL_RED, (playerPosX, int(playerPosY - circleRadius)), circleRadius, 0)
                else:
                    pygame.draw.circle(DS, PASTEL_BLUE, (playerPosX, int(playerPosY - circleRadius)), circleRadius, 0)

            #몬스터 출현
            if isMonsterDie == False:
                if monsterPosX > 92+playerPosX/9:
                    DS.blit(monster_left,(monsterPosX, monsterPosY))
                    monsterPosX -= 1.2
                elif monsterPosX <= 92+playerPosX/9:
                    stolen = True

                # 충돌
                if doublejump:
                    if playerVelocityDouble < 0:
                         if playerPosX <= monsterPosX + monsterWidth / 2 + 5 and playerPosX >= monsterPosX - monsterWidth / 2 + 5 and playerPosY + 25 >= monsterPosY:
                            monster_touch_music.play(0)
                            DS.blit(monster_die, (monsterPosX + 10, monsterPosY))
                            isMonsterDie = True
                            score += 1

            else :
                DS.blit(monster_die,(monsterPosX,monsterPosY))
                monsterPosX -= 2
                monsterPosY -= 1
                if monsterPosX <= -50:
                    isMonsterDie = False
                    monsterPosX = 950
                    monsterPosY = 355

            #선물더미 그리기
            DS.blit(present, (playerPosX/9, 355))
            pygame.draw.line(DS, PASTEL_GRAY, (92+playerPosX/9, 450), (playerPosX, playerPosY - 25), 5)



        elif not monsterPosX >= 1100:
            #몬스터가 선물 가져감
            DS.blit(present, (monsterPosX-100, 355))
            DS.blit(monster_right, (monsterPosX+20, monsterPosY))
            pygame.draw.line(DS, PASTEL_GRAY, (monsterPosX-16, 450), (monsterPosX + 55, monsterPosY +80), 5)
            monsterPosX += 1
            if monsterPosX >= 1100:
                game_over = True

        if game_over :
            DS.fill(BLACK)
            DS.blit(gameoverback,(-123,0))
            DS.blit(textSurfaceObj2, textRectObj2)
            DS.blit(textSurfaceObj, textRectObj)


        pygame.display.update()
        CLOCK.tick(FPS)
        DS.fill(BLACK)