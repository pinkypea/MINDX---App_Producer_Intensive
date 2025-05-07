from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from models import MovieList

import os
from datetime import datetime
from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6.QtCore import QDate, QDir

class AddDialog(QDialog):
    """
    Hộp thoại Add
    """

    def __init__(self):
        super().__init__()

        # Load giao diện
        self.ui = uic.loadUi("Buoi5/ui/add_dialog.ui", self)
        
        # Tạo đối tượng QDir để quản lý đường dẫn
        self.dir = QDir()

        # Nút tải ảnh từ máy tính
        self.ui.uploadImgButton.clicked.connect(self.browse_files)
        self.ui.releasedateInput.setDisplayFormat("dd/MM/yyyy") # Format ngày tháng năm
    
    def browse_files(self):
        """
        Phương thức mở file dialog để chọn ảnh
        """
        fname = QFileDialog.getOpenFileName(self,
                                            'Open file', 
                                            './ui/images',
                                            filter='Image files (*.png, *.jpg, *.svg)'
                                            )
        self.ui.uploadImgButton.setText(fname[0])
        return fname

    def return_input_fields(self) -> dict:
        """
        Thu thập dữ liệu của tất cả các trường và trả về một dict
        """
        # Xử lý trường ngày tháng năm
        date_input = self.ui.releasedateInput.date().toPyDate() # formatted YYYY-mm-dd
        image_path_input = self.ui.uploadImgButton.text()
        
        # Trả dữ liệu
        return {
            "title": self.ui.titleInput.text(),
            "release_date": date_input.strftime("%b %Y"),
            "image": self.dir.relativeFilePath(image_path_input),
            "rating": float(self.ui.ratingInput.text()) if self.ui.ratingInput.text() else None,
            "link": self.ui.urlInput.text() if self.ui.urlInput.text() else "None"
        }


class EditDialog(QDialog):
    """
    Hộp thoại Edit 
    """

    def __init__(self, edit_item): # Nhận vào đối tượng
        super().__init__()

        # Load giao diện
        self.ui = uic.loadUi("Buoi5//ui/edit_dialog.ui.ui", self)
        # with open(self.STYLE_LOCATION, "r") as style_file:
        #     style_config = style_file.read()
        # self.setStyleSheet(style_config)

        self.ui.releasedateInput.setDisplayFormat("dd/MM/yyyy")
        self.ui.uploadImgButton.clicked.connect(self.browse_files)
        
        self.dir = QDir()

        # Hiển thị dữ liệu hiện tại của item
        self.ui.titleInput.setText(edit_item.title)
        date = datetime.strptime(edit_item.release_date, '%b %Y')
        self.ui.releasedateInput.setDate(QDate(date.year, date.month, date.day))
        self.ui.uploadImgButton.setText(self.dir.relativeFilePath(edit_item.image))
        self.ui.ratingInput.setText(str(edit_item.rating))
        self.ui.urlInput.setText(edit_item.link)
    
    def browse_files(self):
        """
        Phương thức mở file dialog để chọn ảnh
        """
        fname = QFileDialog.getOpenFileName(self,
                                            'Open file', 
                                            './ui/images',
                                            filter='Image files (*.png, *.jpg, *.svg)'
                                            )
        self.ui.uploadImgButton.setText(fname[0])
        return fname
    
    def return_input_fields(self) -> dict:
        """
        Thu thập dữ liệu của tất cả các trường và trả về một dict
        """
        date_input = self.ui.releasedateInput.date().toPyDate() # formatted YYYY-mm-dd
        image_path_input = self.ui.uploadImgButton.text()

        return {
            "title": self.ui.titleInput.text(),
            "release_date": date_input.strftime("%b %Y"),
            "image": self.dir.relativeFilePath(image_path_input),
            "rating": float(self.ui.ratingInput.text()) if self.ui.ratingInput.text() else None,
            "link": self.ui.urlInput.text() if self.ui.urlInput.text() else "None"
        }


class ListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Buoi5/ui/main_window1.ui", self)

        self.database = MovieList()
        self.database.load_from_json()

        self.setup_CRUD_page()

    def setup_CRUD_page(self):
        movie_title = self.database.get_title_list()
        self.ui.animeListWidget.addItems(movie_title)
        self.ui.animeListWidget.setCurrentRow(0)

    def on_homeButton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_rankButton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_CRUDButton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_exitButton_clicked(self):
        QApplication.quit()

    ### CRUD methods
    def add(self):
        curr_index = self.ui.animeList.currentRow()

        # Tạo Dialog Add
        add_dialog = AddDialog()
        # Nếu nhấn nút OK trên dialog
        if add_dialog.exec():
            # Lấy dữ liệu từ dialog
            inputs = add_dialog.return_input_fields()
            # Thêm item vào List Widget
            self.ui.animeList.insertItem(curr_index, inputs["title"])
            # Thêm dữ liệu vào database
            self.database.add_movie(inputs)

    def edit(self):
        # Lấy item đang chọn
        curr_index = self.ui.animeList.currentRow()
        item = self.ui.animeList.item(curr_index)
        item_title = item.text()
        edit_item = self.database.get_first_item_by_title(item_title)

        # Tạo Dialog Edit 
        if item is not None:
            edit_dialog = EditDialog(edit_item)
            # Nếu nhấn nút OK trên dialog
            if edit_dialog.exec():
                # Lấy dữ liệu từ dialog
                inputs = edit_dialog.return_input_fields()
                # Sửa lại tên item trên List Widget
                item.setText(inputs["title"])
                # Sửa dữ liệu trong database
                self.dtb.update_movie(item_title, inputs)

    def delete(self):
        # Lấy item đang chọn
        curr_index = self.ui.animeList.currentRow()
        item = self.ui.animeList.item(curr_index)
        item_title = item.text()
        
        # Tạo Message Box confirm
        if item is not None:
            choice = QMessageBox.question(self, "Remove Anime",
                                            "Do you want to remove this anime?",
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            # Nếu chọn nút "Yes"
            if choice == QMessageBox.StandardButton.Yes:
                # Xoá item khỏi List Widget
                item = self.ui.animeList.takeItem(curr_index)
                # Xoá dữ liệu trong database
                self.dtb.remove_movie(item_title)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    listWidget = ListWidget()
    
    listWidget.show()
    app.exec()