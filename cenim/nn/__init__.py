# -*- coding: utf-8 -*-
# Package: cenim.nn

import numpy as np
import tensorflow as tf

import cenim.data.movie_data as md
import cenim.data.user_data as ud
from cenim.utils import load_data

from dnn import DnnClassifier


def build_dnn(sess):
    print('Building DNN...')
    n_input = md.MOVIE_FEATURE_SIZE * 3
    n_classes = 2
    dnn = DnnClassifier(sess, n_input, n_classes)
    dnn.add_hidden_layer(md.MOVIE_FEATURE_SIZE)
    dnn.add_output_layer()
    print('[DONE] - DNN has been built.\n')
    return dnn


def gen_training_data():
    X = []
    Y = []
    print('Generating training data...\n')
    for rating in load_data('ratings'):
        user_id = rating['sessionId']
        rating_value = rating['value']
        if ud.has_user(user_id) and (rating_value == -1 or rating_value == 1):
            movie_id = rating['movieId']
            x = ud.combine_user_and_movie_feature(user_id, movie_id)
            X.append(x)
            if rating_value == 1:
                Y.append([1, 0])
            elif rating_value == -1:
                Y.append([0, 1])
    print('[Done] Training data has been generated.')
    return (np.array(X), np.array(Y))


def run():
    (X, Y) = gen_training_data()
    with tf.Session() as sess:
        dnn = build_dnn(sess)
        sess.run(tf.global_variables_initializer())
        print(''.join(['Training(', str(len(X)), ' steps)...']))
        dnn.train(X, Y)
        print('[Done] Training completed.')
