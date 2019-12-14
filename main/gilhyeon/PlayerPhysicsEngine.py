import os
import pygame
from pygame.locals import *
from time import sleep

os.chdir(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

class Player:
    x = 10
    y = 300
    speed = 7

    # 플레이어가 점프중인지 아닌지 저장
    isjump = 0

    # 힘(v)와 질량(m)
    v = 8
    m = 2

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def jump(self):
        self.isjump = 1

    def update(self):
        if self.isjump:
            print("y 좌표 : ", self.y)
            print("v : ",self.v)

            #힘을 계산한다( F = 0.5 * m * v*v )
            if self.v > 0:
                F = (0.5 * self.m * self.v * self.v + 8)
            else:
                F = -(0.5 * self.m *self.v * self.v *0.022)

            #포지션을 바꾼다.
            self.y = self.y - F

            #가속을 바꾼다.
            self.v = self.v - 1
            print("힘(F) : ",F)

            #만약 바닥에 닿았을 경우, 가속을 리셋한다.
            if self.y >= 300:
                self.y = 300
                self.isjump = 0
                self.v = 8

class App:
    width, height = 640, 480
    player = 0

    def __init__(self):
        self._running = True
        self.player = Player()

    #게임 시작 화면
    def on_init(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Time Keeper Game !")
        self._running = True

        background = pygame.image.load('drawable/mainGameBackground.gif')
        self.playerIng = pygame.image.load('drawable/run.png').convert()

        self.gameDisplay.blit(background, (0,0))

        pygame.display.update()

    #Esc누르면 종료
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass


    def on_render(self):
        self.gameDisplay.blit(self.playerIng, (self.player.x, self.player.y))
        self.player.update()
        pygame.display.flip()
        sleep(0.0159)

    #pygame 종료
    def on_cleanup(self):
        pygame.quit()


    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                self.player.moveRight()

            if keys[K_LEFT]:
                self.player.moveLeft()

            if keys[K_UP]:
                self.player.jump()

            if keys[K_ESCAPE]:
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()