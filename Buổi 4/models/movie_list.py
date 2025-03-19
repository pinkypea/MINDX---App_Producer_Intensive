# Lưu trữ class danh sách phim
from movie_items import Movies

class MovieList:
    def __init__(self):
        self.movie_list = []

    # Thêm phim mới vào danh sách
    def add_movie(self, movie):
        self.movie_list.append(movie)

    # Xoá phim khỏi danh sách
    def remove_movie(self, identifier):
        for movie in self.movie_list:
            if movie.title == identifier:
                self.movie_list.remove(movie)

    # Tìm kiếm phim bằng tên phim
    def search_movie(self, title):
        return [movie for movie in self.movie_list if title.lower() in movie.title.lower()]
    
    # Cập nhật phim
    def update_movie(self, movie_id, new_id, new_title, new_release_date = None, new_rating = None, new_link = None):
        for movie in self.movie_list:
            if movie.id == movie_id:
                movie.update(new_id, new_title, new_release_date, new_rating, new_link)
                return True
        return False
    
    def sort_movies(self, key="title", reverse=False):
        """Sắp xếp phim theo tiêu chí: title, rating hoặc release_date."""
        if key == "title":
            self.movie_list.sort(key=self.get_title, reverse=reverse)
        elif key == "rating":
            self.movie_list.sort(key=self.get_rating, reverse=reverse)
        elif key == "release_date":
            self.movie_list.sort(key=self.get_release_date, reverse=reverse)

    def get_title(self, movie):
        """Trả về tên phim (viết thường để sắp xếp không phân biệt chữ hoa)."""
        return movie.title.lower()

    def get_rating(self, movie):
        """Trả về điểm rating."""
        return movie.rating

    def get_release_date(self, movie):
        """Chuyển ngày tháng từ chuỗi sang dạng (năm, tháng, ngày) để sắp xếp chính xác."""
        day, month, year = map(int, movie.release_date.split("/"))
        return (year, month, day)
    
    def display_movie(self):
        for movie in self.movie_list:
            print(f"{movie.id} - {movie.title} - {movie.release_date} - {movie.rating}")

    # def sort_movie(self, key = "title", reverse = False):

movie_list = MovieList()
movie1 = Movies("001", "Iron Man", "16/05/2008")
movie2 = Movies("002", "Black Panther", "16/02/2018")
movie3 = Movies("003", "Love Rosie", "24/10/2014")
movie4 = Movies("004", "Mật mã Lyoko", "03/09/2003")

# Thêm phim vào danh sách
movie_list.add_movie(movie1)
movie_list.add_movie(movie2)
movie_list.add_movie(movie3)
movie_list.add_movie(movie4)

print("\nXEM DANH SÁCH PHIM BAN ĐẦU")
movie_list.display_movie()

movie_list.remove_movie("Black Panther")
print("\nXEM DANH SÁCH PHIM SAU KHI XOÁ")
movie_list.display_movie()

result_movie = movie_list.search_movie("iron")
print("\nKẾT QUẢ TÌM KIẾM PHIM")
for movie in result_movie:
    print(movie.title)

# Sắp xếp theo tên phim (title)
movie_list.sort_movies(key="title")
print("\nSắp xếp theo tên phim:")
movie_list.display_movie()

# Sắp xếp theo điểm rating giảm dần
movie_list.sort_movies(key="rating", reverse=True)
print("\nSắp xếp theo điểm rating giảm dần:")
movie_list.display_movie()

# Sắp xếp theo ngày phát hành (release_date)
movie_list.sort_movies(key="release_date")
print("\nSắp xếp theo ngày phát hành:")
movie_list.display_movie()