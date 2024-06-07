class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artist(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, song):
        cls.genres.append(song.genre)

    @classmethod
    def add_to_genre_count(cls, song):
        if song.genre in cls.genre_count:
            current_val = cls.genre_count[f'{song.genre}']
            cls.genre_count[f'{song.genre}'] = current_val + 1
        else:
            cls.genre_count[f'{song.genre}'] = 1

    @classmethod
    def add_to_artist(cls, song):
        cls.artists.append(song.artist)

    @classmethod
    def add_to_artist_count(cls, song):
        if song.artist in cls.artist_count:
            current_val = cls.artist_count[f'{song.artist}']
            cls.artist_count[f'{song.artist}'] = current_val + 1
        else:
            cls.artist_count[f'{song.artist}'] = 1
