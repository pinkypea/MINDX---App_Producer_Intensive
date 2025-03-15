# Ôn tập về hàm

# Hàm không trả về giá trị
def say_hello(name):
    print("Hello", name)

say_hello("MindX")
my_name = "Nhật Minh"
say_hello(my_name)

# Hàm có giá trị trả về
def get_average(a, b, c):
    sum = a + b + c
    average = sum / 3
    return average

result = get_average(10, 20, 25)
print(result)

# Viết 1 hàm truyền vào 2 tham số là CD và CR của HCN.
# Tính P và S của HCN.

def get_P_and_S(CD, CR):
    P = (CD + CR) * 2
    S = CD * CR
    return P, S

print(get_P_and_S(20, 10))