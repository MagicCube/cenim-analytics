# -*- coding: utf-8 -*-
# Module: cenim.tests.dnn.train

import numpy as np
import tensorflow as tf

from cenim.data import input_data, MOVIE_FEATURE_SIZE
from cenim.models import DnnClassifier


def build_dnn(sess):
    print('Building DNN...')
    n_input = MOVIE_FEATURE_SIZE * 3
    n_classes = 2
    # Build a 3 layers DNN classifier
    dnn = DnnClassifier(sess, n_input, n_classes)
    dnn.add_output_layer(tf.nn.softmax)
    print('[DONE] - DNN has been built.\n')
    return dnn


def run():
    with tf.Session() as sess:
        # Build DNN and initialize Tensorflow
        dnn = build_dnn(sess)
        sess.run(tf.global_variables_initializer())
        # Generate datasets
        datasets = input_data.gen_datasets()
        # Start Training
        N_ITERATION = 2000
        print('Training(' + str(N_ITERATION) + ' steps)...')
        for i in xrange(N_ITERATION):
            (X, Y) = datasets.train.next_batch(100)
            dnn.train(X, Y)
            if i % (N_ITERATION / 5) == 0:
                test_x, test_y = datasets.test
                accuracy = dnn.compute_accuracy(test_x, test_y)
                print(str(i * 100 / N_ITERATION) + '% completed with accuracy ' + str(accuracy * 100) + '%')
        print('[Done] 100% completed')