import pygame
import os
import main.item.ConversationItem
import main.display.MakeButton
from main.gilhyeon.GameTest import MainGame

class GameStart:

    def __init__(self):
        # 파이게임 초기화
        pygame.init()
        # 윈도우 창의 크기 설정
        self.screen = pygame.display.set_mode((640, 480))
        self.makeButton = main.display.MakeButton.MakeButton
        self.convItem = main.item.ConversationItem.ConversationItem()

        os.chdir(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

        self.back = pygame.image.load("drawable/snowback.png")
        self.screen.blit(pygame.transform.scale(self.back, (640, 480)), (0, 0))
        self.font = pygame.font.SysFont("comicsansms", 40)
        self.startText = self.font.render("Welcome to Santa village !", True, (0, 0, 0))
        self.screen.blit(self.startText, (35, 30))

        self.button1 = self.makeButton((0, 108, 250), 20, 265, 600, 90, self.convItem.item[5])
        self.button2 = self.makeButton((0, 108, 250), 20, 365, 600, 90, self.convItem.item[6])
        self.takeCheck = 1
        self.run = True

        self.mainGame = MainGame()

    def redrawWindow(self):
        self.button1.draw(self.screen, (0, 0, 0))
        self.button2.draw(self.screen, (0, 0, 0))

    # 행복한 산타마을 등장
    def Take1(self):
        self.christmasPresent = pygame.image.load("drawable/christmas3.jpg")
        self.screen.blit(pygame.transform.scale(self.christmasPresent, (640, 480)), (0, 0))

    # 누군가 선물을 다 가져간다고 한다 !
    def Take2(self):
        font = pygame.font.SysFont("comicsansms", 40)
        self.screen.fill((200, 200, 200))
        self.robbrr = pygame.image.load("drawable/robber.png")
        self.screen.blit(self.robbrr,(240, 250))
        self.text = font.render(self.convItem.item[2], True, ((255, 0, 0)))
        self.screen.blit(self.text, (80, 370))

    # 도둑이다 !
    def Take3(self):
        self.back = pygame.image.load("drawable/snowback2.png.jpg")
        self.screen.blit(pygame.transform.scale(self.back, (640, 480)), (0, 0))
        self.badbad = pygame.image.load("drawable/criminal.png")
        self.badbad = pygame.transform.scale(self.badbad, (100, 100))
        self.screen.blit(self.badbad, (100, 170))

    # 산타집을 턴 도둑, 눈 앞에서 선물 뺏긴 산타
    def Take4(self):
        font = pygame.font.SysFont("comicsansms", 80)
        self.beggarSanta = pygame.image.load("drawable/sadSanta.PNG")
        self.screen.blit(pygame.transform.scale(self.beggarSanta, (640, 480)), (0, 0))
        self.text7 = font.render(self.convItem.item[10], True, ((0, 0, 0)))
        self.screen.blit(self.text7, (180, 100))

    # 산타 슬퍼 누가 내 선물 찾아와
    def Take5(self):
        crysanta = pygame.image.load('drawable/crysanta.PNG')
        self.screen.blit(pygame.transform.scale(crysanta, (640, 480)), (0, 0))
        font = pygame.font.SysFont("comicsansms", 28)
        text2 = font.render(self.convItem.item[3], True, ((255, 255, 255)))
        self.screen.blit(text2, (120, 330))

    # (유저네임)동글이가 간다
    def Take6(self):
        font = pygame.font.SysFont("comicsansms", 30)
        circleBack = pygame.image.load("drawable/donggeul.PNG")
        self.screen.blit(pygame.transform.scale(circleBack, (640, 480)), (0, 0))
        text3 = font.render(self.convItem.item[4], True, (0, 0, 0))
        self.screen.blit(text3, (110, 40))

    def Take7(self):
        self.screen.fill((13, 132, 0))
        self.redrawWindow()

    # 게임 설명 넣기
    def Take8(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont("comicsansms", 20)
        self.text4 = font.render(self.convItem.item[7], True, ((252, 88, 0)))
        self.text5 = font.render(self.convItem.item[8], True, ((252, 88, 0)))
        self.text6 = font.render(self.convItem.item[9], True, ((252, 88, 0)))
        self.screen.blit(self.text4, (30, 300))
        self.screen.blit(self.text5, (30, 345))
        self.screen.blit(self.text6, (30, 370))
        self.snowjump = pygame.image.load('drawable/snowjump.jpg')
        self.catch = pygame.image.load('drawable/catch.jpg')
        self.snowjump = pygame.transform.scale(self.snowjump, (292, 219))
        self.catch = pygame.transform.scale(self.catch, (292,219))
        self.screen.blit(self.snowjump, (20, 30))
        self.screen.blit(self.catch, (330, 30))

    def Run(self):
        while self.run:
            pygame.display.update()
            pygame.display.set_caption("SNOW RUN")

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    exit()

                # 마우스로 화면을 눌렀을때
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.takeCheck == 1:
                        self.Take1()
                        self.takeCheck += 1
                    elif self.takeCheck == 2:
                        self.Take2()
                        self.takeCheck += 1
                    elif self.takeCheck == 3:
                        self.Take3()
                        self.takeCheck += 1
                    elif self.takeCheck == 4:
                        self.Take4()
                        self.takeCheck += 1
                    elif self.takeCheck == 5:
                        self.Take5()
                        self.takeCheck += 1
                    elif self.takeCheck == 6:
                        self.Take6()
                        self.takeCheck += 1
                    elif self.takeCheck == 7:
                        self.Take7()

                # 버튼 눌렸을 때
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button1.isOver(pos):
                        self.Take8()
                        print("button1 was clicked !")
                    elif self.button2.isOver(pos):
                        self.mainGame.run()
                        print("button2 was clicked !")

                if event.type == pygame.MOUSEMOTION:
                    if self.button1.isOver(pos):
                        self.button1.color = (255, 255, 0)
                    else:
                        self.button1.color = (172, 164, 255)

                    if self.button2.isOver(pos):
                        self.button2.color = (250, 250, 0)
                    else:
                        self.button2.color = (172, 164, 255)