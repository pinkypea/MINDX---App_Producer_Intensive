from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt

class ListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("list-widget.ui", self)

        self.list = ["Nhật Minh", "Trường Phúc", "Trung Khải", "Băng Sơn"]
        # Thêm giá trị mới vào trong list widget
        self.ui.listWidget.addItems(self.list)

        # Thêm giá trị mới vào vị trí bất kỳ trong list widget
        self.ui.listWidget.insertItem(0, "Trung Kiên")

        # Xoá phần tử tại vị trí cụ thể trong list widget
        self.ui.listWidget.takeItem(1)

        # Tìm kiếm phần tử trong list widget
        matched_items = self.ui.listWidget.findItems("Băng Sơn", Qt.MatchFlag.MatchContains)
        for i in range(self.ui.listWidget.count()):
            it = self.ui.listWidget.item(i)
            it.setHidden(it not in matched_items)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    listwidget = ListWidget()
    
    listwidget.show()
    app.exec()