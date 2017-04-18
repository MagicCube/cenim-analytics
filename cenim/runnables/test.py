# -*- coding: utf-8 -*-
# Module: cenim.runnable.test

import numpy as np

from cenim.data.movie_data import MOVIE_FEATURE_SIZE, get_all_movies, merge_movie_features
from cenim.utils import load_data


checkpoint = load_data('models/checkpoint')
weight = np.array(checkpoint['weights'])


def run():
    INPUT_MOVIE_IDS = ["1291583", "1308807", "1297359", "1291585", "1293318"]
    user_features = np.concatenate([merge_movie_features(INPUT_MOVIE_IDS), np.zeros([MOVIE_FEATURE_SIZE])])
    movies = get_all_movies()
    for movie in movies:
        movie_feature = movie['feature']
        user_movie_features = np.array([np.concatenate([user_features, movie_feature])])
        y = np.matmul(user_movie_features, weight)
        movie['rate'] = {
            'like': y[0, 0],
            'dislike': y[0, 1],
            'value': y[0, 0] - y[0, 1]
        }
    movies.sort(key=lambda movie: movie['rate']['value'], reverse=True)
    for movie in movies:
        print(movie['title'])
