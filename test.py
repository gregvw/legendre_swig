import numpy as np
import time

from numpy.polynomial.legendre import legval
from pyLegendre import legendreEval

if __name__ == '__main__':

    m = 200
    n = 200

    a = np.random.randn(n)
    x = np.linspace(-1,1,m)

    start = time.time()
    f = legval(x,a)
    stop = time.time()

    print("NumPy time = " + str(stop-start))

    start = time.time()
    g = legendreEval(x,a)
    stop = time.time()
    print("C SWIG time = " + str(stop-start))
