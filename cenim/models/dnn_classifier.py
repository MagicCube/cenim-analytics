# -*- coding: utf-8 -*-
# Module: cenim.models.DnnClassifier

import tensorflow as tf

from .classifier import Classifier


class DnnClassifier(Classifier):
    def __init__(self, session, n_input, n_classes):
        super(DnnClassifier, self).__init__(session, n_input, n_classes)
        self.__output_layer = self.input_x
        self.__output_layer_size = n_input
        self._prediction = None
        self._train_step = None

    def add_layer(self, size, activation_function=None,):
        weights = tf.Variable(tf.random_normal([self.__output_layer_size, size]))
        biases = tf.Variable(tf.zeros([1, size]) + 0.1,)
        wx_plus_b = tf.matmul(self.__output_layer, weights) + biases
        wx_plus_b = tf.nn.dropout(wx_plus_b, self.keep_prob)
        if activation_function is None:
            outputs = wx_plus_b
        else:
            outputs = activation_function(wx_plus_b,)
        self.__output_layer = outputs
        self.__output_layer_size = size
        return (weights, biases)

    def add_hidden_layer(self, n_neuron, activation_function=None):
        (weights, biases) = self.add_layer(n_neuron, activation_function=None)
        return (weights, biases)

    def add_output_layer(self, activation_function=None):
        (weights, biases) = self.add_layer(self.n_classes, activation_function)
        self._prediction = self.__output_layer
        cross_entropy = -tf.reduce_sum(self.input_y * tf.log(tf.clip_by_value(self._prediction, 1e-10, 1.0)))
        self._train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)
        return (weights, biases)

    def get_prediction(self):
        if self._prediction is None:
            raise Exception('Please add output layer before training.')
        return self._prediction

    def get_train_step(self):
        if self._train_step is None:
            raise Exception('Please add output layer before training.')
        return self._train_step
