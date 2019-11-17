# 모듈 불러오기
import pygame
import math

# 초기화 시키기
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
acc = [0, 0]


# 이미지 가져오기
player = pygame.image.load("drawable/run.png")


keys = [False, False, False, False]
playerpos = [30, 320]

# 화면이 계속 보이게 하기


while True :
    # 화면을 깨끗하게 하기
    screen.fill((0,0,0))        # ( R,G,B )

    # 플레이어 마우스 바라보게 만들기
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1]+32), position[0] - (playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width//2, playerpos[1] - playerrot.get_rect().height//2)
    screen.blit(playerrot, playerpos1)


    # 화면 다시 그리기
    pygame.display.flip()

    # 게임 종료하기
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

        # QUIT 은 X 이다. 이것을 누르면 이 창을 종료한다.
        if event.type == pygame.QUIT :
            pygame.quit()
            exit(0)
        # 플레이어 움직이기
        if keys[0]:
            playerpos[1] = playerpos[1] - 5
        elif keys[2]:
            playerpos[1] = playerpos[1] + 5
        elif keys[1]:
            playerpos[0] = playerpos[0] - 5
        elif keys[3]:
            playerpos[0] = playerpos[0] + 5