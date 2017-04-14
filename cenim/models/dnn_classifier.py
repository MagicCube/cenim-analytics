# -*- coding: utf-8 -*-
# Module: cenim.nn.Dnn

import tensorflow as tf


class DnnClassifier(object):
    def __init__(self, session, n_input, n_classes):
        self.session = session
        self.n_input = n_input
        self.n_classes = n_classes
        self.n_input = n_input
        self.input_x = tf.placeholder(tf.float32, [None, n_input])
        self.input_y = tf.placeholder(tf.float32, [None, n_classes])
        self.__output_layer = self.input_x
        self.__output_layer_size = n_input
        self.__prediction = None
        self.__train_step = None

    def add_layer(self, size, activation_function=None):
        weights = tf.Variable(tf.random_normal([self.__output_layer_size, size]))
        biases = tf.Variable(tf.zeros([1, size]) + 0.1,)
        wx_plus_b = tf.matmul(self.__output_layer, weights) + biases
        if activation_function is None:
            outputs = wx_plus_b
        else:
            outputs = activation_function(wx_plus_b)
        pass
        self.__output_layer = outputs
        self.__output_layer_size = size
        return self.__output_layer

    def add_hidden_layer(self, n_neuron, activation_function=tf.nn.tanh):
        self.add_layer(n_neuron, activation_function=None)

    def add_output_layer(self, activation_function=None):
        self.__prediction = self.add_layer(self.n_classes, activation_function=tf.nn.softmax)
        loss = DnnClassifier.create_loss_func(self.input_y, self.__prediction)
        self.__train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

    @staticmethod
    def create_loss_func(input, prediction):
        # Cross entropy
        return tf.reduce_mean(-tf.reduce_sum(input * tf.log(prediction), reduction_indices=[1]))

    def train(self, x, y):
        if self.__train_step is None:
            raise Exception('Please add output layer before training.')
        self.session.run(
            self.__train_step,
            feed_dict={self.input_x: x, self.input_y: y}
        )
        pass
