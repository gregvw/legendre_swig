#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import *
from distutils import sysconfig

import numpy


try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()    




legendre_module = Extension('_legendre',
                           sources=['legendre.i', 'legendre.c'],
                           include_dirs = [numpy_include],
                           )

setup (name = 'legendre',
       version = '0.1',
       author      = "Greg von Winckel",
       description = """Evaluate a Legendre series with C""",
       ext_modules = [legendre_module],
       py_modules = ["legendre"],
       )
