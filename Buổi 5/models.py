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

# Lưu trữ class danh sách phim
class MovieList:
    def __init__(self):
        self.movie_list = []

    def add_movie(self, movie):
        self.movie_list.append(movie)

    def remove_movie(self, identifier):
        self.movie_list = [movie for movie in self.movie_list if movie.title != identifier]

    def search_movie(self, title):
        return [movie for movie in self.movie_list if title.lower() in movie.title.lower()]
    
    def update_movie(self, movie_id, new_id, new_title, new_release_date=None, new_rating=None, new_link=None):
        for movie in self.movie_list:
            if movie.id == movie_id:
                movie.id = new_id
                movie.title = new_title
                if new_release_date:
                    movie.release_date = new_release_date
                if new_rating:
                    movie.rating = float(new_rating)
                if new_link:
                    movie.link = new_link
                return True
        return False
    
    def display_movie(self):
        for movie in self.movie_list:
            print(f"{movie.id} - {movie.title} - {movie.release_date} - {movie.rating}")

    def save_to_json(self, filename="data.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([movie.transfer_to_dict() for movie in self.movie_list], file, indent=4, ensure_ascii=False)

    def load_from_json(self, filename="data.json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.movie_list = [self.create_movie_from_dict(movie) for movie in data]

    def create_movie_from_dict(self, data):
        return Movies(data["id"], data["title"], data["release_date"], data["rating"], data["link"])
    

# Tạo danh sách phim
movie_list = MovieList()

# Thêm phim vào danh sách
movie1 = Movies("001", "Iron Man", "16/05/2008")
movie2 = Movies("002", "Black Panther", "16/02/2018")
movie3 = Movies("003", "Love Rosie", "24/10/2014")
movie4 = Movies("004", "Mật mã Lyoko", "03/09/2003")

movie_list.add_movie(movie1)
movie_list.add_movie(movie2)
movie_list.add_movie(movie3)
movie_list.add_movie(movie4)

print("\nXEM DANH SÁCH PHIM BAN ĐẦU")
movie_list.display_movie()
movie_list.save_to_json()


movie_list.remove_movie("Black Panther")
print("\nXEM DANH SÁCH PHIM SAU KHI XOÁ")
movie_list.display_movie()
movie_list.save_to_json()

result_movie = movie_list.search_movie("iron")
print("\nKẾT QUẢ TÌM KIẾM PHIM")
for movie in result_movie:
    print(movie.title)

movie_list.update_movie("001", "010", "Avengers", "27/04/2012")
movie_list.save_to_json()
