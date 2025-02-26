# # Hàm có không trả về giá trị

# def say_hello(name):
#     print("Hello " + str(name))

# say_hello("lớp PTI11")

# # Hàm có giá trị trả về

# def get_sum(a, b):
#     sum = a + b
#     return sum

# print(get_sum(7, 8))


# # Viết hàm truyền vào 2 tham số là Chiều dài và Chiều rộng của 1 HCN.
# # Tính diện tích và chu vi của HCN đó.

# def get_P_and_S(CD, CR):
#     dien_tich = CD * CR
#     chu_vi = (CD + CR) * 2
#     return dien_tich, chu_vi

# print(get_P_and_S(10, 7))

class Movies:
    def __init__(self, id, title, release_date, rating=None, link=None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.rating = float(rating) if rating else 0
        self.link = link

    def update(self, new_id, new_title, new_release_date, new_rating=None, new_link=None):
        self.id = new_id
        self.title = new_title
        self.release_date = new_release_date
        self.rating = new_rating
        self.link = new_link

# Khởi tạo các đối tượng
movie1 = Movies("001", "Iron Man", "16/05/2008")
movie2 = Movies("002", "Black Panther", "16/02/2018")
movie3 = Movies("003", "Love Rosie", "24/10/2014")
movie4 = Movies("004", "Mật mã Lyoko", "03/09/2003")

# Khởi tạo danh sách đối tượng
movie_list = [movie1, movie2, movie3, movie4]

