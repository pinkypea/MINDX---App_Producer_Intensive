# Khởi tạo class
class Students:
    name = "Nguyen Van A"
    age = 13
    gender = "Male"
    school = "MindX Technology School"

# Khởi tạo object
myStudent = Students()
print(myStudent.name)
print(myStudent.age)
print(myStudent.gender)
print(myStudent.school)

# Thay đổi giá trị mới cho thuộc tính
myStudent.school = "High school for gifted student"
print(myStudent.school)


class Laptop:
    # Khởi tạo phương thức __init__
    def __init__(self, os, cpu, ram, disk):
        self.os = os
        self.cpu = cpu
        self.ram = ram        
        self.disk = disk

    # Khởi tạo phương thức bình thường
    def show(self):
        print("OS:", self.os)
        print("CPU:", self.cpu)
        print("RAM:", self.ram,)
        print("Disk:", self.disk,)

# Khởi tạo object từ class Laptop
myLaptop = Laptop("Windows", "Core I5 11th", 16, 512)
myLaptop.show()

# Khởi tạo lớp cho hình chữ nhật:
#     - Viết phương thức __init__ để khai báo chiều dài, chiều rộng
#     - Viết phương thức để tính chu vi và diện tích

class HINHCHUNHAT:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_chu_vi_va_dien_tich(self):
        dien_tich = self.chieu_dai * self.chieu_rong
        chu_vi = (self.chieu_dai + self.chieu_rong) * 2
        print("Chu vi =", chu_vi)
        print("Diện tích =", dien_tich)

# Khởi tạo lớp cho hình tam giác
#     - Viết phương thức __init__ để khai báo 3 cạnh của tam giác
#     - Viết phương để kiểm tra xem tam giác đó có tồn tại hay không

class HINHTAMGIAC:
    def __init__(self, canh1, canh2, canh3):
        self.canh1 = canh1
        self.canh2 = canh2
        self.canh3 = canh3

    def is_available(self):
        if self.canh1 > self.canh2 + self.canh3 and self.canh2 > self.canh1 + self.canh3 and self.canh3 > self.canh1 + self.canh2:
            print("Tam giác có tồn tại")
        else:
            print("Tam giác không tồn tại")

# Khởi tạo giao diện bằng thư viện PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.show()
app.exec()

# Khởi tạo giao diện bằng thư viện PyQt6 và QtDesigner
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic

class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("index.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    test.show()
    app.exec()