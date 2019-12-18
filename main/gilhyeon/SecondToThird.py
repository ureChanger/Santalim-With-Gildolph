import pygame
import os
import sys
from pygame.locals import *
import time

class SecondToThird :
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

        self.bg = pygame.image.load("drawable/bkgd_final.jpg")
        self.bgWidth, self.bgHeight = self.bg.get_rect().size

        self.frame= pygame.image.load("drawable/frame.png")

        self.BLACK = (0, 0, 0, 255)
        self.RED = (255, 0, 0, 255)
        self.WHITE = (255, 255, 255, 255)

        self.stageWidth = self.bgWidth * 2
        self.stagePosX = 0

        self.iceBreak = pygame.image.load("drawable/iceBreak.jpg")
        self.unknownOne = pygame.image.load("drawable/mistery.png")

        #텍스트
        self.fontObj = pygame.font.Font("drawable/seoul_hangang.ttf", 40)
        self.textSurfaceObj = self.fontObj.render("☆ 주의 ☆ ", True, self.RED)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (465, 120)

        self.fontObj2 = pygame.font.Font("drawable/seoul_hangang.ttf", 23)
        self.textSurfaceObj2 = self.fontObj2.render("귀여운 모습에 속지 마세요 !!!", True, self.BLACK)
        self.textRectObj2 = self.textSurfaceObj2.get_rect()
        self.textRectObj2.center = (450, 510)
        self.fontObj3 = pygame.font.Font("drawable/seoul_hangang.ttf", 50)

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        startTime = time.time()
        currentTime = 0

        while currentTime <= 2.3:
            print(time.time())
            print(currentTime)
            currentTime = time.time() - startTime
            self.DS.blit(self.iceBreak,(0,0))
            self.DS.blit(self.iceBreak, (0, 0))
            self.textSurfaceObj3 = self.fontObj3.render(("3 스테이지로 이동중 ... [ 지옥 ]"),
                                                        True,
                                                        self.WHITE)
            self.textRectObj3 = self.textSurfaceObj3.get_rect()
            self.textRectObj3.center = (400, 550)
            self.DS.blit(self.textSurfaceObj3, self.textRectObj3)
            pygame.display.update()

        self.DS.fill(self.BLACK)

        while True:
            self.events()

            # 배경 스크롤링
            self.stagePosX -= 4
            self.rel_x = self.stagePosX % self.bgWidth
            self.DS.blit(self.bg, (self.rel_x - self.bgWidth, 20))
            if self.rel_x < self.W:
                self.DS.blit(self.bg, (self.rel_x, 20))

            self.DS.blit(self.frame,(190,55))
            self.DS.blit(self.unknownOne, (325, 180))
            self.DS.blit(self.textSurfaceObj2, self.textRectObj2)
            self.DS.blit(self.textSurfaceObj, self.textRectObj)

            currentTime = time.time() - startTime
            if currentTime >= 6.5 :
                return 1


            pygame.display.update()