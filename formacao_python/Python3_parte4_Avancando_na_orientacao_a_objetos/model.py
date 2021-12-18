class Movie:

    def __init__(self, name, year, duration):
        self.name = name
        self.year = year
        self.duration = duration


class Serie:

    def __init__(self, name, year, seasons):
        self.name = name
        self.year = year
        self.seasons = seasons

avengers = Movie('avengers - infinity war', 2018, 160)
print(f'Name: {avengers.name} - Year: {avengers.year} - Duration: {avengers.duration}')

theWitcher = Serie('the witcher', 2019, 2)
print(f'Name: {theWitcher.name} - Year: {theWitcher.year} - Seasons: {theWitcher.seasons}')