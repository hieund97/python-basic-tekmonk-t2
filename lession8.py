"""
Hàm không có tham số
Hàm có tham số
Hàm có giá trị trả về
Hàm không có giá trị trả về

Cho 1 dictionary lưu giá trị giá của trái cây:

list_fruit = {
    "apple": 10000,
    "banana": 20000,
    "orange": 30000,
    "grape": 40000
}

Viết 1 chương trình tính toán giá tiền gồm 3 chức năng

Chức năng 1: hiển thị menu hoa quả:
Output: 
MENU:
Apple - 10000đ/kg
Banana - 20000đ/kg
Orange - 30000đ/kg
Grape - 40000đ/kg

Chức năng 2: Chức năng mua hàng:
+ Tạo 1 input nhập tên loại trái cây
+ Kiểm tra trái cây có trong menu hay không
+ Nếu có thì nhập số lượng trái cây cần mua
+ Tính ra số tiền bằng số lượng (kg) * giá
+ In ra tổng hoá đơn

Chức năng 3: Thoát

Chức năng 1 và 2 tạo ra 2 hàm riêng cho 2 chức năng


cho 1 list ngẫu nhiên các số như sau:
random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
Yêu cầu: không dùng hàm max của list, tạo ra 1 hàm tìm số lớn nhất trong list đó
"""


# list_fruit = {
#     "apple": 10000,
#     "banana": 20000,
#     "orange": 30000,
#     "grape": 40000
# }

# def show_menu(list_fruit):
#     for key, value in list_fruit.items():
#         print(f"{key} - {value}đ/kg")

# def buy_fruit(list_fruit):
#     fruit_name = input("Nhập tên hoa quả cần mua: ")
#     if fruit_name in list_fruit:
#         quantity = float(input("Nhập số lượng cần mua: "))
#         total_price = quantity * list_fruit[fruit_name]
#         print(f"Tổng tiền cho {quantity}kg - {fruit_name} là: {total_price}đ")
#     else:
#         print(f"Loại {fruit_name} đã hết hàng")

# while True:
#     option = int(input("Nhập lựa chọn: "))
    
#     if option == 1:
#         show_menu(list_fruit)
#     elif option == 2:
#         buy_fruit(list_fruit)
#     else:
#         print("Thoát chương trình")
#         break

#SCOPE

"""
Phạm vi  LEGB Rule 

L - Local - Phạm vi cục bộ/nội bộ
E - Enclosing scope - Phạm vi bao quanh
G - Global - Phạm vi toàn cục
B - Built-in - Phạm vi bị ghi đè

"""
        
def ham_demo():
    x = 10  # Biến cục bộ
    print("Bên trong hàm:", x)

ham_demo()
# print(x)  # Lỗi, vì x chỉ tồn tại bên trong hàm 

def ham_ngoai():
    x = 20  # Biến thuộc phạm vi bao quanh
    def ham_trong():
        print("Bên trong hàm lồng:", x)
    ham_trong()

ham_ngoai()

def ham_ngoai():
    x = 20
    def ham_trong():
        nonlocal x
        x = 50  # Thay đổi biến của hàm bao quanh
    ham_trong()
    print("Giá trị x sau khi thay đổi:", x)

ham_ngoai()  


x = 100  # Biến toàn cục

def ham_demo():
    print("Biến toàn cục bên trong hàm:", x)

ham_demo()
print("Biến toàn cục bên ngoài hàm:", x)

x = 100

def thay_doi_global():
    global x
    x = 200

thay_doi_global()
print("Giá trị x sau khi thay đổi:", x)

# print(len([1, 2, 3]))  # len là hàm tích hợp sẵn của Python

# Trùng tên với hàm built-in
# print(len([1, 2, 3]))  # Lỗi, vì len đã bị ghi đè

"""
cho 1 biến toàn cục y = 100, 
viết 1 hàm thay đổi giá trị của biến toàn cục y và in ra giá trị sau khi thay đổi
"""

# import lession7 as ls7 # alias

from lession7 import sum, subtract

a = int(input("nhập số a: "))
b = int(input("nhap số b: "))

print(sum(a, b))
print(subtract(a, b))


"""
Tạo ra 1 module có chức năng kiểm tra số chẵn và số lẻ
Import vào file hiện tại sử dụng chức năng đó


Tạo chương trình tính điểm và xếp loại học sinh

Tạo thêm 1 module nhập thông tin học sinh
Tạo 1 module show thông tin học sinh
Tạo 1 module kiểm tra xếp loại học sinh
Điểm >= 8.5 và không có môn nào dưới 7, in ra "Xuất sắc".
Điểm từ 6.5 đến dưới 8.5 và không có môn nào dưới 5, in ra "Khá".
Điểm từ 5 đến dưới 6.5, in ra "Trung bình".
Điểm dưới 5 là Yếu



"""

"""
Ôn tập kiến thức


Kiểu dữ liệu:
Int
Float
String



List
[1,2,3,4,5,6]

Tuple
(1,2,3,4,5,6)


Dictionary

{
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    
}


set 

{1,2,3,4,5,6} - không có phần tử trùng lặp




Function
Scope
Module
Vòng lặp
Index - range


Coding marathon 

"""


# list = [
#     [1, 2, 3, 4, 5],
#     ['a', 'b', 'c', 'd', 'e'],
#     ["xin chào", "tạm biệt", "cảm ơn", "bạn", "rất nhiều"]
#     ['python', 'java', 'c++', 'c#', 'javascript']
# ]

# nếu step > 0 => end = end - 1
# nếu step < 0 => end = end + 1

# range(1,12,3) # 

# range(10,3,-1)

# for i in range(15, 1, -3):
#     if i == 6:
#         continue
#     print(i)


# break
# continue


# thế nào là hàm có giá trị trả về

def function_test(a, b, c = 10):
    return a + b + c


kq = function_test(3,4)
print(kq)