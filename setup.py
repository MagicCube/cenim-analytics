from setuptools import setup

setup(
    name='cenim',
    version='0.1.0',
    packages=['cenim'],
    entry_points={
        'console_scripts': ['train = cenim.exes.train:main']
    })
