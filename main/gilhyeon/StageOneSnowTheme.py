import pygame
from pygame.locals import *
import sys
import os
from pygame import mixer

class StageOneSnowTheme:
    def __init__(self):
        self.W, self.H = 900, 646
        self.HW, self.HH = self.W / 2, self.H / 2
        self.AREA = self.W + self.H

        os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

        pygame.init()
        os.chdir(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
        self.CLOCK = pygame.time.Clock()
        self.DS = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("BackgroundScrolling with Player")
        self.FPS = 400

        # define some colors
        self.BLACK = (0, 0, 0, 255)
        self.WHITE = (255, 255, 255, 255)
        self.PASTEL_BLUE = (217, 241, 255, 200)
        self.PASTEL_RED = (255, 114, 114, 255)
        self.PASTEL_GRAY = (80, 78, 82, 255)
        self.GOLD = (189, 150, 25, 255)

        self.bg = pygame.image.load('drawable/bkgd_winter2.jpg').convert()
        self.bgWidth, self.bgHeight = self.bg.get_rect().size

        self.stageWidth = self.bgWidth * 2
        self.stagePosX = 0

        self.startScrollingPosX = self.HW

        self.circleRadius = 25
        self.circlePosX = self.circleRadius

        self.playerPosX = self.circleRadius + 50
        self.playerPosY = 485
        self.playerVelocityX = 0

        self.playerVelocityY = 90
        self.playerVelocityDouble = 180
        self.m = 5

        self.x = 0

        self.score = 0

        self.isjump = False
        self.doublejump = False
        self.doubleCheck = False

        self.present = pygame.image.load("drawable/sled.png")
        self.present = pygame.transform.scale(self.present, (120, 150))

        self.gameoverback = pygame.image.load("drawable/gameoverBack.jpg")
        self.gameoverback = pygame.transform.scale(self.gameoverback, (1147, 646))

        # Monster
        self.monsterNumber = 0
        self.monsterPosX = 1000
        self.monsterPosY = 355
        self.monster_die = pygame.image.load("drawable/big-bang.png")
        self.monster_die = pygame.transform.scale(self.monster_die, (100, 100))

        self.monster_left = pygame.image.load("drawable/alien.png")
        self.monsterWidth, monsterHeight = self.monster_left.get_rect().size

        self.monster_right = pygame.image.load("drawable/alien2.png")

        self.isMonsterDie = False

        self.stolen = False
        self.game_over = False

        self.fontObj = pygame.font.Font("drawable/amatic/AmaticSC-Regular.ttf", 140)
        self.textSurfaceObj = self.fontObj.render("Game Over ! ", True, self.GOLD)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (475, 480)

        self.fontObj2 = pygame.font.Font("drawable/seoul_hangang.ttf", 23)
        self.textSurfaceObj2 = self.fontObj2.render("다시 시작하기 위해서는 화면을 클릭해주세요", True, self.WHITE)
        self.textRectObj2 = self.textSurfaceObj2.get_rect()
        self.textRectObj2.center = (460, 610)

        self.fontObj3 = pygame.font.Font("drawable/amatic/AmaticSC-Regular.ttf", 50)

        self.christmas_music = "drawable/music2.mp3"
        mixer.init()
        mixer.music.load(self.christmas_music)
        mixer.music.play(-1)

        self.monster_touch_music = pygame.mixer.Sound("drawable/monster_touch.wav")

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()


    def run(self):
        while True:
            self.events()
            self.monster_touch_music = pygame.mixer.Sound("drawable/monster_touch.wav")

            #사용자 클릭 이벤트
            k=pygame.key.get_pressed()
            if self.stolen == False :
                if k[K_RIGHT] or k[K_LEFT] or k[K_UP] or k[K_SPACE]:
                    if k[K_RIGHT]:
                        self.playerVelocityX = 2
                    if k[K_LEFT]:
                        self.playerVelocityX = -3
                    if k[K_UP]:
                        self.isjump = True
                    if k[K_SPACE]:
                        if self.isjump == True:
                            if self.playerVelocityY<0:
                                self.doublejump = True

                else:
                    self.playerVelocityX = -1

            #배경 스크롤링
            if self.playerPosX < self.startScrollingPosX:
                self.circlePosX = self.playerPosX
            elif self.playerPosX > self.stagePosX - self.startScrollingPosX:
                self.circlePosX = self.playerPosX - self.stagePosX + self.W
            else:
                self.circlePosX = self.startScrollingPosX
                self.stagePosX += -self.playerVelocityX
            self.stagePosX -= 0.8
            self.rel_x = self.stagePosX % self.bgWidth
            self.DS.blit(self.bg, (self.rel_x - self.bgWidth, 0))
            if self.rel_x < self.W:
                self.DS.blit(self.bg, (self.rel_x, 0))

            if self.stolen == False:
                self.textSurfaceObj3 = self.fontObj3.render(("Monster to beat    " + str(self.score) + " / 20"), True, self.GOLD)
                self.textRectObj3 = self.textSurfaceObj3.get_rect()
                self.textRectObj3.center = (475, 50)
                self.DS.blit(self.textSurfaceObj3, self.textRectObj3)

                # 플레이어 일반 점프
                if not self.doublejump:
                    if self.isjump:
                        # 힘을 계산한다( F = 0.5 * m * v*v )
                        if self.playerVelocityY > 0:
                            F = (0.5 * self.m * self.playerVelocityY * self.playerVelocityY * 0.0002)
                        else:
                            F = -(0.5 * self.m * self.playerVelocityY * self.playerVelocityY * 0.0004)

                        self.playerPosY = self.playerPosY - F

                        self.playerVelocityY = self.playerVelocityY - 1

                        if self.playerPosY >= 485:
                            self.playerPosY = 485
                            self.isjump = False
                            self.playerVelocityY = 90

                # 플레이어 더블 점프
                elif self.doublejump:
                    # 힘을 계산한다( F = 0.5 * m * v*v )
                    if self.playerVelocityDouble > 0:
                        F = (0.5 * self.m * self.playerVelocityDouble * self.playerVelocityDouble * 0.000033)
                    else:
                        F = -(0.5 * self.m * self.playerVelocityDouble * self.playerVelocityDouble * 0.0005)

                    self.playerPosY = self.playerPosY - F

                    self.playerVelocityDouble = self.playerVelocityDouble - 1

                    if self.playerPosY >= 485:
                        self.playerPosY = 485
                        self.isjump = False
                        self.playerVelocityY = 90
                        self.playerVelocityDouble = 180
                        self.doublejump = False
                        self.m = 5

                self.playerPosX += self.playerVelocityX

                # 배경 한계선 설정
                if self.playerPosX > self.stageWidth - self.circleRadius: self.playerPosX = self.stageWidth - self.circleRadius
                if self.playerPosX < self.circleRadius + 25: self.playerPosX = self.circleRadius + 25
                if self.playerPosX >= 800 - self.circleRadius: self.playerPosX = 800 - self.circleRadius


                # 점프 상태에 따른 색 변화
                if not self.doublejump:
                    pygame.draw.circle(self.DS, self.WHITE, (self.playerPosX, int(self.playerPosY - self.circleRadius)), self.circleRadius, 0)
                elif self.doublejump:
                    if self.playerVelocityDouble <= 8:
                        pygame.draw.circle(self.DS, self.PASTEL_RED, (self.playerPosX, int(self.playerPosY - self.circleRadius)), self.circleRadius, 0)
                    else:
                        pygame.draw.circle(self.DS, self.PASTEL_BLUE, (self.playerPosX, int(self.playerPosY - self.circleRadius)), self.circleRadius, 0)

                #몬스터 출현
                if self.isMonsterDie == False:
                    if self.monsterPosX > 92+self.playerPosX/9:
                        self.DS.blit(self.monster_left,(self.monsterPosX, self.monsterPosY))
                        self.monsterPosX -= 1.2
                    elif self.monsterPosX <= 92+self.playerPosX/9:
                        self.stolen = True

                    # 충돌
                    if self.doublejump:
                        if self.playerVelocityDouble < 0:
                             if self.playerPosX <= self.monsterPosX + self.monsterWidth / 2 + 5 and self.playerPosX >= self.monsterPosX - self.monsterWidth / 2 + 5 and self.playerPosY + 25 >= self.monsterPosY:
                                self.monster_touch_music.play(0)
                                self.DS.blit(self.monster_die, (self.monsterPosX + 10, self.monsterPosY))
                                self.isMonsterDie = True
                                self.score += 1

                else :
                    self.DS.blit(self.monster_die,(self.monsterPosX,self.monsterPosY))
                    self.monsterPosX -= 2
                    self.monsterPosY -= 1
                    if self.monsterPosX <= -50:
                        self.isMonsterDie = False
                        self.monsterPosX = 950
                        self.monsterPosY = 355

                #선물더미 그리기
                self.DS.blit(self.present, (self.playerPosX/9, 355))
                pygame.draw.line(self.DS, self.PASTEL_GRAY, (92+self.playerPosX/9, 450), (self.playerPosX, self.playerPosY - 25), 5)



            elif not self.monsterPosX >= 1100:
                #몬스터가 선물 가져감
                self.DS.blit(self.present, (self.monsterPosX-100, 355))
                self.DS.blit(self.monster_right, (self.monsterPosX+20, self.monsterPosY))
                pygame.draw.line(self.DS, self.PASTEL_GRAY, (self.monsterPosX-16, 450), (self.monsterPosX + 55, self.monsterPosY +80), 5)
                self.monsterPosX += 1
                if self.monsterPosX >= 1100:
                    self.game_over = True

            if self.game_over :
                self.DS.fill(self.BLACK)
                self.DS.blit(self.gameoverback,(-123,0))
                self.DS.blit(self.textSurfaceObj2, self.textRectObj2)
                self.DS.blit(self.textSurfaceObj, self.textRectObj)

            pygame.display.update()
            self.CLOCK.tick(self.FPS)
            self.DS.fill(self.BLACK)
