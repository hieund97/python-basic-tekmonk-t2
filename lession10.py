"""

Bài tập về nhà:

Đề bài: Quản lý danh sách hàng hóa điện tử
1.	Tạo một module có tên product_manager.py, chứa các hàm sau:
	+ add_product(product_list, name, price, quantity): Thêm một sản phẩm mới vào danh sách.
	•	Input: danh sách hàng hóa product_list (list), tên sản phẩm name (string), giá price (float), số lượng quantity (int).
	•	Output: Trả về danh sách đã được cập nhật.
	+ total_inventory_value(product_list): Tính tổng giá trị tồn kho (giá x số lượng) của tất cả sản phẩm.
	•	Input: danh sách hàng hóa product_list.
	•	Output: Trả về tổng giá trị tồn kho (float).
	+ find_most_expensive_product(product_list): Tìm sản phẩm có giá cao nhất.
	•	Input: danh sách hàng hóa product_list.
	•	Output: Trả về tuple gồm tên và giá của sản phẩm đó.
	+ search_product(product_list, name): Tìm kiếm sản phẩm theo tên.
	•	Input: danh sách hàng hóa product_list, tên sản phẩm name (string).
	•	Output: Trả về thông tin sản phẩm (name, price, quantity) nếu tìm thấy, hoặc chuỗi "Không tìm thấy sản phẩm" nếu không có.
 
2.	Trong file chính (main.py):
	+ Import module product_manager.
	+ Sử dụng vòng lặp for để:
	+ Nhập thông tin 5 sản phẩm (tên, giá, số lượng).
	+ Thêm từng sản phẩm vào danh sách bằng hàm add_product.
	+ In ra danh sách sản phẩm sau khi nhập.
	+ Gọi hàm total_inventory_value để tính và in tổng giá trị tồn kho.
	+ Gọi hàm find_most_expensive_product để tìm và in sản phẩm có giá cao nhất.
    + Cho phép người dùng nhập tên sản phẩm để tìm kiếm thông tin, sử dụng hàm search_product.


"""


"""
Sản phẩm cuối khoá:
Yêu cầu:
+ Sử dụng pygame để tạo ra 1 trò chơi của riêng em

Chủ đề:
+ Game snake (Rắn săn mồi)
+ Game hangman
+ Game tic tac toe
+ Game lật thẻ
+ 1 game các em tự sáng tạo

+ Đăng ký chủ đề
+ Các buổi còn lại dành thời gian để hoàn thành sản phẩm cuối khoá

+ An: Game hangman
+ Nhân: Game snake
+ Nguyên: Game balloon

+ Nhiệm vụ:
- AN: Vẽ được title, image, chữ của game hangman
- Nhân: vẽ được con rắn và cho con rắn chuyển động
- Nguyên: Tạo được các quả bóng rơi từ trên xuống, 
nếu rơi qua rìa cuối màn hình -> tiếp tục tạo quả bóng rơi từ trên xuống
"""

import pygame, sys, random

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Balloon game")

WHITE =  (255, 255, 255)

pygame.display.update()

list_balloon = []
FPS = 30
clock = pygame.time.Clock()

for i in range(5):
    x = random.randint(0, screen_width)
    y = random.randint(-100, -40)
    radius = random.randint(20, 40)
    speed =  random.randint(2, 7)
    
    list_balloon.append([x, y, radius, speed, WHITE])
    
def draw_balloon():
    for balloon in list_balloon:
        pygame.draw.circle(screen, balloon[4], (balloon[0], balloon[1]), balloon[2])
    
def update_balloon():
    for balloon in list_balloon:
        balloon[1] += speed


while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    draw_balloon()
    update_balloon()
    pygame.display.update()
    clock.tick(FPS)