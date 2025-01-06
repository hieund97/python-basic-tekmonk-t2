"""
part1:
Nguyên: 3p
Nhân: 5p
An: 9p

Init color list - Viết chương trình chứa 1 list chứa ít nhất 3 string đại diện cho 3 màu, 
ví dụ: “blue”, “red", “teal", “green”
Print color list - Sử dụng lại list ở bài số 1, viết chương trình hiện ra tất cả các màu trong list
Ví dụ:
Our color list:
blue, red, teal, green

Create - Sử dụng lại list ở bài 1, viết chương trình hỏi người dùng muốn thêm màu gì vào list, 
sau khi người dùng nhập, thêm màu này vào cuối list
Ví dụ:
Our color list:
blue, red, teal, green

Enter a new color: orange
Our new color list: 
blue, red, teal, green, orange


Part2:
Nguyên 5p
Nhân: 6p
An: 12p

Create (2) - Sử dụng lại list ở bài số 1, cho phép người dùng xem Nội dung của 1 màu theo vị trí:
Ví dụ:
Enter position: 2
Color at position 2: red

Delete - Sử dụng list ở bài 1, viết chương trình hỏi người dùng muốn xoá màu nào trong danh sách, 
nếu người dùng nhập số, tự động thực hiện xoá theo vị trí,
nếu người dùng nhập chữ, tự động thực hiện xoá theo tên màu sắc

Part3: 
Nguyên: 3p
Nhân: 8
An: 13p

Search number in list - 
Tạo 1 list chứa trên 5 số nguyên không cách đều, sau đó yêu cầu nhập vào một số, 
thực hiện tìm kiếm số mà người dùng nhập vào trong list vừa khởi tạo, 
trả lời câu hỏi: “Số này có trong list không, nếu có thì có đứng thứ mấy trong dãy?”

Ví dụ: Giả sử list cho sẵn là 5, 1, 8, 92, -1, 30
Lần chạy 1:
Enter a number: -99
Not found in our list
Lần chạy 2:
Enter a number: 8
Found, position 8


Part 4:
Nguyên: 14p
Nhân: 20p

Sum number in list - Tạo 1 list chứa trên 5 số không cách đều. Tính tổng dãy này và in ra kết quả.
Thực hiện bài này bằng 2 cách, dùng hàm sum() và không dùng hàm sum() .
Ví dụ: Giả sử list cho sẵn là 5, 1, 8, 92, -1, 30
Sum of all numbers: 135

Sum number in list (2) - Thực hiện lại bài trên với danh sách các số nhập từ người dùng, 
các số cách nhau bởi dấu cách ,
Ví dụ:
Enter a list of numbers, separated by ,: 5 12 6 61 124
Sum of all entered numbers: 208


Part5:
Nguyên: 4p
Nhân: 11p

Filter even - Tạo 1 list chứa trên 5 số không cách đều.
Lọc ra tất cả những số chẵn trong dãy này và in ra màn hình. 
Ví dụ: Giả sử list cho sẵn là 5, 1, 8, 92, 7, 30
All even numbers: 8, 92, 30
Sequence input - Thực hiện lại bài trên với danh sách các số nhập từ người dùng, 
các số cách nhau bởi dấu phẩy ‘,’
Ví dụ:
Enter a list of numbers, separated by ‘,’: 5, 12, 6, 61, 124
All even numbers from entered list: 12, 6, 124

Part6:
Nguyên: 5p
Nhân: 4p


init list of district names and population - 
Cho danh sách các quận của một thành phố cùng diện tích cũng như dân số của các quận này như bảng
Tạo 2 list:
List đầu tiên, theo thứ tự từ trên xuống dưới, bao gồm tên của các quận trong bảng
List thứ hai, theo thứ tự từ trên xuống dưới, bao gồm dân số của các quận trong bảng
Search max n min population - Ở trong list dân số của các quận trong bảng, tìm ra chỉ số của quận có số dân lớn nhất và quận có dân số ít nhất
From district index to name - Từ chỉ số của quận có dân số đông nhất và ít nhất, in ra tên của quận có số dân lớn nhất và số dân ít nhất


Quận       Dân số   Diện tích
ST         117,43   150,300 
BĐ         9.224    247,100   
BTL        43.35    333,300    
CG         12.04    266,800  
ĐĐ         9.96     420,900 
HBT        10.09    318,000  



part7: 
Nguyên: 5p
Nhân: 12p

Population density - Ở bảng bài số 12, tạo ra 1 list chứa diện tích của từng quận, theo thứ tự từ trên xuống dưới
Từ list chứa diện tích và list chứa dân số của các quận, tạo ra 1 list mới chứa mật độ dân cư 
của các quận từ trên xuống. Công thức: Mật độ dân cư = Dân số / diện tích
Average population density - Từ list ở bài 15, tính mật độ dân cư trung bình của các quận. Công thức: Mật độ dân cư trung bình = Tổng mật độ dân cư /  tổng số quận



Part:8
nguyên: 8p
Nhân: 11p
Init high score list - Tạo 1 list, chứa các số nguyên, đại diện cho điểm cao (High scores) của người chơi

Print high score list - Hiện ra danh sách điểm cao (chưa cần phải đúng thứ tự từ trên xuống dưới ngay):
Ví dụ:
High scores:
1. 78
2. 56
3. 67
4. 45


New high score - Viết chương trình thêm điểm mới của người chơi (chưa cần phải đúng thứ tự từ trên xuống dưới ngay)
Ví dụ:
High scores:
1. 78
2. 56
3. 67
4. 45
Enter your new score: 70
High scores:
1. 78
2. 56
3. 67
4. 45
5. 70


Part 9:

Thực hiện lại part 8 với các điểm từ cao đến thấp VÀ chỉ hiện ra điểm của 5 người điểm cao nhất
High Score: 45, 67, 56, 78, 100, 213, 44, 34, 55, 75, 81, 22, 11, 33, 66, 77, 88, 99, 100, 200

Tìm điểm trong high_score
+ Nhập điểm cần tìm và in ra thứ hạng của điểm nếu điểm đó tồn tại
+ nếu điểm không tồn tại in ra màn hình "Không tìm thấy điểm trong danh sách"

"""


list = [
    9.224,
    43.35,
    12.04,
    9.96,
]

max_dan_so = max(list)