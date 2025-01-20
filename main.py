import product_manager as pm

product_list = []

while True:
    print("Chọn chức năng:")
    print("1. Thêm sản phẩm mới")
    print("2. Tìm kiếm sản phẩm")
    print("3. Tính tổng giá trị kho hàng")
    print("4. Xác định sản phẩm bán chạy nhất")
    print("5. Thoát")
    
    choice = int(input("Nhập số chọn: "))
    
    if choice == 1:
        for i in range(2):
            print("Nhập 5 sản phẩm")
            print(f"Lần {i + 1}")
            name = input("Nhập tên sản phẩm: ")
            price = float(input("Nhập giá sản phẩm: "))
            quantity = int(input("Nhập số lượng sản phẩm: "))
            pm.add_product(product_list, name, price, quantity)
    elif choice == 2:
        name = input("Nhập tên sản phẩm: ")
        result = pm.search_product(product_list, name)
        print(result)
    elif choice == 3:
        result = pm.total_inventory_value(product_list)
        print(result)
    elif choice == 4:
        result = pm.find_most_expensive_product(product_list)
        print(result)
    elif choice == 5:
        break
    
        
    
