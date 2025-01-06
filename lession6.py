dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

#           0          1          2          3          4
list = ["value1", "value2", "value3", "value4", "value5"]

list[1] = "value2"




danh_sach = {
    "name": "Nhân", #1
    "age": 16, #2
    "address": "Hanoi" #3
}


# để truy cập vào các phần tử của dictionary thì chúng ta phải truy cập theo key chứ không dùng index
# vì dictionary không có index

# Nguyên: Nhân
# Nhân: Nhân
# Nhân: Nhân


# Xin chào tôi tên là Nhân, năm nay tôi 16 tuổi và tôi ở Hà Nội

# print(f"Xin chào tôi tên là {danh_sach['name']}, năm nay tôi {danh_sach['age']} tuổi và tôi ở {danh_sach['address']}")

# # print(danh_sach["address"])

# # lấy được toàn bộ key trong dictionary
# print(danh_sach.keys())

# # lấy toán bộ value trong dictionary
# print(danh_sach.values())

# # lấy toàn bộ cặp key và value
# print(danh_sach.items())


# list_order = {
#     "name": "Laptop Dell",
#     "price": 1200,
#     "quantity": 2,
# }

# # từ list_order trên, tính ra tổng số tiền bằng price * quantity và in ra câu sau
# # Tổng hoá đơn Laptop Dell có giá là {tổng tiền} - Đơn giá: 1200$ - Số lượng: 2 cái

# total_price =  list_order["price"] * list_order["quantity"]

# print(f"Tổng hoá đơn {highest_score_name} có giá là {total_price} - Đơn giá: {list_order['price']}$ - Số lượng: {list_order['quantity']} cái")


"""

Cho một dictionary lưu số điểm của các học sinh trong lớp:

scores = {
    "Hùng": 85,
    "Lan": 92,
    "Minh": 78,
    "Hà": 65,
    "Tùng": 90
}

	1.	Tìm học sinh có điểm cao nhất và thấp nhất.
	2.	Tính điểm trung bình của cả lớp.
 
Gợi ý:
    Dùng vòng lặp for với scores.items()

"""

scores = {
    "Hùng": 85,
    "Lan": 92,
    "Minh": 78,
    "Hà": 65,
    "Tùng": 90
}


highest_score_name = ""
highest_score = 0
lowest_score_name = ""
lowest_score = float("inf")

for key, value in scores.items():
    if value > highest_score:
        highest_score = value
        highest_score_name = key
    if value < lowest_score:
        lowest_score = value
        lowest_score_name = key
        
avg_score = sum(scores.values()) / len(scores)


# print(f"Bạn {highest_score_name} có điểm cao nhất là {highest_score}")
# print(f"Bạn {lowest_score_name} có điểm thấp nhất là {lowest_score}")
# print(f"Điểm trung bình của tất cả học sinh là: {avg_score}")

"""
Bài 7: Sắp xếp dictionary

Cho một dictionary lưu số lượng bán hàng của các sản phẩm:

sales = {
    "Laptop": 120,
    "Phone": 200,
    "Tablet": 50,
    "Monitor": 75
}

	1.	Sắp xếp các sản phẩm theo số lượng bán giảm dần và in kết quả.
	2.	Sắp xếp các sản phẩm theo tên (key) theo thứ tự bảng chữ cái.

"""
# sorted(list, key, reverse = True)

#cach 1:

sales = {
    "Laptop": 120,
    "Phone": 200,
    "Tablet": 50,
    "Monitor": 75
}

def sorted_by_value(value):
    return value[1]

sorted_sale = sorted(sales.items(), key=sorted_by_value, reverse=True)
# print(sorted_sale)



# list

#           0          1          2          3          4
list = ["value1", "value2", "value3", "value4", "value5"]


# thêm 1 phần tử vào cuối cùng của list:
# list.append("value6")
# list.remove('value4')
# list.pop(3)
list.insert(3, "value4-3")
len(list) # đếm số phần tử
# print(list)

sales = {
    "Laptop": 120,
    "Phone": 200,
    "Tablet": 50,
    "Monitor": 75
}

