from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from models import MoviesList

class CRUD_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Buoi8/CRUD.ui", self)

        self.database = MoviesList()
        self.database.load_from_json()

        self.create_CRUD_page()

        self.ui.removeButton.clicked.connect(self.delete)

    def create_CRUD_page(self):
        movie_title = self.database.get_movie_title_list()
        self.ui.movieList.addItems(movie_title)
        self.ui.movieList.setCurrentRow(0)

    def delete(self):
        # Lấy items hiện tại
        current_index = self.ui.movieList.currentRow()
        item = self.ui.movieList.item(current_index)
        item_title = item.text()

        # Tạo message box
        if item is not None:
            choice = QMessageBox.question(self, "Remove movie",
                                            "Do you want to remove this movie?",
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
            # Nếu người dùng ấn "Yes" thì xoá phim
            if choice == QMessageBox.StandardButton.Yes:
                item = self.ui.movieList.takeItem(current_index)
                # Xoá dữ liệu trong DB
                self.database.remove_movie(item_title)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    CRUDpage = CRUD_Page()
    CRUDpage.show()
    app.exec()