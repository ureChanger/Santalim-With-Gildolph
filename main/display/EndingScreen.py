import pygame
import os
import main.item.ConversationItem

class endingScene:

    def __init__(self):
        pygame.init()
        os.chdir(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((255, 255, 255))
        self.convItem = main.item.ConversationItem.ConversationItem()
        self.takeCheck = 1
        self.run = True

    def endPresent(self):
        self.screen.fill((255, 255, 255))
        self.gift = pygame.image.load('drawable/gift.png')
        self.gift = pygame.transform.scale(self.gift, (150, 150))
        self.screen.blit(self.gift, (240, 200))

    def endingmsg(self):
        self.packP = pygame.image.load('drawable/packingPresent.jpg')
        self.screen.blit(pygame.transform.scale(self.packP, (640, 480)), (0, 0))
        font = pygame.font.Font("drawable/seoul_hangang.ttf", 20)
        self.text1 = font.render(self.convItem.item[11], True, ((0, 0, 0)))
        self.screen.blit(self.text1, (200, 140))
        self.text2 = font.render(self.convItem.item[12], True, ((0, 0, 0)))
        self.screen.blit(self.text2, (200, 175))
        self.text3 = font.render(self.convItem.item[13], True, ((0, 0, 0)))
        self.screen.blit(self.text3, (200, 210))
        self.text4 = font.render(self.convItem.item[14], True, ((0, 0, 0)))
        self.screen.blit(self.text4, (200, 245))
        self.text5 = font.render(self.convItem.item[15], True, ((0, 0, 0)))
        self.screen.blit(self.text5, (200, 280))
        self.text6 = font.render(self.convItem.item[16], True, ((0, 0, 0)))
        self.screen.blit(self.text6, (200, 315))
        self.text7 = font.render(self.convItem.item[17], True, ((0, 0, 0)))
        self.screen.blit(self.text7, (200, 350))

    def endingRun(self):

        while self.run:
            pygame.display.update()
            pygame.display.set_caption("SNOW RUN")

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.takeCheck == 1:
                        self.endPresent()
                        self.takeCheck += 1
                    elif self.takeCheck == 2:
                        self.endingmsg()
                        self.takeCheck += 1



if __name__ == '__main__':
    end = endingScene()
    end.endingRun()