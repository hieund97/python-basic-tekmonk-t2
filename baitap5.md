### Bài Tập Python: Quản Lý Kho Sản Phẩm 
#### Đề Bài:  
Viết chương trình Python để quản lý kho sản phẩm của cửa hàng. Thông tin về sản phẩm sẽ được lưu trong **các danh sách** riêng biệt.

---

### Yêu Cầu:

#### 1. **Tạo Danh Sách Sản Phẩm**  
- Tạo 3 danh sách riêng biệt:
  - `names`: Lưu tên sản phẩm (chuỗi).
  - `prices`: Lưu giá sản phẩm (số thực).
  - `quantities`: Lưu số lượng sản phẩm trong kho (số nguyên).  

**Ví dụ**:
```python
names = ["Áo Thun", "Quần Jeans", "Mũ Lưỡi Trai", "Giày Thể Thao", "Balo"]
prices = [100000, 300000, 150000, 500000, 250000]
quantities = [50, 20, 30, 15, 10]
```

---

#### 2. **Hiển Thị Danh Sách Sản Phẩm**  
- Sử dụng **vòng lặp** để hiển thị danh sách sản phẩm với thông tin đầy đủ:
  ```
  STT   Tên Sản Phẩm       Giá        Số Lượng
  1     Áo Thun            100000     50
  2     Quần Jeans         300000     20
  ```

---

#### 3. **Thêm Sản Phẩm Mới**  
- Hỏi người dùng nhập:
  - Tên sản phẩm (`str`).
  - Giá sản phẩm (`float`).
  - Số lượng sản phẩm (`int`).
- Thêm thông tin này vào các danh sách tương ứng (`names`, `prices`, `quantities`).

---

#### 4. **Tìm Kiếm Sản Phẩm**  
- Hỏi người dùng nhập tên sản phẩm cần tìm.  
- Dùng **toán tử so sánh** và **vòng lặp** để kiểm tra trong danh sách `names`.  
  - Nếu tìm thấy, hiển thị thông tin chi tiết (tên, giá, số lượng).  
  - Nếu không tìm thấy, thông báo: "Sản phẩm không tồn tại".

---

#### 5. **Cập Nhật Số Lượng Sản Phẩm**  
- Hỏi người dùng nhập tên sản phẩm cần cập nhật số lượng.  
- Nếu sản phẩm tồn tại:
  - Hỏi số lượng mới và cập nhật trong danh sách `quantities`.  
- Nếu không tồn tại, thông báo: "Sản phẩm không tồn tại".

---

#### 6. **Tính Tổng Giá Trị Kho Hàng**  
- Sử dụng **vòng lặp** để tính tổng giá trị kho hàng:
  \[
  \text{Tổng giá trị} = \sum (\text{prices[i]} \times \text{quantities[i]})
  \]  
- Hiển thị kết quả.

---

#### 7. **Xác Định Sản Phẩm Bán Chạy Nhất**  
- Sử dụng **toán tử so sánh** để tìm sản phẩm có số lượng lớn nhất trong `quantities`.  
- Hiển thị tên, giá, và số lượng của sản phẩm đó.

---

### Yêu Cầu Kỹ Thuật:
- Không được sử dụng `dict`, chỉ sử dụng các danh sách (`list`).
- Sử dụng các **toán tử so sánh** và **vòng lặp**.
- Các thao tác phải đồng bộ giữa các danh sách (cùng chỉ số `i` trong các danh sách).

---

#### Kết Quả Mong Đợi:  
Kết quả tương tự bài tập trước, ví dụ:  
```
Tổng giá trị kho hàng: 5,000,000 VND  
Sản phẩm bán chạy nhất: Áo Thun (Số lượng: 50)
```