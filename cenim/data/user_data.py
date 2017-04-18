# -*- coding: utf-8 -*-
# Module cenim.data.user_data

import numpy as np

from cenim.utils import load_data

import movie_data as md


# Global Variables
__users = []
__user_dict = {}


def __initial_load():
    print('Loading users...')
    for user_movies in load_data('user-movie'):
        user = gen_user(user_movies)
        __users.append(user)
        __user_dict[user['id']] = user
    print('[DONE] - %d users were loaded.\n' % len(__users))


def gen_user(user_movies):
    user = {
        'id': user_movies['id']
    }
    likes = md.merge_movie_features(user_movies['likes'])
    dislikes = md.merge_movie_features(user_movies['dislikes'])
    skips = md.merge_movie_features(user_movies['skips'])
    user['feature'] = np.concatenate([likes, dislikes, skips])
    return user


def has_user(id):
    return id in __user_dict


def get_user(id):
    if id in __user_dict:
        return __user_dict[id]
    else:
        return None


def get_user_feature(id):
    user = get_user(id)
    if user:
        return user['feature']
    else:
        return None


def combine_user_and_movie_feature(user_id, movie_id):
    user_feature = get_user_feature(user_id)
    if user_feature is not None:
        movie_feature = md.get_movie_feature(movie_id)
        if movie_feature is not None:
            return np.concatenate([user_feature, movie_feature])
        else:
            return None
    else:
        return None


if len(__users) == 0:
    __initial_load()