sales['mouse'] = 20
sales['Phone'] = 150



# print(sales)

"""
Set không phải là kiểu dữ liệu

Set là 1 tập hợp không có index và không có giá trị trùng

set giống dictionary nhưng không có key:value

set = {"hello", "hi", 1,2,3,4}



"""

# set = {"hello", "hi", 1,2,3,4,4,4,4,4,4,4,4}
# print(set)

"""
Bài 1: Xử lý thông tin học sinh

Cho danh sách học sinh và thông tin điểm của họ:

students = [
    {"name": "Nguyen Van A", "class": "10A", "scores": [8, 7.5, 9]},
    {"name": "Tran Thi B", "class": "10B", "scores": [6, 8, 7]},
    {"name": "Le Van C", "class": "10A", "scores": [9, 8.5, 10]},
    {"name": "Pham Thi D", "class": "10C", "scores": [7, 6.5, 8]}
]

	1.	Tính điểm trung bình của mỗi học sinh và thêm trường "average" vào từng dictionary trong danh sách.
	2.	Lọc ra các học sinh thuộc lớp "10A".
	3.	Tạo một set chứa tất cả các lớp trong danh sách. VD: set = {"10A", "10B", "10C"}


"""


students = [
    {"name": "Nguyen Van A", "class": "10A", "scores": [8, 7.5, 9]},
    {"name": "Tran Thi B", "class": "10B", "scores": [6, 8, 7]},
    {"name": "Le Van C", "class": "10A", "scores": [9, 8.5, 10]},
    {"name": "Pham Thi D", "class": "10C", "scores": [7, 6.5, 8]}
]

list_10A_student = []
set = set() # khởi tạo 1 set rỗng

for student in students:
    student['average'] = sum(student['scores']) / len(student['scores'])
    if student['class'] == "10A":
        list_10A_student.append(student['name'])
    set.add(student['class'])


# print(list_10A_student)
# print(set)
# print(students)

"""
Kết hợp danh sách học sinh và môn học

Cho danh sách học sinh và danh sách môn học:

students = ["Nguyen Van A", "Tran Thi B", "Le Van C", "Pham Thi D"]
subjects = ["Math", "English", "History", "Physics"]

	1.	Tạo một dictionary với mỗi học sinh là một key, giá trị là một set chứa các môn học mà học sinh học.
Output ví dụ:

{
    "Nguyen Van A": {"Math", "English"},
    "Tran Thi B": {"History", "Physics"},
    ...
}


"""

students = ["Nguyen Van A", "Tran Thi B", "Le Van C", "Pham Thi D"]


subjects = ["Math", "English", "History", "Physics"]
    
dict = {}

{
    "Nguyen Van A": {"Math", "English"},
    "Tran Thi B": {"History", "Physics"},
}

dict = {}

for student in students:
    if student == "Nguyen Van A":
        for sub in subjects:
            if sub == "Math":
                dict[student] = {sub}
            elif sub == "English":
                dict[student] = {sub}
    elif student == "Tran Thi B":
        for sub in subjects:
            if sub == "History":
                dict[student] = {sub}
            elif sub == "Physics":
                dict[student] = {sub}
        

"""
Phân tích dữ liệu điểm thi

Cho danh sách học sinh và điểm thi của họ:

data = [
    {"name": "Nguyen Van A", "scores": {"Math": 8, "English": 7.5, "Physics": 9}},
    {"name": "Tran Thi B", "scores": {"Math": 6, "English": 8, "Physics": 7}},
    {"name": "Le Van C", "scores": {"Math": 9, "English": 8.5, "Physics": 10}},
    {"name": "Pham Thi D", "scores": {"Math": 7, "English": 6.5, "Physics": 8}}
]

	1.	Tính điểm trung bình của mỗi học sinh, lưu vào dictionary theo cấu trúc:

{
    "Nguyen Van A": 8.17,
    "Tran Thi B": 7.0,
    ...
}


	2.	Tạo một set chứa tất cả các môn học có trong danh sách.
	3.	Tìm học sinh có điểm trung bình cao nhất.

"""
