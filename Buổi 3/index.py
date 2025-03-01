# Khởi tạo class Movies
class Movies:
    def __init__(self, id, title, release_date, rating = None, link = None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.rating = rating
        self.link = link

    def update(self, new_title, new_release_date, new_rating = None, new_link = None):
        self.title = new_title
        self.release_date = new_release_date
        self.rating = new_rating
        self.link = new_link

    def display(self):
        print(f"{self.id} \t {self.title} \t {self.release_date} \t {self.rating} \t {self.link}")

# Khởi tạo các đối tượng từ class Movies
movie1 = Movies("001", "Avengers: End game", "26/04/2019", 8.4)
movie2 = Movies("002", "Terrifier 3", "19/09/2024", 6.3)
movie3 = Movies("003", "Kamen Rider Decade", "30/08/2009")
movie4 = Movies("004", "Phinies and Ferb", "17/08/2007")

# Tạo danh sách đối tượng
movie_list = [movie1, movie2, movie3, movie4]

# Duyệt danh sách
print("\n----------------------", "\nDANH SÁCH PHIM BAN ĐẦU")
for movie in movie_list:
    print(f"{movie.id} \t {movie.title} \t {movie.release_date} \t {movie.rating} \t {movie.link}")

# Thêm phần tử mới vào danh sách
movie5 = Movies("005", "Jujutsu no Kaisen", "2018")
movie_list.append(movie5)
print("\n----------------------", "\nTHÊM PHIM MỚI VÀO DANH SÁCH")
for movie in movie_list:
    print(f"{movie.id} \t {movie.title} \t {movie.release_date} \t {movie.rating} \t {movie.link}")

# Xoá phần tử trong danh sách
for movie in movie_list:
    if movie.title == "Phinies and Ferb":
        movie_list.remove(movie)
print("\n----------------------", "\nXOÁ PHIM KHỎI DANH SÁCH")
for movie in movie_list:
    print(f"{movie.id} \t {movie.title} \t {movie.release_date} \t {movie.rating} \t {movie.link}")