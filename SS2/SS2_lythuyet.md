Đối tượng (Object): là một thực thể (thứ gì đó cụ thể). Đối tượng có hình dạng, màu sắc, và có thể thực hiện một số hành động. 

Ví dụ: Trong cuộc sống, đối tượng có thể là: 
- Đối tượng xe đạp màu đen có thể chạy
- Đối tượng con mèo tam thể có thể chạy nhảy 
- Đối tượng quả bóng màu cam có thể bật và lăn

Lớp (class): Đại diện cho một nhóm các đối tượng có những đặc điểm chung
Ví dụ: Trong cuộc sống, tất cả những chiếc xe đạp mà ta thấy được thực ra là đối tượng thuộc lớp "Xe Đạp". Lớp "Xe Đạp" có thể mô tả các đặc điểm chung: Số lượng bánh xe, hãng xe, màu sắc, yên,.... Một đối tượng thuộc lớp "Xe Đạp" xe có đặc điểm cụ thể như sau: Có 2 bánh, hãng Thống Nhất, màu đen, ...


===> Lớp và Đối Tượng có mối liên hệ mật thiết với nhau. Có thể hiểu Lớp là bản thiết kế để tạo ra nhiều đối tượng.

Cú pháp khai báo lớp:
class <Tên Lớp>:
    # thuộc tính (def, __init__)
    # phương thức (def ,self)

Cú pháp khởi tạo đối tượng:
<tên đối tượng> = <Tên Lớp>(<tham số nếu có>)



#### Đề bài thực hành: Hãy viết lớp mô tả hình chữ nhật và phương thức:
- tính chu vi hình chữ nhật
- tính diện tích hình chữ nhật



Module: Ôn tập PyQt6
- Cài đặt PyQt6: 
+ Tạo môi trường ảo ".venv": python -m venv .venv
+ kích hoạt môi trường ảo "...": 
+ Cài đặt pyqt6: pip install PyQt6
+ Cài thêm gói công cụ: pip install pyqt6-tools