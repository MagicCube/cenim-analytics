# -*- coding: utf-8 -*-
# Package: cenim.utils


import codecs
import json


def load_json(path):
    f = open(path, 'r')
    data = json.load(f, encoding='utf-8')
    f.close()
    return data


def load_data(name):
    path = ''.join(['data/', name, '.json'])
    return load_json(path)
