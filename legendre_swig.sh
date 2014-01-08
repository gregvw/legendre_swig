# Make this executable with  
# chmod u+x legendre_swig.sh
#
# Execute with 
# ./legendre_swig.sh


#rm legendre.py legendre.pyc legendre_wrap.* legendre.o _legendre.so
swig -python legendre.i
python setup.py build_ext --inplace
python test.py
