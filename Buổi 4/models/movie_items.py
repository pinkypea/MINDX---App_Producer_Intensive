# Lưu trữ class phim
class Movies:
    def __init__(self, id, title, release_date, rating=None, link=None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.rating = float(rating) if rating else 0
        self.link = link

    # def update(self, new_id, new_title, new_release_date, new_rating=None, new_link=None):
    #     self.id = new_id
    #     self.title = new_title
    #     self.release_date = new_release_date
    #     self.rating = new_rating
    #     self.link = new_link