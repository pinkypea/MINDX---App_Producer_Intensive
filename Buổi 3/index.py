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

movie1 = Movies("001", "Avengers", "27/04/2012", 8.0)
movie1.show()
movie1.update("Avengers: End game", "26/04/2019", 8.4)
movie1.show()