import pygame
import os
import main.item.ConversationItem
import main.display.MakeButton

# 파이게임 초기화
pygame.init()
# 윈도우 창의 크기 설정
screen = pygame.display.set_mode((640, 480))

makeButton = main.display.MakeButton.MakeButton
convItem = main.item.ConversationItem.ConversationItem()

os.chdir(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
back = pygame.image.load("drawable/christmas1.jpg")
screen.blit(pygame.transform.scale(back, (640, 480)), (0, 0))
font = pygame.font.SysFont("comicsansms", 40)
startText = font.render("Welcome to Santa village !", True, (0, 0, 0))
screen.blit(startText, (135, 400))

class GameStart:

    def __init__(self):
        pygame.init()
        self.button1 = makeButton((0, 108, 250), 20, 265, 600, 90, convItem.item[5])
        self.button2 = makeButton((0, 108, 250), 20, 365, 600, 90, convItem.item[6])
        self.screen = pygame.display.set_mode((640, 480))
        self.takeCheck = 1
        self.run = True


    # 행복한 산타마을 등장
    def Take1(self):
        christmasPresent = pygame.image.load("drawable/christmas3.jpg")
        screen.blit(pygame.transform.scale(christmasPresent, (640, 480)), (0, 0))
        # santa = pygame.image.load("drawable/santa-claus.png")
        # santa = pygame.transform.scale(santa, (180, 180))
        # screen.blit(santa, (420, 240))
        self.takeCheck += 1

    # 누군가 선물을 다 가져간다고 한다 !
    def Take2(self):
        font = pygame.font.SysFont("comicsansms", 40)
        screen.fill((0, 0, 0))
        # pygame.draw.rect(screen, (255, 255, 255), [50, 360, 530, 80], 3)
        text = font.render(convItem.item[2], True, ((255, 0, 0)))
        screen.blit(text, (150, 370))
        self.takeCheck += 1

    # 도둑이다 !
    def Take3(self):
        screen.fill((0, 0, 0))
        badbad = pygame.image.load("drawable/devil.png")
        badbad = pygame.transform.scale(badbad, (230, 230))
        screen.blit(badbad, (200, 100))
        self.takeCheck += 1

    # 산타집을 턴 도둑, 눈 앞에서 선물 뺏긴 산타
    def Take4(self):
        snowWorld = pygame.image.load("drawable/snowworld.PNG")
        screen.blit(pygame.transform.scale(snowWorld, (640, 480)), (0, 0))
        theif = pygame.image.load('drawable/criminal.png')
        santaclaus = pygame.image.load('drawable/santaclaus.png')
        # 위에 도둑도망가기 , 산타는 따라가다 멈추기
        self.takeCheck += 1

    # 산타 슬퍼 누가 내 선물 찾아와
    def Take5(self):
        crysanta = pygame.image.load('drawable/crysanta.PNG')
        screen.blit(pygame.transform.scale(crysanta, (640, 480)), (0, 0))
        font = pygame.font.SysFont("comicsansms", 30)
        text2 = font.render(convItem.item[3], True, ((0, 0, 0)))
        screen.blit(text2, (100, 390))
        self.takeCheck += 1

    # (유저네임)동글이가 간다
    def Take6(self):
        font = pygame.font.SysFont("comicsansms", 30)
        circleBack = pygame.image.load("drawable/circleBack.PNG")
        screen.blit(pygame.transform.scale(circleBack, (640, 480)), (0, 0))
        text3 = font.render(convItem.item[4], True, (0, 0, 0))
        screen.blit(text3, (100, 400))
        self.takeCheck += 1

    def Take7(self):
        screen.fill((13, 132, 0))
        self.button1.draw(screen, (0, 0, 0))
        self.button2.draw(screen, (0, 0, 0))
        self.takeCheck += 1

    # 게임 설명 넣기
    def Take8_1(self):
        screen.fill((0, 0, 0))

    # 게임 연결하기
    def Take8_2(self):
        screen.fill(255, 255, 255)

    def run(self):
        while self.run:
            pygame.display.update()
            pygame.display.set_caption("Time Keeper Game !")

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

                if self.takeCheck == 7:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button1.isOver(pos):
                            self.Take8_1()
                            print("button1 was clicked !")
                        elif self.button2.isOver(pos):
                            self.Take8_2()
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

if __name__ == '__main__':
    gameDisplay = GameStart()
    gameDisplay.run