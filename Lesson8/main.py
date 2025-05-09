from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from models import MovieList, Movies

from PyQt6.QtCore import QDate
from datetime import datetime


class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Lesson8/add_dialog.ui", self)

        # Format lại ngày tháng năm
        self.ui.dateInput.setDisplayFormat("dd/MM/yyyy")

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def return_input_fields(self) -> dict:
        date_input = self.ui.dateInput.date().toPyDate()

        # Trả dữ liệu về
        return {
            "id": self.ui.idInput.text(),
            "title": self.ui.titleInput.text(),
            "release_date": date_input.strftime("%d/%m/%Y"),
            "rating": float(self.ui.ratingInput.text() or 0.0),
            "link": self.ui.linkInput.text(),
        }

class EditDialog(QDialog):
    def __init__(self, edit_item):
        super().__init__()
        self.ui = uic.loadUi("Lesson8/edit_dialog.ui", self)

        # Format lại ngày tháng năm
        self.ui.dateInput.setDisplayFormat("dd/MM/yyyy")

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

        # Hiển thị dữ liệu hiện tại của item
        self.ui.idInput.setText(edit_item.id)
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
            "link": self.ui.linkInput.text(),
        }

class ListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Lesson8/list-widget.ui", self)

        self.database = MovieList()
        self.database.load_from_json()

        self.setup_CRUD_page()

        self.addButton.clicked.connect(self.add)
        self.editButton.clicked.connect(self.edit)
        self.deleteButton.clicked.connect(self.delete)

    # Xử lý các phần CRUD của trang CRUD
    def setup_CRUD_page(self):
        movie_title = self.database.get_title_list()
        self.ui.listWidget.addItems(movie_title)
        self.ui.listWidget.setCurrentRow(0)

    def add(self):
        current_index = self.ui.listWidget.currentRow()
        add_dialog = AddDialog()
        # Nếu nhấn nút OK
        if add_dialog.exec():
            # Lấy dữ liệu từ dialog
            inputs = add_dialog.return_input_fields()
            movie = Movies(**inputs)
            # Thêm item vào list widget
            self.ui.listWidget.insertItem(current_index, inputs["title"])
            # Thêm dữ liệu vào database
            self.database.add_movie(movie)

    def edit(self):
        current_index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(current_index)
        item_title = item.text()
        edit_item = self.database.get_first_movie_by_title(item_title)

        # Tạo dialog edit
        if item:
            edit_dialog = EditDialog(edit_item)
            # Nếu nhấn nút OK
            if edit_dialog.exec():
                inputs = edit_dialog.return_input_fields()
                # Sửa lại item trên list widget
                item.setText(inputs["title"])
                # Sửa dữ liệu trong json
                self.database.update_movie(
                    movie_id=edit_item.id,
                    new_title=inputs["title"],
                    new_release_date=inputs["release_date"],
                    new_rating=inputs["rating"],
                    new_link = inputs["link"]
                )

    def delete(self):
        current_index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(current_index)
        item_title = item.text()

        # Tạo message box để confirm
        if item is not None:
            choice = QMessageBox.question(
                self,
                "Remove movie",
                "Do you want to remove this movie?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )

            if choice == QMessageBox.StandardButton.Yes:
                item = self.ui.listWidget.takeItem(
                    current_index
                )  # Xoá phần tử trong list widget
                self.database.remove_movie(item_title)  # Xoá dữ liệu trong file json


if __name__ == "__main__":
    app = QApplication(sys.argv)
    add = AddDialog()
    window = ListWidget()
    window.show()
    app.exec()
