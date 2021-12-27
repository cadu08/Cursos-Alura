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


class Playlist():

    def __init__(self, name, medias):
        self.name = name
        self._medias = medias

    def __getitem__(self, item):
        return self._medias[item]

    def __len__(self):
        return len(self._medias)


avengers = Movie('avengers - infinity war', 2018, 160)
lalaland = Movie('La La Land', 2016, 168)
shawshank = Movie('the shawshank redemption', 1994, 182)
shape_water = Movie('the shape of water', 2017, 163)
moonlight = Movie('moonlight', 2016, 110)
the_artist = Movie('the artist', 1927, 100)

the_witcher = Serie('the witcher', 2019, 2)
the_untamed = Serie('the untamed', 2019, 1)
my_country = Serie('my country: the new age', 2019, 1)
xena = Serie('xena: warrior princess', 1995, 6)
chris = Serie('everybody hates chris', 2005, 4)
the_crown = Serie('the crown', 2016, 4)
sense8 = Serie('sense8', 2015, 2)
dark = Serie('dark', 2017, 3)
stranger_things = Serie('stranger things', 2016, 3)

the_untamed.add_like()
the_untamed.add_like()
the_untamed.add_like()
the_untamed.add_like()
the_untamed.add_like()
the_untamed.add_like()

moonlight.add_like()
moonlight.add_like()
moonlight.add_like()
moonlight.add_like()
moonlight.add_like()

xena.add_like()
xena.add_like()
xena.add_like()

the_witcher.add_like()
the_witcher.add_like()

medias_list = [avengers, the_witcher, the_untamed, xena]
weekend_playlist = Playlist('Weekend', medias_list)

print(f'Playlist length: {len(weekend_playlist)}')

for media in weekend_playlist:
    print(media)