from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt6 import uic
import sys
from models import MovieList
from models import Movies

from PyQt6.QtCore import QDate
from datetime import datetime

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Lesson_8/add-dialog.ui", self)

        # Format lại ngày tháng năm (Long và Vinh không cần ghi)
        self.ui.dateInput.setDisplayFormat("dd/MM/yyyy")

        # Xử lý nút OK/Cancel
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def return_input_fields(self) -> dict:
        date_input = self.ui.dateInput.date().toPyDate() #Long và Vinh không cần ghi

        return {
            "id": self.ui.idInput.text(),
            "title": self.ui.titleInput.text(),
            "release_date": date_input.strftime("dd/MM/yyyy"),
            "rating": float(self.ui.ratingInput.text() or 0.0),
            "link": self.ui.linkInput.text()
        }

class ListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Lesson_8/list-widget.ui", self)

        self.database = MovieList()
        self.database.load_from_json()

        self.setup_CRUD_page()

        self.deleteButton.clicked.connect(self.delete)
        self.addButton.clicked.connect(self.add)

    def setup_CRUD_page(self):
        movie_title = self.database.get_title_list()
        self.ui.movieList.addItems(movie_title)
        self.ui.movieList.setCurrentRow(0)

    def add(self):
        current_index = self.ui.movieList.currentRow()
        
        # Khởi tạo add dialog
        add_dialog = AddDialog()
        # Nếu ấn nút OK
        if add_dialog.exec():
            # Lấy dữ liệu từ dialog
            inputs = add_dialog.return_input_fields()
            movie = Movies(**inputs)
            # Thêm item vào list widget
            self.ui.movieList.insertItem(current_index, inputs["title"])
            self.database.add_movie(movie)

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
                item = self.ui.movieList.takeItem(current_index)
                self.database.remove_movie(item_title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListWidget()
    window.show()
    app.exec()