"""
OMDB Entities
"""

class Movie():
    def __init__(self, movie_dict):
        """
        :param movie_dict: OMDB movie dictionary
        """
        self.plot = movie_dict['Plot']
        self.rating = movie_dict['Rated']
        self.language = movie_dict['Language']
        self.title = movie_dict['Title']
        self.country = movie_dict['Country']
        self.writer = movie_dict['Writer']
        self.metascore = movie_dict['Metascore']
        self.imdbRating = movie_dict['imdbRating']
        self.director = movie_dict['Director']
        self.released = movie_dict['Released']
        self.actors = movie_dict['Actors']
        self.genres = movie_dict['Genre'].split(', ')
        self.awards = movie_dict['Awards']
        self.runtime = movie_dict['Runtime']
        self.type = movie_dict['Type']
        self.poster = movie_dict['Poster']
        self.imdbVotes = movie_dict['imdbVotes']
        self.imdbId = movie_dict['imdbID']