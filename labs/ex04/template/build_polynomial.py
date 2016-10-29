# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np
import math

def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    poly=np.ones([x.shape[0],degree+1])
    for i in range(0,x.shape[0]):
        for j in range(1, degree+1):
            poly[i][j]=math.pow(x[i],j)
    return poly