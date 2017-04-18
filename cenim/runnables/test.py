# -*- coding: utf-8 -*-
# Module: cenim.runnable.test

import numpy as np

from cenim.data.movie_data import MOVIE_FEATURE_SIZE, get_all_movies, merge_movie_features
from cenim.utils import load_data


def run():
    checkpoint = load_data('models/checkpoint')
    weight = np.array(checkpoint['weights'])
    INPUT_MOVIE_IDS = ['1300267', '1293964', '1293839', '1294371', '1307315']
    user_likes = merge_movie_features(INPUT_MOVIE_IDS)
    user_features = np.concatenate([np.random.random([MOVIE_FEATURE_SIZE]), np.random.random([MOVIE_FEATURE_SIZE * 2])])
    movies = get_all_movies()
    for movie in movies:
        movie_feature = np.array(movie['feature'])
        user_movie_features = np.array([np.concatenate([user_features, movie_feature])])
        y = np.matmul(user_movie_features, weight)
        movie['rate'] = {
            'like': y[0, 0],
            'dislike': y[0, 2],
            'value': y[0, 0]
        }
    movies.sort(key=lambda movie: movie['rate']['value'], reverse=True)
    i = 0
    for movie in movies:
        i += 1
        if i > 10:
            break
        #print(str(i) + '. ' + movie['title'] + ', rate: ' + str(movie['rate']['value']) + ', ' + str(np.array(movie['feature']).sum()) + ' tags')
        print(str(i) + '. ' + movie['title'])
