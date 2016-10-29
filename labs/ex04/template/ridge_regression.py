# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np

def ridge_regression(y, tx, lamb):
    """implement ridge regression."""
    return np.linalg.solve((tx.T @ tx)+lamb*np.identity(tx.shape[1]), tx.T @ y)