import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class Login(QMainWindow): # khiến lớp Logcin có thể sử dụng để tạo giao diện đăng nhập cho ứng dụng
    def __init__(self):
        super().__init__() 
        uic.loadUi("SS2/ui/Login.ui",self) # Nạp giao diện tư file có tên "" vào cho cửa sổ Login.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
        