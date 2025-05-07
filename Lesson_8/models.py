import json

# Lưu trữ class phim
class Movies:
    def __init__(self, id, title, release_date, rating=None, link=None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.rating = float(rating) if rating else 0
        self.link = link

    # Chuyển đổi các object thành kiểu dữ liệu dictionary
    def transfer_to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "release_date": self.release_date,
            "rating" : self.rating,
            "link": self.link
        }
    
    def update(self, new_title, new_release_date, new_rating = None, new_link = None):
        self.title = new_title
        self.release_date = new_release_date
        self.rating = new_rating
        self.link = new_link

# Lưu trữ class danh sách phim
class MovieList:
    def __init__(self):
        self.movie_list = []

    def add_movie(self, movie):
        self.movie_list.append(movie)
        self.save_to_json()

    def remove_movie(self, identifier):
        self.movie_list = [movie for movie in self.movie_list if movie.title != identifier]
        self.save_to_json()

    def search_movie(self, title):
        return [movie for movie in self.movie_list if title.lower() in movie.title.lower()]
    
    def update_movie(self, movie_id, new_title, new_release_date, new_rating = None, new_link = None):
        for movie in self.movie_list:
            if movie.id == movie_id:
                movie.update(new_title, new_release_date, new_rating, new_link)
                self.save_to_json()
                return True
        return False

    def display_movie(self):
        for movie in self.movie_list:
            print(f"{movie.id} - {movie.title} - {movie.release_date} - {movie.rating}")

    def save_to_json(self, filename="Lesson_8/data.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([movie.transfer_to_dict() for movie in self.movie_list], file, indent=4, ensure_ascii=False)

    def load_from_json(self, filename="Lesson_8/data.json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.movie_list = [self.create_movie_from_dict(movie) for movie in data]

    def create_movie_from_dict(self, data):
        return Movies(data["id"], data["title"], data["release_date"], data["rating"], data["link"])
    
    def get_title_list(self):
        return [movie.title for movie in self.movie_list]
    
    def get_first_item_by_title(self, movie_title):
        for movie in self.movie_list:
            if movie.title == movie_title:
                return movie
            return False