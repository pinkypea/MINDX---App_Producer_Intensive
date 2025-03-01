# Cú pháp khởi tạo class và object

# class Student:
#     # Thuộc tính
#     name = "Nguyễn Văn A"
#     age = 13
#     gender = "male"
#     school = "MindX Technology School"

#     # Phương thức

# myStudent = Student() #Khởi tạo object myStudent từ class Student
# # Truy cập thuộc tính của đối tượng
# print(myStudent.name)
# print(myStudent.age)
# print(myStudent.gender)
# print(myStudent.school)

# # Thay đổi giá trị của thuộc tính
# myStudent.age = 15
# myStudent.school = "High school for gifted students"
# print(myStudent.age)
# print(myStudent.school)

# class Phone:
#     def __init__(self, brand, ram, memory, screen, nfc):
#         self.brand = brand
#         self.ram = ram
#         self.memory = memory
#         self.screen = screen
#         self.nfc = nfc

#     def show(self):
#         print("Brand:", self.brand)
#         print("RAM:", self.ram)
#         print("Memory:", self.memory)
#         print("Screen:", self.screen)
#         print("NFC:", self.nfc)

# myPhone = Phone("Xiaomi", 8, 128, "AMOLED", True)
# myPhone.show()

# Viết class HinhChuNhat.
#     - Viết phương thức __init__ để khởi tạo Chiều dài và Chiều rộng
#     - Viết phương thức để tính Chu vi và diện tích

# class HinhChuNhat:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def perimeterAndArea(self):
#         P = (self.length + self.width) * 2
#         S = self.length * self.width
#         print("Chu vi:", P)
#         print("Diện tích:", S)

# myGarden = HinhChuNhat(10, 8)
# myGarden.perimeterAndArea()

# Viết class HinhVuong:
#     - Viết phương thức __init__ để khởi tạo Cạnh hình vuông
#     - Viết phương thức để tính độ dài đường chéo hình vuông

# import math
# class HinhVuong:
#     def __init__(self, canh):
#         self.canh = canh

#     def tinh_duong_cheo(self):
#         duong_cheo = math.sqrt(2 * pow(self.canh, 2))
#         print(duong_cheo)

# nha_cua_toi = HinhVuong(4)
# nha_cua_toi.tinh_duong_cheo()

# Tạo cửa sổ từ pyqt6
# from PyQt6.QtWidgets import QApplication, QMainWindow
# import sys

# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()
# app.exec()

# Tạo cửa sổ từ file giao diện của Qt Designer

from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic

class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("index.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    app.exec()