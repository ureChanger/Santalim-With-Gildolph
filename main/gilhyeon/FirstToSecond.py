import pygame
import os
import sys
from pygame.locals import *
import time

class FirstToSecond :
    def __init__(self):
        self.startTime = time.time()

        pygame.init()
        os.chdir(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

        self.W, self.H = 900, 640
        self.HW, self.HH = self.W / 2, self.H / 2
        self.AREA = self.W + self.H

        os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

        self.CLOCK = pygame.time.Clock()
        self.DS = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Fist To Second")
        self.FPS = 80

        #사진로드

        self.bg = pygame.image.load("drawable/bkgd_stage2.png")
        self.bgWidth, self.bgHeight = self.bg.get_rect().size

        self.frame= pygame.image.load("drawable/frame.png")

        self.greenMonsterHint = pygame.image.load("drawable/greenAlien.png")
        self.greenLittleMonsterHint = pygame.image.load("drawable/greenLittleAlien.png")
        self.skullHint = pygame.image.load("drawable/skull.png")

        self.arrow = pygame.image.load("drawable/arrow.png")

        self.BLACK = (0, 0, 0, 255)
        self.WHITE = (255, 255, 255, 255)

        self.stageWidth = self.bgWidth * 2
        self.stagePosX = 0

        #텍스트
        self.fontObj = pygame.font.Font("drawable/seoul_hangang.ttf", 40)
        self.textSurfaceObj = self.fontObj.render("☆ 한가지 팁 ☆ ", True, self.BLACK)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (465, 120)

        self.fontObj2 = pygame.font.Font("drawable/seoul_hangang.ttf", 23)
        self.textSurfaceObj2 = self.fontObj2.render("초록 괴물은 두번 타격을 줘야한다고 합니다 !", True, self.BLACK)
        self.textRectObj2 = self.textSurfaceObj2.get_rect()
        self.textRectObj2.center = (460, 510)

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        startTime = time.time()
        currentTime = 0

        while currentTime <= 1.5:
            print(time.time())
            print(currentTime)
            currentTime = time.time() - startTime
            self.DS.fill(self.BLACK)
            pygame.display.update()

        while True:
            self.events()

            # 배경 스크롤링
            self.stagePosX -= 4
            self.rel_x = self.stagePosX % self.bgWidth
            self.DS.blit(self.bg, (self.rel_x - self.bgWidth, 20))
            if self.rel_x < self.W:
                self.DS.blit(self.bg, (self.rel_x, 20))

            self.DS.blit(self.frame,(190,55))
            self.DS.blit(self.greenMonsterHint,(220, 250))
            self.DS.blit(self.arrow, (340, 300))
            self.DS.blit(self.greenLittleMonsterHint, (385, 250))
            self.DS.blit(self.arrow, (525, 300))
            self.DS.blit(self.skullHint, (570, 250))
            self.DS.blit(self.textSurfaceObj2, self.textRectObj2)
            self.DS.blit(self.textSurfaceObj, self.textRectObj)

            currentTime = time.time() - startTime
            if currentTime >= 4.5 :
                return 1


            pygame.display.update()