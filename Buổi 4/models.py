# Class Movies để khởi tạo các bộ phim
class Movies:
    def __init__(self, id, title, release_date, rating = None, link = None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.rating = float(rating) if rating else 0
        self.link = link

# Class MoviesList để quản lý danh sách phim
class MoviesList:
    def __init__(self):
        self.movie_list = []

    # Thêm phim mới
    def add_movie(self, movie):
        self.movie_list.append(movie)

    # Xoá phim
    def remove_movie(self, identifier):
        for movie in self.movie_list:
            if movie.title == identifier or movie.id == identifier:
                self.movie_list.remove(movie)

    # Cập nhật phim
    def update_movie(self, movie_id, new_id, new_title, new_release_date, new_rating = None, new_link = None):
        for movie in self.movie_list:
            if movie.id == movie_id:
                movie.update(new_id, new_title, new_release_date, new_rating, new_link)
                return True
        return False

    # Tìm kiếm phim bằng tên
    def search_movie(self, title):
        return [movie for movie in self.movie_list if title.lower() in movie.title.lower()]

    # Trả về tên phim viết in thường
    def get_movie_title(self, movie):
        return movie.title.lower()
    
    # Trả về điểm đánh giá của phim
    def get_movie_rating(self, movie):
        return movie.rating
    
    # Trả về ngày tháng năm phát hành phim
    def get_movie_release_date(self, movie):
        # Chuyển ngày tháng năm từ string thành dạng danh sách
        day, month, year = map(int, movie.release_date.split("/"))
        return (year, month, day)

    # Sắp xếp phim
    def sort_movie(self, key="title"):
        if key == "title":
            self.movie_list.sort(key = self.get_movie_title)

        elif key == "rating":
            self.movie_list.sort(key = self.get_movie_rating)

        elif key == "release_date":
            self.movie_list.sort(key = self.get_movie_release_date)

    # In ra danh sách phim
    def display_movie(self):
        for movie in self.movie_list:
            print(f"{movie.id} - {movie.title} - {movie.release_date} - {movie.rating} - {movie.link}")

movie_list = MoviesList()
# Khởi tạo các đối tượng từ class Movies
movie1 = Movies("001", "Avengers: End game", "26/04/2019", 8.4)
movie2 = Movies("002", "Terrifier 3", "19/09/2024", 6.3)
movie3 = Movies("003", "Kamen Rider Decade", "30/08/2009")
movie4 = Movies("004", "Phinies and Ferb", "17/08/2007")

print("\n-----------------")
print("DANH SÁCH PHIM BAN ĐẦU")
movie_list.display_movie()

# Kết quả khi thêm phim mới
print("\n-----------------")
print("DANH SÁCH PHIM KHI THÊM PHIM MỚI")
movie_list.add_movie(movie1)
movie_list.add_movie(movie2)
movie_list.add_movie(movie3)
movie_list.add_movie(movie4)
movie_list.display_movie()

# Kết quả khi xoá phim
print("\n-----------------")
print("DANH SÁCH PHIM KHI XOÁ PHIM")
movie_list.remove_movie("Terrifier 3")
movie_list.display_movie()

# Kết quả khi tìm kiếm phim
result_movie = movie_list.search_movie("kamen")
print("\n-----------------")
print("DANH SÁCH PHIM KHI TÌM KIẾM PHIM")
for movie in result_movie:
    print(movie.title)

# Sắp xếp phim theo tên
movie_list.sort_movie(key="title")
print("\n-----------------")
print("SẮP XẾP PHIM THEO TÊN")
movie_list.display_movie()

# Sắp xếp phim theo rating
movie_list.sort_movie(key="rating")
print("\n-----------------")
print("SẮP XẾP PHIM THEO RATING")
movie_list.display_movie()

# Sắp xếp phim theo ngày phát hành
movie_list.sort_movie(key="release_date")
print("\n-----------------")
print("SẮP XẾP PHIM THEO NGÀY PHÁT HÀNH")
movie_list.display_movie()