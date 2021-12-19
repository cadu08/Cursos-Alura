class Media:

    def __init__(self, name, year):
        self._name = name.title()
        self._year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def add_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()


class Movie(Media):

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration


class Serie(Media):

    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


avengers = Movie('avengers - infinity war', 2018, 160)
print(f'Name: {avengers.name} - Likes: {avengers.likes}')

theWitcher = Serie('the witcher', 2019, 2)

theWitcher.add_like()

print(f'Name: {theWitcher.name} - Likes: {theWitcher.likes}')