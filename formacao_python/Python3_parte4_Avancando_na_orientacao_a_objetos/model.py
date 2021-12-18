class Movie:

    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def add_like(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()

class Serie:

    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def add_like(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()

avengers = Movie('avengers - infinity war', 2018, 160)
print(f'Name: {avengers.name} - Year: {avengers.year} - Duration: {avengers.duration} - Likes: {avengers.likes}')

theWitcher = Serie('the witcher', 2019, 2)

theWitcher.add_like()

print(f'Name: {theWitcher.name} - Year: {theWitcher.year} - Seasons: {theWitcher.seasons} - Likes: {theWitcher.likes}')