import json

# Khởi tạo class Movies
class Movies:
    def __init__(self, id, title, release_date, rating = None, link = None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.rating = rating
        self.link = link
        
    def to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "release_date" : self.release_date,
            "rating" : self.rating,
            "link" : self.link
        }
    
    def update(self, new_title, new_release_date,  new_rating= None, new_link = None):
        self.title = new_title
        self.release_date = new_release_date
        self.rating = new_rating
        self.link = new_link
        
# Khởi tạo class MovieList
class MovieList:
    def __init__(self):
        self.movie_list = []

    # Thêm phim mới
    def add_movie(self, movie):
        self.movie_list.append(movie)
        self.save_to_json()

    # Xoá phim
    def remove_movie(self, identifier):
        for movie in self.movie_list:
            if movie.title == identifier or movie.id == identifier:
                self.movie_list.remove(movie)
        self.save_to_json()

    # Tìm kiếm phim
    def search_movie(self, title):
        return [movie for movie in self.movie_list if title.lower() in movie.title.lower()]
    
    # Cập nhật phim
    def update_movie(self, movie_id, new_title, new_release_date, new_rating = None, new_link = None):
        for movie in self.movie_list:
            if movie.id == movie_id:
                movie.update(new_title, new_release_date, new_rating, new_link)
                self.save_to_json()
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

    # def display_movie(self):
    #     for movie in self.movie_list:
    #         print(f"{movie.id} - {movie.title} - {movie.release_date} - {movie.rating} - {movie.link}")

    # Chuyển dữ liệu từ dictionary thành object
    def create_movie_from_dict(self, data):
        return Movies(data["id"], data["title"], data["release_date"], data["rating"], data["link"])

    def save_to_json(self):
        with open("Lesson8/data.json", "w", encoding="utf-8") as file:
            json.dump([movie.to_dict() for movie in self.movie_list], file, indent=4, ensure_ascii=False)

    def load_from_json(self):
        with open("Lesson8/data.json", "r", encoding="utf-8") as file:
            data = json.load(file) # lưu dữ liệu từ json vào biến data
            self.movie_list = [self.create_movie_from_dict(movie) for movie in data]

    # Lấy ra danh sách tên các bộ phim
    def get_title_list(self):
        return [movie.title for movie in self.movie_list]
    
    def get_first_movie_by_title(self, movie_title):
        for movie in self.movie_list:
            if movie.title == movie_title:
                return movie
        return False