from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys
from models import MovieList

class ListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Lesson_8/list-widget.ui", self)

        self.database = MovieList()
        self.database.load_from_json()

        self.setup_CRUD_page()

    def setup_CRUD_page(self):
        movie_title = self.database.get_title_list()
        self.ui.movieList.addItems(movie_title)
        self.ui.movieList.setCurrentRow(0)

    def delete(self):
        current_index = self.ui.movieList.currentRow()
        item = self.ui.movieList.item(current_index)
        item_title = item.text()

        # Tạo ra message box để confirm
        if item is not None:
            choice = QMessageBox.question(self, "Remove movie", 
                                                "Do you want to delete this movie?",
                                                QMessageBox.StandardButton.Yes | 
                                                QMessageBox.StandardButton.No)
            if choice == QMessageBox.StandardButton.Yes:
                item = self.ui.movieList.takeItem(item_title)
                self.database.remove_movie(item_title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListWidget()
    window.show()
    app.exec()