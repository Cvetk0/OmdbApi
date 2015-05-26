"""
OMDB Entities
"""

class Movie():
    def __init__(self, movie_dict):
        """
        :param movie_dict: OMDB movie dictionary
        """
        self.actors = movie_dict['Actors']
        self.awards = movie_dict['Awards']
        self.country = movie_dict['Country']
        self.director = movie_dict['Director']
        self.genres = movie_dict['Genre'].split(', ')
        self.language = movie_dict['Language']
        self.metascore = movie_dict['Metascore']
        self.plot = movie_dict['Plot']
        self.poster = movie_dict['Poster']
        self.rating = movie_dict['Rated']
        self.released = movie_dict['Released']
        self.runtime = movie_dict['Runtime']
        self.title = movie_dict['Title']
        self.type = movie_dict['Type']
        self.writer = movie_dict['Writer']
        self.year = movie_dict['Year']
        self.imdbId = movie_dict['imdbID']
        self.imdbRating = movie_dict['imdbRating']
        self.imdbVotes = movie_dict['imdbVotes']

    def __str__(self):
        movie = ''
        for param in dir(self):
            if param[0] != '_':
                movie += (param + ': ' + str(getattr(self, param)) + '\n')
        return movie


class Episode():
    def __init__(self, episode_dict):
        """
        :param episode_list: OMDB episode dictionary
        """
        self.actors = episode_dict['Actors']
        self.awards = episode_dict['Awards']
        self.country = episode_dict['Country']
        self.director = episode_dict['Director']
        self.episode = episode_dict['Episode']
        self.genres = episode_dict['Genre'].split(', ')
        self.language = episode_dict['Language']
        self.metascore = episode_dict['Metascore']
        self.plot = episode_dict['Plot']
        self.poster = episode_dict['Poster']
        self.rating = episode_dict['Rated']
        self.released = episode_dict['Released']
        self.runtime = episode_dict['Runtime']
        self.season = episode_dict['Season']
        self.title = episode_dict['Title']
        self.type = episode_dict['Type']
        self.writer = episode_dict['Writer']
        self.year = episode_dict['Year']
        self.imdbId = episode_dict['imdbID']
        self.imdbRating = episode_dict['imdbRating']
        self.imdbVotes = episode_dict['imdbVotes']

    def __str__(self):
        movie = ''
        for param in dir(self):
            if param[0] != '_':
                movie += (param + ': ' + str(getattr(self, param)) + '\n')
        return movie