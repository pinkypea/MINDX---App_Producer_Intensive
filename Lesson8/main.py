from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from models import MovieList


class ListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Lesson8/list-widget.ui", self)

        self.database = MovieList()
        self.database.load_from_json()

        self.setup_CRUD_page()

    # Xử lý các phần CRUD của trang CRUD
    def setup_CRUD_page(self):
        movie_title = self.database.get_title_list()
        self.ui.listWidget.addItems(movie_title)
        self.ui.listWidget.setCurrentRow(0)

    

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListWidget()
    window.show()
    app.exec()