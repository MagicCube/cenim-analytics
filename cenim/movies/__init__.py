# -*- coding: utf-8 -*-
# Package cenim.movies

import codecs
import numpy as np
import json


# Constants
MOVIE_VECTOR_SIZE = 0

# Global Variables
movies = []
movie_dict = {}


def __load_movies():
    global movies, movie_dict, MOVIE_VECTOR_SIZE
    f = open('data/movies.json', 'r')
    movies = json.load(f, encoding='utf-8')
    f.close()
    MOVIE_VECTOR_SIZE = len(movies[0]['feature'])
    for movie in movies:
        key = movie['id']
        movie_dict[key] = movie


def get_movie(id):
    return movie_dict[id]


def get_movie_feature(id):
    movie = get_movie(id)
    if movie is None:
        return None
    else:
        return movie['feature']


def get_movies_matrix(ids):
    features = []
    for id in ids:
        feature = get_movie_feature(id)
        if not(feature is None):
            features.append(feature)
    return np.array(features)


if len(movies) == 0:
    __load_movies()
