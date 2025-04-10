# Hàm không trả về giá trị
def say_hello(name):
    print("Hello", name)

myFullName = "Đào Trung Kiên"
say_hello(myFullName)

# Hàm có giá trị trả về
def get_sum(a, b):
    return a + b

print(get_sum(10, 5))

# Viết hàm truyền vào 2 tham số là Chiều dài và Chiều rộng của HCN. 
# Tính P và S của HCN đó.

def get_P_and_S(length, width):
    S = length * width
    P = (length + width) * 2
    return S, P

length = int(input("Enter length: "))
width = int(input("Enter width: "))
print(get_P_and_S(length, width))

# Viết hàm truyền vào 6 tham số để tính điểm trung bình môn học:
#     - 3 tham số đầu tiên là điểm hệ số 1
#     - 2 tham số tiếp theo là điểm hệ số 2
#     - Tham số cuối cùng là điểm hệ số 3

def get_average_score(a, b, c, d, e, f):
    total = (a + b + c) + (d + e) * 2 + f * 3
    average_score = total / 10
    return average_score

print(get_average_score(1, 2, 3, 4, 5, 6))