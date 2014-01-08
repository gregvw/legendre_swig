/* File: legendre.i */
%module legendre

%{
    #define SWIG_FILE_WITH_INIT
    #include "legendre.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}


/* This lets us determine the length of the array */
%apply (double *IN_ARRAY1, int DIM1) {(double *x, int m1)};
%apply (double *INPLACE_ARRAY1, int DIM1) {(double *f, int m2)};
%apply (double *IN_ARRAY1, int DIM1) {(double *a, int n)};

%include "legendre.h"
