import sys
import os
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from SS4.models.movie_item import MovieItem
from SS4.models.movie_list import MovieDatabase

class MainWindow(QMainWindow):
    # Định nghĩa vị trí của các file ui
    UI_LOCATION  = os.path.join('SS7/ui/main_window1.ui') # thay đổi
    STYLE_LOCATION = os.path.join("SS7/ui/style_main1.qss")
    
    def __init__(self, parent: QApplication):
        super(MainWindow, self).__init__()
        self.app = parent
        
        # Load file giao diện .ui và .qss
        self.ui = uic.loadUi(self.UI_LOCATION, self)
        with open(self.STYLE_LOCATION, "r") as style_file:
            style_config = style_file.read()
        self.setStyleSheet(style_config)  # truyền các thuộc tính đã sửa để cập nhật vào app
        
        
        # Hiển thị trang CRUD
        self.ui.stackedWidget.setCurrentIndex(2)
        
        
        # Tạo Database
        self.dtb = MovieDatabase()
        self.dtb.load_data()
        
        # Hiển thị danh sách phim
        movie_titles = self.dtb.get_title_list()
        
        # Hiển thị cửa sổ ra màn hình.
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    sys.exit(app.exec())