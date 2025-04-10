from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from models import MovieList


class ListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Lesson7/list-widget.ui", self)

        self.database = MovieList()
        self.database.load_from_json()

        self.setup_CRUD_page()

    # Xử lý các phần CRUD của trang CRUD
    def setup_CRUD_page(self):
        movie_title = self.database.get_title_list()
        self.ui.listWidget.addItems(movie_title)
        self.ui.listWidget.setCurrentRow(0)

        self.ui.removeButton.clicked.connect(self.delete)

    def delete(self):
        # Lấy item đang chọn
        curr_index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(curr_index)
        item_title = item.text()
        
        # Tạo Message Box confirm
        if item is not None:
            choice = QMessageBox.question(self, "Remove movie",
                                            "Do you want to remove this movie?",
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            # Nếu chọn nút "Yes"
            if choice == QMessageBox.StandardButton.Yes:
                # Xoá item khỏi List Widget
                item = self.ui.listWidget.takeItem(curr_index)
                # Xoá dữ liệu trong database
                self.database.remove_movie(item_title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListWidget()
    window.show()
    app.exec()