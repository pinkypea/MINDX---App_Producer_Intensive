import json

# Class Movies để khởi tạo các bộ phim
class Movies:
    def __init__(self, id, title, release_date, rating = None, link = None):
        self.id = int(id) if id else 0
        self.title = title
        self.release_date = release_date
        self.rating = float(rating) if rating else 0
        self.link = link

    def to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "release_date" : self.release_date,
            "rating" : self.rating,
            "link" : self.link
        }
    
    def update(self, new_title, new_release_date, new_rating = None, new_link = None):
        self.title = new_title
        self.release_date = new_release_date
        self.rating = new_rating
        self.link = new_link

# Class MoviesList để quản lý danh sách phim
class MoviesList:
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

    # Cập nhật phim
    def update_movie(self, movie_id, new_title, new_release_date, new_rating = None, new_link = None):
        for movie in self.movie_list:
            if movie.id == movie_id:
                movie.update(new_title, new_release_date, new_rating, new_link)
                self.save_to_json()
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

    def save_to_json(self):
        with open("./Buoi9/data.json", "w", encoding="utf-8") as file:
            json.dump([movie.to_dict() for movie in self.movie_list], file, indent=4 ,ensure_ascii=False)

    def load_from_json(self):
        with open("./Buoi9/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            self.movie_list = [self.create_movie_from_dict(movie) for movie in data]

    def create_movie_from_dict(self, data):
        return Movies(data["id"], data["title"], data["release_date"], data.get("rating"), data.get("link"))
    
    def get_movie_title_list(self):
        return [movie.title for movie in self.movie_list]
    
    def get_first_item_by_title(self, movie_title):
        for movie in self.movie_list:
            if movie.title == movie_title:
                return movie
            return False