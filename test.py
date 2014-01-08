import numpy as np
from numpy.polynomial.legendre import legval

from legendre import legendreEval

if __name__ == '__main__':

    n = 3
    a = np.random.randn(n)
    x = 0.5

    f = legval(x,a)

    print("NumPy result = " + str(f))


    g = legendreEval(x,a)

    print("C SWIG result = " + str(g))
