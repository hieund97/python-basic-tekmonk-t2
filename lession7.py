# tiếp tục làm với list, dictionary, set


# list = ['value1', 'value2', 'value3', 'value4', 'value5']
# set = {'value1', 'value2', 'value3', 'value4', 'value5'}
# tuple = ('value1', 'value2', 'value3', 'value4', 'value5')

"""
list = [1,124,6,124,345,126,745,12,435,7,3,9,91,21,657,12,512,56723,124124,62]

Với list ở trên ( không dùng hàm max và sum)
+ tìm số lớn nhất trong list 
+ Tính tổng của list


sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 25, 'e': 15}
in key có value lớn nhất trong dictionary
kết quả mong muốn: key d có value lớn nhất bằng 25

cho 1 list lồng nhau như sau:

big_list = [
    [1,2,3,4,5,100],
    [12,54,55,77],
    [7,9,11,14,56],
    [15,17,35,22]
]

Tìm danh sách con có tổng lớn nhất trong danh sách to
Kết quả mong muốn: Danh sách con nằm ở vị trí thứ ?? có tổng lớn nhất bằng ??



Tạo 1 input để nhập vào 1 chuỗi, từ chuỗi đó chuyển thành 1 list
VD: nhập 1 chuỗi 1 2 3 4 5 6 -> chuyển thành list = [1,2,3,4,5,6]

yêu cầu: Xoá toàn bộ số chẵn trong list đó

chuyển từ string thành list

string =  "1 2 3 4 5 6"

string.split(' ')

"""
# big_list = [
#     [1,2,3,4,5,100],
#     [12,54,55,77],
#     [7,9,11,14,56],
#     [15,17,35,22]
# ]
# max_sum = 0
# max_index = 0

# for i in range(len(big_list)):
#     current_sum = sum(big_list[i])
#     if current_sum > max_sum:
#         max_sum = current_sum
#         max_index = i
        
# print(f"Danh sách con nằm ở vị trí thứ {max_index + 1} có tổng lớn nhất bằng {max_sum}")



# set không có các phần tử trùng lặp
# các phần tử có thể trùng lặp trùng
# tuple không thể thêm bớt được các phần tử không chỉnh sửa dược giá trị các phần tử

# set và list ngoài dấu ngoặc khác nhau ở điểm nào


# làm việc với pygame, thực hành vẽ hình và tạo 1 game đơn giản bằng pygame
# dictionary = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3',
#     'key4': 'value4',
#     'key5': 'value5',
# }



# dictionary.keys() # lấy ra toàn bộ key trong dict
# dictionary.values() # lấy ra toàn bộ value trong dict
# dictionary.items() # lấy ra toàn cả cặp key và value


# list = ['value1', 'value2', 'value3', 'value4', 'value5', 'value6']
# list.append('value6')
# #remove(list[4])
# len(list) # đếm số phần tử trong list
# list.pop(4)
# list.remove('value5')

# list.sort(reverse=True)
# sorted(list, reverse=True)
"""

pop
insert
remove
len()
sorted
append


"""

# print(*dictionary.values())

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b