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
%apply (double *INPLACE_ARRAY1, int DIM1) {(double *a, int n)}

%include "legendre.h"
