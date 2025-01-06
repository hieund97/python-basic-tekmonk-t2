"""
Kiểu dữ liêu:
Boolean - True/ False
string - "Hello"
integer - số nguyên: -1 2 3 4 5 -5 -6
float - Số thực: 1.5 2.5 3.3
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hello world", "python", "C++", "Java", "C#"]

for

while
"""

"""
Part I: 
Full name - Viết chương trình cho người dùng nhập vào tên và họ rồi in ra tên đầy đủ của họ
Capitalize name - Viết chương trình chuyển những gì người dùng nhập vào thành chữ hoa
Square number - Viết chương trình cho người dùng nhập vào một số rồi in ra bình phương của số vừa nhập

Part II:
3 to 12 sequence - Viết chương trình in ra một dãy số từ 3 đến 12 (Tối đa 5 dòng code)
0 to n sequence - Viết chương trình in ra một dãy số từ 0 đến n, n > 0 do người dùng nhập vào
0 to n odd sequence - Viết chương trình in ra một dãy số lẻ từ n đến 0, n > 0 do người dùng nhập vào

Part III:
Larger than 13 - Viết chương trình cho người dùng nhập vào một số rồi in ra cho biết số này có lớn hơn 13 hay không
Even check - Viết chương trình cho người dùng nhập vào một số rồi in ra cho biết số này có phải là số chẵn hay không
Days of month - Viết chương trình cho người dùng nhập vào một tháng trong năm và in ra số ngày của tháng này

Part IV:
+ Registration simulation - Viết chương trình cho phép người dùng đăng ký tài khoản. Bằng cách hỏi 3 thông tin:  
tên đăng nhập, mật khẩu, email

+ Registration simulation v2 - Dựa vào chương trình đã tạo ở bài 1, tạo thêm một mục là “nhập lại mật khẩu” 
ô “mật khẩu” và ô “nhập lại mật khẩu” phải giống nhau, nếu khác nhau báo lỗi và bắt người dùng nhập lại.

+ Registration simulation v3 - Tiếp tục làm việc với chương trình  đã tạo ở bài 1,2 kiểm tra xem email 
người dùng nhập vào có phải là 1 email hợp lệ không (có @, có dấu chấm...),  độ dài tối thiểu của mật khẩu phải 
lớn hơn 8 ký tự, bao gồm cả chữ vào số. nếu không có yêu cầu người dùng nhập lại


"""

user_name = input("Nhập tên đăng nhập: ")
password = input("Nhập mật khẩu: ")
email = input("Nhập email: ")

while "@" not in email and "." not in email:
    print("Email không hợp lệ")
    email = input("Nhập email: ")

confirm_password = input("Nhập lại mật khẩu: ")
# khi mà confirm_password không bằng password => print(lỗi) => viết lại input confirm_password để nhập lại
while confirm_password != password:
    print("Mật khaus không khợp")
    confirm_password = input("Nhập lại mật khẩu: ")





