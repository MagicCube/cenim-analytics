# -*- coding: utf-8 -*-
# Package: cenim.nn

import tensorflow as tf

import cenim.data.movie_data as md
import cenim.data.user_data as ud

from dnn import DnnClassifier


def build_dnn():
    print('Building DNN...')
    n_input = md.MOVIE_FEATURE_SIZE * 3
    n_classes = 2
    dnn = DnnClassifier(n_input, n_classes)
    print('[DONE] - DNN has been built.\n')
    pass


def run():
    build_dnn()
    pass
