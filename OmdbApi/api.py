"""
Open Movie Database API client
** http://www.omdbapi.com/ **

Requirements:
requests module

Provides following functionalities:
- Retrieval of movies by IMDB ID
- Retrieval of movies by title (search string)
- Retrieval of series' single  episode
- Retrieval of series season
- Retrieval of series' multiple  episodes

Author: Jernej Kladnik - cvetk0 at gmail.com
"""

import requests

from OmdbApi.entities import Movie


class Client():
    def __init__(self, download_image=False):
        self.host = 'http://www.omdbapi.com/'
        self.dl_image = download_image

    def movie_by_ids(self, movie_id_list):
        """
        Retrieves single or mutliple movies information from IMDB based on IMDB ID
        :type movie_id_list: list
        :param movie_id_list: single IMDB movie ID or list of IMDB movie IDs
        :return: list of tuples (movie_info, image_link)
        :rtype: list
        """
        if isinstance(movie_id_list, list):
            ids = movie_id_list
        else:
            raise ValueError('Input must be a list of IMDB movie IDs')

        movie_list = self._get_movies(ids)

        if not movie_list:
            print "No movies found"

        return movie_list

    def movies_by_titles(self, movie_title_list):
        """
        Retrieves single or mutliple movies information from IMDB based on title (search string), returns
        empty tuple if none found
        :type movie_title_list: list
        :param movie_title_list: movie title
        :return: list of movies
        :rtype: list
        """
        if isinstance(movie_title_list, list):
            titles = movie_title_list
        else:
            raise ValueError('Input must be a list of titles')

        movie_list = self._get_movies(titles, query_type='title')

        if not movie_list:
            print "No movies found"

        return movie_list

    def series_episode(self, title, season, episode):
        """
        Retrieves single episode of the series
        :type season: int
        :type episode: int
        :param title: str - Series title
        :param season: int
        :param episode: int
        :return: series episode
        :rtype: tuple
        """
        s = int(season)
        e = int(episode)

        episode = self._get_episode(title, s, e)

        if episode is None:
            print "Episode not found"
            return episode

        return episode

    def series_season(self, title, season, number_of_episodes):
        """
        Retrieves entire series season based on number_of_episodes input parameter
        :type season: int
        :type number_of_episodes: int
        :param title:
        :param season:
        :param number_of_episodes:
        :return: series season list
        :rtype: list
        """
        episodes = []
        for episode in range(1, number_of_episodes + 1):
            e = self.series_episode(title, season, episode)
            if e is not None:
                episodes.append(e)

        if not episodes:
            print "No episodes found"

        return episodes

    def series_season_episodes(self, title, season, episode_list):
        """
        Retrieves list of series episodes based on episode_list
        :type season: int
        :type episode_list: list
        :param title:
        :param season:
        :param episode_list:
        :return: list of season episodes
        :rtype: list
        """
        episodes = []
        for episode in episode_list:
            e = self.series_episode(title, season, episode)
            if e is not None:
                episodes.append(e)

        if not episodes:
            print "No episodes found"

        return episodes

    def _get_movies(self, movie_list, query_type='id'):
        """
        Retrieves list of movies based on query_type parameter
        :type movie_list: list
        :type query_type: str
        :param movie_list: list of movies to retrieve
        :param query_type: type of query to perform
        :return:
        :rtype : Movie
        """
        types = ('id', 'title')
        p = ''
        movies = []

        if query_type not in types:
            raise ValueError('Invalid query_type, supported types are %r' % str(types))
        for movie in movie_list:
            if query_type == 'id':
                p = dict(i=movie)
            elif query_type == 'title':
                p = dict(t=movie)

            m = self._get(p)
            if 'Error' in m:
                print 'Error retrieving movie by title %r: %s' % (movie, m['Error'])
            else:
                #movies.append((m, m['Poster']))
                movies.append(Movie(m))

        return movies

    def _get_episode(self, title, season, episode):
        """
        Retrieves single series episode
        :type title: str
        :type season: int
        :type episode int
        :param title: series title
        :param season: season number
        :param episode: episode number
        :return: episode information
        :rtype tuple
        """
        p = dict(t=title, Season=season, Episode=episode)
        e = self._get(p)
        episode_data = None

        if 'Error' in e:
            print 'Error retrieving series: %r season: %s episode: %s' % (title, str(season), str(episode))
        else:
            episode_data = (e, e['Poster'])

        return episode_data

    def _get(self, params):
        """
        OMDB API query method
        :param params: query parameters as defined in OMDB API specification
        :return: API result
        :rtype: dict
        """
        r = requests.get(self.host, params=params)
        return r.json()