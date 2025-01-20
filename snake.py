import pygame, sys, random

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake game")

WHITE =  (255, 255, 255)

pygame.display.update()

FPS = 12
clock = pygame.time.Clock()

x = screen_width // 2
y = screen_height // 2
x_change = 0
y_change = 0
snake_size = 10

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # sự kiện nhấn phím
            if event.key == pygame.K_LEFT: # kiểm tra loại phím bấm
                x_change = -snake_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_size
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_size
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_size
                
    x += x_change
    y += y_change
    
    pygame.draw.rect(screen, WHITE, [x, y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(FPS)