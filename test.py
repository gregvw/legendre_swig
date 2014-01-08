import numpy as np
from numpy.polynomial.legendre import legval

from pyLegendre import legendreEval

if __name__ == '__main__':

    m = 5
    n = 3
    a = np.random.randn(n)
    x = np.linspace(-1,1,m)

    f = legval(x,a)

    print("NumPy result = " + str(f))

    g = legendreEval(x,a)

    print("C SWIG result = " + str(g))
