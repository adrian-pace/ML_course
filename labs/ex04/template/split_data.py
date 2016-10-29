# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np
import math

def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    split_size=math.floor(x.shape[0]*ratio)
    split_x=[]
    split_y=[]
    shuffle_indices = np.random.permutation(np.arange(y.shape[0]))
    shuffled_y = y[shuffle_indices]
    shuffled_tx = x[shuffle_indices]
    return shuffled_tx[0:split_size],shuffled_y[0:split_size],shuffled_tx[split_size:],shuffled_y[split_size:]