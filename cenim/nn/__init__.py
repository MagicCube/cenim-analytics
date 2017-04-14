# -*- coding: utf-8 -*-
# Package: cenim.nn

from cenim.movies import *
from prepare import *


def run():
    prepare()
    print(get_movies_matrix(['1299398']).shape)
