# -*- coding: utf-8 -*-
# Module: cenim.models.Dnn

import tensorflow as tf


class DnnClassifier(object):
    def __init__(self, session, n_input, n_classes):
        self.__session = session
        self.__n_input = n_input
        self.__n_classes = n_classes
        self.input_x = tf.placeholder(tf.float32, [None, n_input])
        self.input_y = tf.placeholder(tf.float32, [None, n_classes])
        self.__output_layer = self.input_x
        self.__output_layer_size = n_input
        self.__prediction = None
        self.__train_step = None

    def add_layer(self, size, activation_function=None,):
        weights = tf.Variable(tf.random_normal([self.__output_layer_size, size]))
        biases = tf.Variable(tf.zeros([1, size]) + 0.1,)
        wx_plus_b = tf.matmul(self.__output_layer, weights) + biases
        if activation_function is None:
            outputs = wx_plus_b
        else:
            outputs = activation_function(wx_plus_b,)
        self.__output_layer = outputs
        self.__output_layer_size = size
        return self.__output_layer

    def add_hidden_layer(self, n_neuron, activation_function=None):
        self.add_layer(n_neuron, activation_function=None)

    def add_output_layer(self, activation_function=None):
        self.__prediction = self.add_layer(self.__n_classes, activation_function)
        loss = DnnClassifier.create_loss_func(self.input_y, self.__prediction)
        self.__train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    def compute_accuracy(self, x, y):
        y_pred = self.__session.run(self.__prediction, feed_dict={self.input_x: x})
        dislikes = 0
        for pred in y_pred:
            if pred[0] == 0 and pred[1] == 1:
                dislikes += 1
        print(y_pred)
        print('Dislikes: ' + str(dislikes))
        correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        result = self.__session.run(accuracy, feed_dict={self.input_x: x, self.input_y: y})
        return result

    @staticmethod
    def create_loss_func(input, prediction):
        # Cross entropy
        return -tf.reduce_sum(input * tf.log(tf.clip_by_value(prediction, 1e-10, 1.0)))

    def train(self, x, y):
        if self.__train_step is None:
            raise Exception('Please add output layer before training.')
        self.__session.run(
            self.__train_step,
            feed_dict={self.input_x: x, self.input_y: y}
        )
