"""
Câu lệnh print

input đầu vào -> xử lý logic -> xử lý output đầu ra

sep và end

sep mặc định là dấu khoảng trắng blank space

end mặc định là ký tự xuống dòng \n

f string

ten bien = gia tri

+ Quy tắc đặt tên biến:
    + Không chứa ký tự đặc biệt (#, %, &, -, ...)
    + Không chưa ký tự số ở ký tự đầu tien (1Hello)
    + Không được chứa các ký tự liên quan đến lập trình (if, for, while, and, or, not)
    + Biến số phân biệt chữ hoa và chữ thường
    

Yêu cầu: Tính chu vi hình tròn biết đường kính là 10cm, số Pi là 3.14
    + Đặt 2 biến duong_kinh và so_Pi
    + Tính chu vi hình tròn
    + In ra chu vi hình tròn: Chu vi hình tròn có đường kính là 10 bằng: 31,4


"""

# nhiet_do_soi = 101
# Nhiet_Do_Soi = 102
# ten_hoc_sinh = "Xuan"

# print(f"Bạn {ten_hoc_sinh} thực hành thí nghiệm đo đạc nhiệt độ sôi của nước")
# print(f"Bạn {ten_hoc_sinh} đo được khi đun khoảng 10p là {nhiet_do_soi} độ C")
# print(f"{nhiet_do_soi} độ C tương ứng với 200 độ F")
# print(f"{nhiet_do_soi} độ C có thể khiến nước bay hơi")
# print(Nhiet_Do_Soi)


# duong_kinh = 10
# so_Pi = 3.14
# chu_vi = duong_kinh * so_Pi
# print(f"Chu vi hình tròn có đường kính là {duong_kinh} bằng: {chu_vi}")


"""
Kiểu dữ liệu:
+ Số nguyên: integer - int - VD: 1, 2, 3
+ Số thực: float - float - VD: 1.5 , 2.5, 3.5
+ Chuỗi: String - str - VD: "Hello", "World", "Python"
+ Kieu bool: boolean - bool - VD: True, False

Toán tử sử dụng trong python
+ - * /

Chia lấy phần dư: %
Chia lấy phần nguyên: //
Luỹ thừa: **

Ép kiểu


"""

# x = "10" # ép kiểu từ string -> int hoặc float
# y = 100
# z = float(x) + y
# print(z)


# duong_kinh = float(input("Nhập đường kính vào đây: ")) # mặc định kiểu dữ liêu là string
# so_Pi = 3.14
# chu_vi = duong_kinh * so_Pi
# print(f"Chu vi hình tròn có đường kính là {duong_kinh} bằng: {chu_vi}")

"""
Cho công thức z = a^2 + b^2 / 2*a*b
yêu cầu: 
nhập giá trị số a và b từ bàn phím
In ra kết quả của căn bậc 2 của z

+ import math -> sqrt

"""
#  


"""
đếm số ký tự của string len(string)


string[start:end:step]

nếu step > 0 <-> end = end - 1
nếu step < 0 <-> end = end + 1
mặc định start = 0
mặc định step = 1
mặc định end = len(string)
1. AN
2. Xuân
3. Nhân

"""

#An
# print(string[1:15:4])

# # xuân | h dctt sr
# print(string[::5])

# nhân
# print(string[12:3:-1])


"""
string = "hello world welcome to python. latest version python is 3.12.7"


từ đoạn string trên in ra ký tự đầu tiên và ký tự cuối cùng của string


"""
#--->
# 0 -> len(string) - 1


                                                                
                                                                    #<----
                                                    #-len(string) <--- -1
# string = "hello world welcome to python. latest version python is 3.12.7"

# print(string[-len(string)])


# a = int(input("Nhập start: "))
# b = int(input("Nhập end: "))
# c = int(input("Nhập step: "))

# print(string[a:b:c])
#         0123456
string = "TEKMONK"
#         -5-4-3-2-1


"""
BTVN:
Bài tập 1: Tìm vị trí của ký tự
Viết chương trình nhập vào một chuỗi và một ký tự từ người dùng. Sử dụng index của string để tìm vị trí xuất hiện đầu tiên của ký tự đó trong chuỗi.


"""

"""
Kiểu dữ liệu:
integer - int: 1 2 3 4 5
float - Số thực: 0.1 1.5 2.5
string - str: "Hello" "World"



x = 10 # int
y = 20 # int
z = "100" #str
t = 10.5 # float

sum1 = x + y # 30
sum2 = x + z # 10100
sum3 = x + t # lỗi - 20.5

"""

# x = 10 # int
# y = 20 # int
# z = "100" #str
# t = 10.5 # float

# sum1 = x + y # 30
# sum2 = x + int(z) # 110
# sum3 = x + t # lỗi - 20.5

# print(sum1)
# print(sum2)
# print(sum3)

