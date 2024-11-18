"""
int -> 1 2 3 4 -1 -2 -3
float -> 1.5 2.5 3.3 4.6
string -> "Hello", "123"
boolean -> True / False

lenght
"""


# phương thức để đếm số phần tử trong list
# print(len(list))
# range(start, end, step)
"""
nếu step > 0 -> end = end - 1
nếu step < 0 -> end = end + 1
Mặc định:
Start = 0
end = 1

Nguyen: 10 9 8 7 6 5 4
Nhân: 9 8 7 6 5 4
An: 

range -> cho ra 1 kết quả là 1 list các dãy số

"""

# tạo 1 input để người nhập giá trị
# áp dụng vòng lặp for tìm kiếm giá trị đó trong list
# Nếu có in ra thứ tự của giá trị đó trong list
# nếu không thì in ra không tìm thấy

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hello world", "python", "C++", "Java", "C#"]
# x = input("nhập giá trị cần tìm: ")  
# found = 0 


# tạo 1 input để người nhập 1 ký tự cần tìm
# áp dụng vòng lặp for đếm số ký tự xuất hiện trong string
# Ví dụ: nhập vào input chữ h -> chữ h xuất hiện 5 lần
# string = "hello world welcome to python. latest version python is 3.12.7"

# character = input("nhập ký tự cần tìm: ")
# count = 0
# for i in string:
#     if i == character:
#         count += 1

# if count == 0:
#     print(f"Không tìm thấy ký {character} trong string")
# else:
#     print(f"Có {count} ký tự {character} trong string")
    
"""
Viết một chương trình yêu cầu người dùng nhập vào một số nguyên dương n. 
Chương trình sẽ sử dụng vòng lặp while để tính tổng các số từ 1 -> n

ví dụ nhập vào n = 5
tính 1 + 2 + 3 + 4 + 5



Bài tập: Đoán số

Viết một chương trình yêu cầu người dùng đoán một số bí mật từ 1 đến 100. 
Chương trình sẽ tiếp tục cho phép người dùng đoán cho đến khi đoán đúng.
Giới hạn đoán là 5 lần

Yêu cầu:
	1.	Tạo 1 biến chứa 1 số ngẫu nhiên từ 1 đến 100
	2.	Sử dụng vòng lặp while để lặp lại quá trình yêu cầu đoán cho đến khi người dùng nhập đúng số bí mật.
	3.	Sau mỗi lần đoán, nếu người dùng đoán sai, thông báo cho họ biết nếu số bí mật lớn hơn hay nhỏ hơn số họ vừa đoán.
	4.	Khi người dùng đoán đúng, hiển thị thông báo chúc mừng và kết thúc chương trình.

Gợi ý:
	•	Hàm input() sẽ giúp bạn lấy dữ liệu nhập từ người dùng.

"""

lucky_number = 50
count = 0
while count < 5:
	guess_number = int(input("Nhập số bí mật: "))
	if guess_number == lucky_number:
		print("Chúc mừng, bán đoán đúng")
		break
	elif guess_number < lucky_number:
		print("Số bí mật lớn hơn")
	else:
		print("Số bí mật nhỏ hơn")
	count += 1







