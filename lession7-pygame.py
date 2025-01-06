import pygame, sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rắn săn mồi")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
GREEN = (0, 255, 0)

screen.fill(AQUA)
# vẽ hình chữ nhật
                                #x  y    dai  rong
pygame.draw.rect(screen, RED, [300, 400, 200, 150])

# vẽ hình tròn
#                                      x   y    ban kinh
# pygame.draw.circle(screen, WHITE, [400, 300], 50)

# vẽ hình đa giác

pygame.draw.polygon(screen, GREEN, [[300, 400], [400, 300], [500, 400]])
pygame.draw.rect(screen, BLUE, [380, 500, 50, 50])

pygame.display.update()

while True:
    for event in pygame.event.get(): # tác dụng bắt toàn bộ sự kiện
        if event.type == pygame.QUIT: # kiểm tra loại sự kiện
            pygame.quit()
            sys.exit()