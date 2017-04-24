# -*- coding: utf-8 -*-
# Module: cenim.data.input_data

import numpy as np

from cenim.utils import load_data

from . import movie_data as md
from . import user_data as ud

# Global Variables
__samples = []


class Datasets(object):
    def __init__(self, train_samples, test_samples):
        self.train = TrainingDataSet(train_samples)
        self.test = Datasets.samples_to_xy_array(test_samples)

    @staticmethod
    def samples_to_xy_array(samples):
        X = []
        Y = []
        for sample in samples:
            X.append(sample['x'])
            Y.append(sample['y'])
        return (np.array(X), np.array(Y))


class TrainingDataSet(object):
    def __init__(self, train_samples):
        self.__samples = train_samples

    def next_batch(self, count):
        return Datasets.samples_to_xy_array(
            np.random.choice(self.__samples, count)
        )


def __initial_load():
    print('Loading input samples...\n')
    for rating in load_data('ratings'):
        user_id = rating['sessionId']
        rating_value = rating['value']
        if ud.has_user(user_id) and (rating_value == -1 or rating_value == 1 or rating_value == 0):
            movie_id = rating['movieId']
            if rating_value == 1:
                label = [1, 0, 0]
            elif rating_value == 0:
                label = [0, 1, 0]
            elif rating_value == -1:
                label = [0, 0, 1]
            __samples.append({
                'x': ud.combine_user_and_movie_feature(user_id, movie_id),
                'y': label
            })
    print('[Done] Input samples has been loaded.')


def gen_datasets(training_percentage=0.8):
    samples = __samples[:]
    # 80% for training, 20% for test/validation
    training_count = int(len(samples) * training_percentage)
    np.random.shuffle(samples)
    return Datasets(
        samples[0:training_count],
        samples[training_count:]
    )


if len(__samples) == 0:
    __initial_load()
