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

    def show(self):
        print(self.id, self.title, self.release_date, self.rating, self.link)

# Tạo các bộ phim
movie1 = Movies("001", "Avengers", "27/04/2012", 8.0)
movie2 = Movies("002", "Justice league", "17/11/2017", 6.0)
movie3 = Movies("003", "Cô dâu 8 tuổi", "21/07/2018")
movie4 = Movies("004", "Kungfu Panda", "27/06/2008", 7.6)

# Tạo danh sách phim
movie_list = [movie1, movie2, movie3, movie4]

# Duyệt danh sách
print("\n-----------------------------", "\nDANH SÁCH PHIM BAN ĐẦU")
for movie in movie_list:
    print(f"{movie.id} - {movie.title}")

# Thêm phần tử mới vào danh sách
movie5 = Movies("005", "Gia đình Simpson", "17/12/1989")
movie_list.append(movie5)
print("\n-----------------------------", "\nKẾT QUẢ SAU KHI THÊM PHIM MỚI")
for movie in movie_list:
    print(f"{movie.id} - {movie.title}")

# Xoá phần tử khỏi danh sách
remove_title = "Avengers"
for movie in movie_list:
    if movie.title == remove_title:
        movie_list.remove(movie)

print("\n-----------------------------", "\nKẾT QUẢ SAU KHI XOÁ PHIM")
for movie in movie_list:
    print(f"{movie.id} - {movie.title}")