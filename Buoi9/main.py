from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from models import MoviesList, Movies

from PyQt6.QtCore import QDate
from datetime import datetime

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Buoi9/add_dialog.ui", self)

        # Format lại ngày tháng năm
        self.ui.dateInput.setDisplayFormat("dd/MM/yyyy")

        # Xử lý 2 nút OK và Cancel
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def return_input_fields(self) -> dict:
        date_input = self.ui.dateInput.date().toPyDate()

        # Trả dữ liệu về
        return {
            "id": self.ui.idInput.text(),
            "title": self.ui.titleInput.text(),
            "release_date": date_input.strftime("%d/%M/%y"),
            "rating": float(self.ui.ratingInput.text() or 0.0),
            "link": self.ui.linkInput.text()
        }

class EditDialog(QDialog):
    def __init__(self, edit_item):
        super().__init__()
        self.ui = uic.loadUi("Buoi9/edit_dialog.ui", self)

        self.ui.dateInput.setDisplayFormat("dd/MM/yyyy")

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

        # Hiển thị dữ liệu hiện tại của item
        self.ui.idInput.setText(str(edit_item.id))
        self.ui.titleInput.setText(edit_item.title)
        date = datetime.strptime(edit_item.release_date, "%d/%m/%Y")
        self.ui.dateInput.setDate(QDate(date.year, date.month, date.day))
        self.ui.ratingInput.setText(str(edit_item.rating))
        self.ui.linkInput.setText(edit_item.link)

    def return_input_fields(self) -> dict:
        date_input = self.ui.dateInput.date().toPyDate()

        # Trả dữ liệu về
        return {
            "id": self.ui.idInput.text(),
            "title": self.ui.titleInput.text(),
            "release_date": date_input.strftime("%d/%m/%Y"),
            "rating": float(self.ui.ratingInput.text() or 0.0),
            "link": self.ui.linkInput.text()
        }
    
class CRUD_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Buoi9/CRUD.ui", self)

        self.database = MoviesList()
        self.database.load_from_json()

        self.create_CRUD_page()

        self.ui.removeButton.clicked.connect(self.delete)
        self.ui.addButton.clicked.connect(self.add)
        self.ui.editButton.clicked.connect(self.edit)

    def create_CRUD_page(self):
        movie_title = self.database.get_movie_title_list()
        self.ui.movieList.addItems(movie_title)
        self.ui.movieList.setCurrentRow(0)

    def add(self):
        current_index = self.ui.movieList.currentRow()
        add_dialog = AddDialog()
        # Nếu nhấn nút OK
        if add_dialog.exec():
            # Lấy dữ liệu từ dialog
            inputs = add_dialog.return_input_fields()
            movie = Movies(**inputs)
            # Thêm dữ liệu vào list widget
            self.ui.movieList.insertItem(current_index, inputs["title"])
            # Thêm dữ liệu vào json
            self.database.add_movie(movie)

    def edit(self):
        current_index = self.ui.movieList.currentRow()
        item = self.ui.movieList.item(current_index)
        item_title = item.text()
        edit_item = self.database.get_first_item_by_title(item_title)

        if item:
            edit_dialog = EditDialog(edit_item)
            if edit_dialog.exec():
                # Lấy dữ liệu từ dialog
                inputs = edit_dialog.return_input_fields()
                # Sửa lại tên item trên list widget
                item.setText(inputs["title"])
                # Sửa lại dữ liệu trong json
                self.database.update_movie(
                    movie_id = edit_item.id,
                    new_title=inputs["title"],
                    new_release_date = inputs["release_date"],
                    new_rating = inputs["rating"],
                    new_link = inputs["link"]
                )

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