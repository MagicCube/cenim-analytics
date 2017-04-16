# -*- coding: utf-8 -*-
# Module cenim.data.movie_data

import numpy as np

from cenim.utils import load_data


# Constants
MOVIE_FEATURE_SIZE = 0

# Global Variables
__movies = []
__movie_dict = {}


def __initial_load():
    global __movies, __movie_dict, MOVIE_FEATURE_SIZE
    print('Loading movies...')
    __movies = load_data('movies')
    MOVIE_FEATURE_SIZE = len(__movies[0]['feature'])
    for movie in __movies:
        key = movie['id']
        __movie_dict[key] = movie
    print('[DONE] - %d movies were loaded.\n' % len(__movies))


def empty_movie_feature():
    return np.zeros((MOVIE_FEATURE_SIZE,), dtype=int)


def get_movie(id):
    if id in __movie_dict:
        return __movie_dict[id]
    else:
        return None


def find_movies(ids):
    movies = []
    for id in ids:
        movie = get_movie(id)
        if movie:
            movies.append(movie)
    return movies


def get_movie_feature(id):
    movie = get_movie(id)
    if movie is None:
        return None
    else:
        return np.array(movie['feature'], dtype=int)


def get_movie_features(ids):
    features = []
    movies = find_movies(ids)
    for movie in movies:
        features.append(movie['feature'])
    return np.array(features, dtype=int)


def merge_movie_features(ids):
    merged = empty_movie_feature()
    movies = find_movies(ids)
    for movie in movies:
        merged = merged | movie['feature']
    return merged


def sum_movie_features(ids):
    merged = empty_movie_feature()
    movies = find_movies(ids)
    for movie in movies:
        merged = merged + movie['feature']
    return merged


if len(__movies) == 0:
    __initial_load()
