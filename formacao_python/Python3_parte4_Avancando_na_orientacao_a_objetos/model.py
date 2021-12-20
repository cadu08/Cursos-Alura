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

    def __str__(self):
        return f'Name: {self.name} Likes: {self.likes}'


class Movie(Media):

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'Name: {self.name} - Duration: {self.duration} min - Likes: {self.likes}'


class Serie(Media):

    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Name: {self.name} - Seasons: {self.seasons} - Likes: {self.likes}'


avengers = Movie('avengers - infinity war', 2018, 160)
theWitcher = Serie('the witcher', 2019, 2)
theWitcher.add_like()

list = [avengers, theWitcher]

for media in list:
    print(media)