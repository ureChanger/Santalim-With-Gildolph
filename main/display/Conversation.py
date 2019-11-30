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
back = pygame.image.load("drawable/pooh.jpg")
screen.blit(pygame.transform.scale(back, (640, 480)), (0, 0))

run = True

class GameStart:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        #screen.fill((0, 0, 0))
        #self.nextButton = makeButton((255, 205, 5), 560, 380, 50, 50, ">")

    def redrawWindow(self):
        #self.nextButton.draw(screen, (0, 0, 0))
        self.selectbutton1.draw(screen, (0, 0, 0))
        self.selectbutton2.draw(screen, (0, 0, 0))
        self.selectbutton3.draw(screen, (0, 0, 0))
        self.selectbutton4.draw(screen, (0, 0, 0))

    def Take1():
        font = pygame.font.Font(None, 40)
        screen.fill((0, 0, 0))
        text1 = font.render(convItem.item[0], True, (255, 255, 255))
        text2 = font.render(convItem.item[1], True, (255, 255, 255))
        screen.blit(text1, (100, 300))
        screen.blit(text2, (100, 350))

    def Take2():
        font = pygame.font.Font(None, 40)
        # screen.fill((0, 0, 0))
        cutie2 = pygame.image.load("drawable/cutie2.png")
        screen.blit(cutie2, (100, 200))
        pygame.draw.rect(screen, (255, 255, 255), [50, 360, 500, 80], 3)
        text3 = font.render(convItem.item[2], True, (255, 255, 255))
        screen.blit(text3, (120, 390))

    def Take3():
        # screen.fill((0, 0, 0))
        wizard1 = pygame.image.load("drawable/wizard1.png")
        screen.blit(wizard1, (10, -25))
        selectbutton1 = makeButton((0, 0, 255), 20, 265, 600, 90, convItem.item[3])
        selectbutton2 = makeButton((0, 0, 255), 20, 365, 600, 90, convItem.item[4])

    def Take4_1(self):
        # screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 40)
        postIt = pygame.image.load("drawable/postIt.png")
        screen.bilt(postIt, (40, 20))
        text8 = font.render(convItem.item[7], True, (255, 255, 255))
        text9 = font.render(convItem.item[8], True, (255, 255, 255))
        screen.blit(text8, (100, 300))
        screen.blit(text9, (100, 350))


    def Take4_2(self):
        font = pygame.font.Font(None, 40)
        blood = pygame.image.load("drawable/blood.PNG")
        screen.blit(pygame.transform.scale(blood, (640, 480)), (0, 0))
        text6 = font.render(convItem.item[5], True, (255, 255, 255))
        text7 = font.render(convItem.item[6], True, (255, 0, 0))
        screen.blit(text6, (100, 300))
        screen.blit(text7, (100, 350))
        breakpoint()

    def Take5(self):
        heroUnicorn = pygame.image.load("drawable/heroUnicorn.png")
        screen.bilt(heroUnicorn, (40, 20))
        self.selectbutton3 = makeButton((0, 0, 255), 20, 265, 600, 90, convItem.item[9])
        self.selectbutton4 = makeButton((0, 0, 255), 20, 365, 600, 90, convItem.item[10])
        screen(self.selectbutton3)
        screen(self.selectbutton4)

    def Take6_2(self):
        font = pygame.font.Font(None, 40)
        blood = pygame.image.load("drawable/blood.PNG")
        screen.blit(pygame.transform.scale(blood, (640, 480)), (0, 0))
        text10 = font.render(convItem.item[11], True, (255, 255, 255))
        text11 = font.render(convItem.item[12], True, (255, 0, 0))
        screen.blit(text10, (100, 300))
        screen.blit(text11, (100, 350))
        breakpoint()

    takeCheck = 1
    while run:
        pygame.display.update()
        pygame.display.set_caption("Time Keeper Game !")


        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

            # 마우스로 버튼을 눌렀을때
            if event.type == pygame.MOUSEBUTTONDOWN:
                if takeCheck == 1:
                    Take1()
                    takeCheck += 1
                    print(1)
                    print(takeCheck)
                elif takeCheck == 2:
                    Take2()
                    takeCheck += 1
                    print(2)
                elif takeCheck == 3:
                    Take3()
                    takeCheck += 1
                elif takeCheck == 4:
                    Take4_1()
                    takeCheck += 1
                elif takeCheck == 5:
                    Take5()
                    takeCheck += 1
                elif takeCheck == 6:
                    Take6_2()
                    takeCheck += 1
            # elif selectbutton1.isOver(pos):

            # elif selectbutton2.isOver(pos):

        # if event.type == pygame.MOUSEMOTION:
        #     if nextButton.isOver(pos):
        #         nextButton.color = (255, 255, 0)
        #     else:
        #         nextButton.color = (172, 164, 255)
        #     # Take 3에서 1번 버튼 클릭시
        #     if selectbutton1.isOver(pos):
        #         selectbutton1.color = (255, 255, 0)
        #     else:
        #         selectbutton1.color = (172, 164, 255)
        #     # Take 3에서 2번 버튼 클릭시
        #     if selectbutton2.isOver(pos):
        #         selectbutton2.color = (250, 250, 0)
        #     else:
        #         selectbutton2.color = (172, 164, 255)