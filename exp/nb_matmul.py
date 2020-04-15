
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/matmul.ipynb

from torch import tensor
import numpy
import pickle
import gzip
from urllib.request import urlopen
import matplotlib.pyplot as plt
import fastai.vision

MNIST_URL='http://deeplearning.net/data/mnist/mnist.pkl.gz'

def test_eq(a, b): assert(a == b)

def is_close(a, b, tol = 0): assert(abs(a-b) < tol)

def get_data():
    f = gzip.open(urlopen(MNIST_URL), 'rb')
    (train_x, train_y),(valid_x, valid_y),_ = pickle.load(f, encoding='latin1')
    f.close()
    return train_x, train_y, valid_x, valid_y