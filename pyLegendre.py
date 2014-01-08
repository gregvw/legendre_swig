"""
    Python outer wrapper for legendre_swig, so that we can return arrays
"""

import numpy as np
import legendre

def legendreEval(x,a):
    f = x
    legendre.legendreEval(x,f,a)
    return f
    
