import pygame
import os
import main.item.ConversationItem

# 파이게임 초기화
pygame.init()
# 윈도우 창의 크기 설정
screen = pygame.display.set_mode((640, 480))

convItem = main.item.ConversationItem.ConversationItem()

os.chdir(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
back = pygame.image.load("drawable/pooh.jpg")
screen.blit(pygame.transform.scale(back, (640, 480)), (0, 0))

class makeButton():
    def __init__(self, color, x , y, width, height, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline = None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont(None , 60)
            text = font.render(self.text, 3 , (0, 0, 0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y +(self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def redrawWindow():
    nextButton.draw(screen, (0, 0, 0))


nextButton = makeButton((255, 205, 5), 560, 380, 50, 50, ">")
run = True

# Take 1)
font = pygame.font.Font(None, 40)
text1 = font.render(convItem.item[0] , True,(255, 255 ,255))
text2 = font.render(convItem.item[1], True, (255, 255, 255))
screen.fill((0, 0, 0))
screen.blit(text1, (100, 300))
screen.blit(text2, (100, 350))

# Take 2)
# screen.fill((0, 0, 0))
# cutie2 = pygame.image.load("drawable/cutie2.png")
# screen.blit(cutie2, (100, 200))
# pygame.draw.rect(screen, (255, 255, 255), [50, 360, 500, 80], 3)
# text3 = font.render(convItem.item[2], True, (255, 255, 255))
# screen.blit(text3, (120, 390))

# Take 3)
# screen.fill((0, 0, 0))
# cutie3 = pygame.image.load("drawable/cutie3.png")
# screen.blit(cutie3, (300, 200))

while run:
    redrawWindow()
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
            if nextButton.isOver(pos):
                print("nextButton was clicked !")
            screen.fill((0, 0, 0))
            cutie2 = pygame.image.load("drawable/cutie2.png")
            screen.blit(cutie2, (100, 200))
            pygame.draw.rect(screen, (255, 255, 255), [50, 360, 500, 80], 3)
            text3 = font.render(convItem.item[2], True, (255, 255, 255))
            screen.blit(text3, (120, 390))

        if event.type == pygame.MOUSEMOTION:
            if nextButton.isOver(pos):
                nextButton.color = (255, 255, 0)
            else:
                nextButton.color = (172, 164, 255)