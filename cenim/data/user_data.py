# -*- coding: utf-8 -*-
# Module cenim.data.user_data

import numpy as np

from cenim.utils import load_data

import movie_data as md


# Global Variables
users = []
user_dict = {}


def __load_users():
    global user_dict
    print('Loading users...')
    for user_movies in load_data('user-movie'):
        user = gen_user(user_movies)
        users.append(user)
        user_dict[user['id']] = user
    print(''.join(['[DONE] - ', str(len(users)), ' users were loaded.\n']))


def gen_user(user_movies):
    user = {
        'id': user_movies['id']
    }
    likes = md.merge_movie_features(user_movies['likes'])
    dislikes = md.merge_movie_features(user_movies['dislikes'])
    user['feature'] = np.concatenate([likes, dislikes])
    return user


if len(users) == 0:
    __load_users()
