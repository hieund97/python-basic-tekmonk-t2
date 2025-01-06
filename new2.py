names = ["Áo Thun", "Quần Jeans", "Mũ Lưỡi Trai", "Giày Thể Thao", "Balo"]
prices = [100000, 300000, 150000, 500000, 250000]
quantities = [50, 20, 30, 15, 10]
def show_product_list():
    print(f"{'STT':<5} {'Tên Sản Phẩm':<20} {'Giá':<10} {'Số Lượng':<10}")
    for i in range(len(names)):
        print(f"{i+1:<5} {names[i]:<20} {prices[i]:<10} {quantities[i]:<10}")
def add_new_product():
    name = input("Nhập tên sản phẩm mới: ")
    price = float(input("Nhập giá sản phẩm mới: "))
    quantity = int(input("Nhập số lượng sản phẩm mới: "))
    names.append(name)
    prices.append(price)
    quantities.append(quantity)
    print("Sản phẩm đã được thêm thanhf cong!")
def search_product():
    search_name = input("Nhập tên sản phẩm cần tìm: ")
    found = False
    for i in range(len(names)):
        if names[i] == search_name:
            print(f"Sản phẩm: {names[i]}")
            print(f"Giá: {prices[i]}")
            print(f"Số lượng: {quantities[i]}")
            found = True
            break
    if not found:
        print("Sản phẩm không có")
def update_quantity():
    update_name = input("Nhập tên sản phẩm cần đổi số lượng: ")
    found = False
    for i in range(len(names)):
        if names[i] == update_name:
            new_quantity = int(input("Nhập số mới: "))
            quantities[i] = new_quantity
            print(f"Số lượng sản phẩm {names[i]} đã được cập nhật.")
            found = True
            break
    if not found:
        print("Sản phẩm không tồn tại.")
def calculate_inventory_value():
    total_value = 0
    for i in range(len(prices)):
        total_value += prices[i] * quantities[i]
    print(f"Tổng giá trị kho hàng: {total_value:,} VND")
def most_selling_product():
    max_quantity = max(quantities)
    max_index = quantities.index(max_quantity)
    print(f"Sản phẩm bán chạy nhất: {names[max_index]} (Số lượng: {quantities[max_index]})")
    print(f"Giá: {prices[max_index]}")
def main():
    while True:
        print("\nChọn chức năng:")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm")
        print("4. Cập nhật số lượng sản phẩm")
        print("5. Tính tổng giá trị kho hàng")
        print("6. Xác định sản phẩm bán chạy nhất")
        print("7. Thoát")
       
        choice = input("Nhập số chọn: ")
       
        if choice == '1':
            show_product_list()
        elif choice == '2':
            add_new_product()
        elif choice == '3':
            search_product()
        elif choice == '4':
            update_quantity()
        elif choice == '5':
            calculate_inventory_value()
        elif choice == '6':
            most_selling_product()
        elif choice == '7':
            print("Chương trình kết thúc.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
