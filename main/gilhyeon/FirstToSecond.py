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
        os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

        self.DS = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Fist To Second")

        self.bkgd = pygame.image.load("drawable/bkgd_stage2.png")
        self.frame= pygame.image.load("drawable/frame.png")
        self.monsterHint = pygame.image.load("drawable/greenAlien.png")

        self.BLACK = (0, 0, 0, 100)
        self.WHITE = (255, 255, 255, 255)

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.events()
            if time.time() - self.startTime >= 6:
                self.DS.blit(self.bkgd,(0,20))
                pygame.draw.rect(self.DS, self.BLACK, [100,100,100,100],0)

            else :
                self.DS.fill(self.BLACK)
            pygame.display.update()