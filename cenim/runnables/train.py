# -*- coding: utf-8 -*-
# Module: cenim.tests.dnn.train

import os.path

import numpy as np
import tensorflow as tf

from cenim.data import input_data, MOVIE_FEATURE_SIZE
from cenim.models import DnnClassifier


# Constants
MODEL_PATH = './data/models/dnn.ckpt'

# Global Variables
__saver = None


def build_model(sess):
    print('Building DNN model...')
    n_input = MOVIE_FEATURE_SIZE * 3
    n_classes = 2
    # Build a 3 layers DNN classifier
    dnn = DnnClassifier(sess, n_input, n_classes)
    dnn.add_output_layer(tf.nn.softmax)
    print('[DONE] - DNN model has been built.\n')
    return dnn


def load_model(sess):
    print("Loading model from file: %s..." % MODEL_PATH)
    __saver.restore(sess, MODEL_PATH)
    pass


def save_model(sess):
    __saver.save(sess, MODEL_PATH)
    print("[Done] Model saved in file: %s." % MODEL_PATH)


def train(sess, dnn):
    # Generate datasets
    datasets = input_data.gen_datasets(0.8)
    # Start Training
    N_ITERATION = 5000
    print('Training(' + str(N_ITERATION) + ' steps)...')
    for i in xrange(N_ITERATION):
        (X, Y) = datasets.train.next_batch(100)
        dnn.train(X, Y)
        if i % (N_ITERATION / 5) == 0:
            test_x, test_y = datasets.test
            accuracy = dnn.compute_accuracy(test_x, test_y)
            print(str(i * 100 / N_ITERATION) + '% completed with accuracy ' + str(accuracy * 100) + '%')
    print('[Done] 100% completed')
    save_model(sess)


def run():
    global __saver
    with tf.Session() as sess:
        # Build DNN and initialize Tensorflow
        dnn = build_model(sess)
        # Restore model from local or initialize for the
        # first time
        __saver = tf.train.Saver()
        if not(os.path.exists(MODEL_PATH + '.index')):
            sess.run(tf.global_variables_initializer())
        else:
            load_model(sess)
        # Start training
        train(sess, dnn)
        # Save model
        save_model(sess)
