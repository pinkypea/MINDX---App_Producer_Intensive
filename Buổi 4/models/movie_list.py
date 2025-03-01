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

movie_list.update_movie("001", "010", "Avengers", "27/04/2012")