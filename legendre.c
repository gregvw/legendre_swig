#include "legendre.h"

/* Evaluate the Legendre series with coefficients a[0],..,a[n-1] at the point x */ 
double legendreEval(double x, double *a,int n)
{
    // The value of the expansion at the given point
    double f = a[0];
    double p0 = 1;
    double p1 = x;  

    int k;
    
    f = a[0];

    if(n > 1)
    {
        f += x*a[1];
        if(n > 2)
        {
            double p2;
            for(k=1; k<n-1; ++k)
            {
                p2 = ((2*k+1)*x*p1-k*p0)/(k+1);
                f += a[k+1]*p2;
                p0 = p1;
                p1 = p2;
            }
        }
    }
    return f;
}

