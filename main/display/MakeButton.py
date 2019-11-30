import pygame

class MakeButton():
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

    # def redrawWindow():
    #     nextButton.draw(screen, (0, 0, 0))
    #     selectbutton1.draw(screen, (0, 0, 0))
    #     selectbutton2.draw(screen, (0, 0, 0))