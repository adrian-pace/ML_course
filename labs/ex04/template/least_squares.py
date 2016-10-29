# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares solution."""
    w=np.linalg.inv(tx.T @ tx) @ tx.T @ y
    e= y - (tx @ w)
    mse=1/(2*y.shape[0])*(e.T @ e)
    return w,mse