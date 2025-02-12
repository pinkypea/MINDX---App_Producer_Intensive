# Khởi tạo class
class Student:
    name = "Nguyễn Văn A"
    age = 13
    gender = "Male"
    school = "MindX Technology School"

# Khởi tạo object từ class
myStudent = Student()

# Truy cập vào từng thuộc tính
print(myStudent.name)
print(myStudent.age)
print(myStudent.gender)
print(myStudent.school)

# Thay đổi giá trị của thuộc tính
myStudent.school = "High school for gifted student"
print(myStudent.school)


class Phone():
    def __init__(self, os, brand, ram, memory):
        self.os = os
        self.brand = brand
        self.ram = ram
        self.memory = memory

    def show(self):
        print("OS:", self.os)
        print("BRAND:", self.brand)
        print("RAM:", self.ram, "GB")
        print("Memory:", self.memory, "GB")

myPhone = Phone("Android", "Xiaomi", 8, 128)
myPhone.show()

# Khởi tạo lớp cho hình tam giác:
# - Viết phương thức __init__ để khai báo 3 cạnh.
# - Viết phương thức để kiểm tra xem tam giác đó là tam giác gì?
#     + Tam giác thường
#     + Tam giác vuông
#     + Tam giác cân
#     + Tam giác đều
#     + Tam giác không tồn tại
import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def checkTriangle(self):
        if self.a + self.b <= self.c or self.b + self.c <= self.a or self.c + self.a <= self.b:
            print("Đây không phải tam giác")
        else:
            if self.a == self.b or self.b == self.c or self.c == self.a:
                print("Tam giác cân")
            elif self.a == self.b == self.c:
                print("Tam giác đều")
            elif pow(self.a, 2) + pow(self.b, 2) == pow(self.c, 2) or pow(self.b, 2) + pow(self.c, 2) == pow(self.a, 2) or pow(self.c, 2) + pow(self.a, 2) == pow(self.b, 2):
                print("Tam giác vuông")
            else:
                print("Tam giác thường")

myTriangle = Triangle(6, 8, 10)
myTriangle.checkTriangle()



# Ôn tập về thư viện PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.show()
app.exec()

# Sử dụng thư viện PyQt6 để khởi chạy file giao diện

from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic

class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("test.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Test()
    test.show()
    app.exec()