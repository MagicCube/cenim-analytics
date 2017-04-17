# -*- coding: utf-8 -*-
# Module: cenim.models.Model

import tensorflow as tf


class Model(object):
    def __init__(self, session):
        self.session = session

    def train(self, x, y):
        raise NotImplementedError

    def get_prediction(self):
        raise NotImplementedError

    def get_train_step(self):
        raise NotImplementedError


class Classifier(Model):
    def __init__(self, session, n_input, n_classes):
        super(Classifier, self).__init__(session)
        self.n_input = n_input
        self.n_classes = n_classes
        self.keep_prob = tf.placeholder(tf.float32)
        self.input_x = tf.placeholder(tf.float32, [None, n_input])
        self.input_y = tf.placeholder(tf.float32, [None, n_classes])

    def train(self, x, y):
        train_step = self.get_train_step()
        self.session.run(
            train_step,
            feed_dict={self.input_x: x, self.input_y: y, self.keep_prob: 0.5}
        )

    def compute_accuracy(self, x, y):
        prediction = self.get_prediction()
        y_pred = self.session.run(prediction, feed_dict={self.input_x: x, self.keep_prob: 1})

        dislikes = 0
        for pred in y_pred:
            if pred[0] == 0 and pred[1] == 1:
                dislikes += 1
        print(y_pred)
        print('Dislikes: ' + str(dislikes))

        correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        result = self.session.run(accuracy, feed_dict={self.input_x: x, self.input_y: y, self.keep_prob: 1})
        return result
