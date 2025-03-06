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
    # def sort_movie():

    def display_movie(self):
        for movie in self.movie_list:
            print(f"{movie.id} - {movie.title} - {movie.release_date} - {movie.rating} - {movie.link}") 