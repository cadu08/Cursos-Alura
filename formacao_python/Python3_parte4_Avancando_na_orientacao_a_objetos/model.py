class Movie:

    def __init__(self, name, year, duration):
        self.name = name.title()
        self.year = year
        self.duration = duration
        self.likes = 0

    def add_like(self):
        self.likes += 1


class Serie:

    def __init__(self, name, year, seasons):
        self.name = name.title()
        self.year = year
        self.seasons = seasons
        self.likes = 0

    def add_like(self):
        self.likes += 1

avengers = Movie('avengers - infinity war', 2018, 160)
print(f'Name: {avengers.name} - Year: {avengers.year} - Duration: {avengers.duration}')

theWitcher = Serie('the witcher', 2019, 2)
print(f'Name: {theWitcher.name} - Year: {theWitcher.year} - Seasons: {theWitcher.seasons}')