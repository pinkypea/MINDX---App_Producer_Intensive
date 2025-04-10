# Khởi tạo class Movies
class Movies:
    def __init__(self, id, title, release_date, rating = None, link = None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.rating = rating
        self.link = link

# Khởi tạo class MovieList
class MovieList:
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

    # Tìm kiếm phim
    def search_movie(self, title):
        return [movie for movie in self.movie_list if title.lower() in movie.title.lower()]
    
    # Cập nhật phim
    def update_movie(self, movie_id, new_id, new_title, new_release_date, new_rating = None, new_link = None):
        for movie in self.movie_list:
            if movie.id == movie_id:
                movie.update(new_id, new_title, new_release_date, new_rating, new_link)
                return True
        return False

    # Sắp xếp phim
    def get_title(self, movie):
        return movie.title.lower()
    
    def get_rating(self, movie):
        return movie.rating
    
    def get_release_date(self, movie):
        day, month, year = map(int, movie.release_date.split("/"))
        return (year, month, day)
    
    def sort_movie(self, key = "title"):
        if key == "title":
            self.movie_list.sort(key = self.get_title)
        elif key == "rating":
            self.movie_list.sort(key = self.get_rating)
        elif key == "release_date":
            self.movie_list.sort(key = self.get_release_date)

    def display_movie(self):
        for movie in self.movie_list:
            print(f"{movie.id} - {movie.title} - {movie.release_date} - {movie.rating} - {movie.link}") 

# KIỂM THỬ
movie_list = MovieList()
movie1 = Movies("001", "Avengers", "27/04/2012", 8.0)
movie2 = Movies("002", "Justice league", "17/11/2017", 6.0)
movie3 = Movies("003", "Cô dâu 8 tuổi", "21/07/2008")
movie4 = Movies("004", "Kungfu Panda", "27/06/2008", 7.6)
print("\n-----------------------")
print("DANH SÁCH PHIM BAN ĐẦU")
movie_list.display_movie()

# Thêm phim vào danh sách
movie_list.add_movie(movie1)
movie_list.add_movie(movie2)
movie_list.add_movie(movie3)
movie_list.add_movie(movie4)
print("\n-----------------------")
print("DANH SÁCH PHIM SAU KHI THÊM PHIM MỚI")
movie_list.display_movie()

# Xoá phim khỏi danh sách
movie_list.remove_movie("Cô dâu 8 tuổi")
print("\n-----------------------")
print("DANH SÁCH PHIM SAU KHI XOÁ PHIM")
movie_list.display_movie()

# Tìm kiếm phim
result_movie = movie_list.search_movie("kungfu")
print("\n-----------------------")
print("DANH SÁCH PHIM SAU KHI TÌM KIẾM PHIM")
for movie in result_movie:
    print(movie.title)

# Sắp xếp phim theo tên từ A -> Z
movie_list.sort_movie(key = "title")
print("\n-----------------------")
print("DANH SÁCH PHIM SAU KHI SẮP XẾP PHIM THEO TÊN")
movie_list.display_movie()

# Sắp xếp phim theo điểm đánh giá
movie_list.sort_movie(key = "rating")
print("\n-----------------------")
print("DANH SÁCH PHIM SAU KHI SẮP XẾP PHIM THEO ĐIỂM ĐÁNH GIÁ")
movie_list.display_movie()

# Sắp xếp phim theo ngày phát hành
movie_list.sort_movie(key = "release_date")
print("\n-----------------------")
print("DANH SÁCH PHIM SAU KHI SẮP XẾP PHIM THEO NGÀY PHÁT HÀNH")
movie_list.display_movie()