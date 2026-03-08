import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv) # Biến app chứa đối tượng ứng dụng PyQt6, lớp QApplication - lớp chính để quản lý ứng dụng PyQt6
# Ghi chú: Trong một chương trình chỉ có MỘT đối tượng QApplication
# sys.argv: Lấy tham số từ terminal truyền cho ứng dụng
window = QWidget() # là lớp (đối tượng) đồ họa trống khi mới khởi tạo, đại diện cho cửa sổ giao diện chính
button = QPushButton("Click Me", window)
button.setGeometry(100, 100, 100, 30)
window.show() # hiển thị cửa sổ trong window ra màn hình máy tính.
app.exec() # Bắt đầu vòng lặp sự kiện hiển thị liên tục cửa sổ window ra màn hình.