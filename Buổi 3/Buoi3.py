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
movie2 = Movies("002", "Black Panther", "16/02/1018")
movie3 = Movies("003", "Love Rosie", "24/10/2014")
movie4 = Movies("004", "Mật mã Lyoko", "03/09/2003")

# Khởi tạo danh sách đối tượng
movie_list = [movie1, movie2, movie3, movie4]

# Duyệt phần tử của danh sách đối tượng
for movie in movie_list:
    print(movie.title)

# Thêm phần tử mới vào danh sách đối tượng
movie5 = Movies("005", "Goblin", "2/12/2016")
movie_list.append(movie5)

# Xoá phần tử khỏi danh sách đối tượng
for movie in movie_list:
    if movie.title == "Black Panther":
        movie_list.remove(movie)

# Cập nhật giá trị của đối tượng
movie1.update("010", "Iron Man 2", "07/05/2010")