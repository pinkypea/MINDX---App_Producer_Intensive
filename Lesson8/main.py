from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from models import MovieList

from PyQt6.QtCore import QDate
from datetime import datetime

class AddDialog(QDialog):
    def __init__(self):
        self.ui = uic.loadUi("Lesson8/add_dialog.ui", self)

        # Format lại ngày tháng năm
        self.ui.dateInput.setDisplayFormat("dd/MM/yyyy")

    def return_input_fields(self) -> dict:
        date_input = self.ui.dateInput.date().toPyDate()

        # Trả dữ liệu về
        return {
            "id": self.ui.idInput.text(),
            "title": self.ui.titleInput.text(),
            "release_date": self.ui.date_input.strftime("%b %Y"),
            "rating": float(self.ui.ratingInput.text() if self.ui.ratingInput.text() else None),
            "link": self.ui.linkInput.text()
        }

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

        self.deleteButton.clicked.connect(self.delete)
    
    def delete(self):
        current_index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(current_index)
        item_title = item.text()

        # Tạo message box để confirm
        if item is not None:
            choice = QMessageBox.question(self, "Remove movie", 
                                                "Do you want to remove this movie?", 
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if choice == QMessageBox.StandardButton.Yes:
                item = self.ui.listWidget.takeItem(current_index) # Xoá phần tử trong list widget
                self.database.remove_movie(item_title) # Xoá dữ liệu trong file json

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListWidget()
    window.show()
    app.exec()