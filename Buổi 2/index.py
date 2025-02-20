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
        print("RAM:", self.ram)
        print("Disk:", self.disk)

# Khởi tạo object từ class Laptop
myLaptop = Laptop("Windows", "Core I5 11th", 16, 512)
myLaptop.show()

# Khởi tạo lớp cho hình chữ nhật:
#     - Viết phương thức __init__ để khai báo chiều dài, chiều rộng
#     - Viết phương thức để tính chu vi và diện tích