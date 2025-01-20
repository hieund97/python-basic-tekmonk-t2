import pygame, sys, random

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake game")

font = pygame.font.SysFont("monospace", 50)

WHITE =  (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)


list_word = ["PYTHON", "JAVA"]
word = random.choice(list_word)


guess = []

hang_man_status = 0

images = []
for i in range(7):
    image = pygame.image.load(f"hangman{i}.png")
    images.append(image)


# Bước 1: Tạo font
# Bước 2: Render ra chữ
# Bước 3: Viết chữ lên màn hìn
def draw_title():
    title = font.render("HANGMAN", True, BLACK)
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, 50 ))
    
def draw():
    x = 100
    screen.blit(images[hang_man_status], (100, 100))
    for i in guess:
        char = font.render(i, True, BLACK)
        screen.blit(char, (x, 400))
        x += 50

    
def draw_lines():
    x = 100
    for i in word:
        if i in guess:
            char = font.render(i, True, BLACK)
        else:
            char = font.render("_", True, BLACK)
        screen.blit(char, (x, 300))
        x += 50


while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha(): #kiểm tra phím là chữ hay không
                #chuyển về thành chữ viết hoa:
                letter = event.unicode.upper()
                #kiểm tra nếu mà chữ này chưa được đoán (Không nằm trong biến guess)
                if letter not in guess:
                    guess.append(letter)
            
    

    draw_title()
    draw()
    draw_lines()
    pygame.display.update()
