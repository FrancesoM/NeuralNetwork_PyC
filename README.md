# NeuralNetwork_PyC
Functions to create and train neural networks. 

The aim of this repository is to develop functions to create and train neural networks. To enhance the didactic power I will progressively rewrite all the python functions in C, exposing the APIs to python. This may increase the performances and will for sure give me a better understanding of both languages. 

# Build the library (should work on both linux and MAC)
You can get along with the python functions. As this project goes on, I want to rewrite them in C. The python module will always be present and will be always available. If you want to try the C functions, you must run follow these steps (next an autoconf/make script will be added):

  <p><b>open pyCext.c and modify the path to your Python.h header</b></p>
  <p>gcc -c NN_func.c -o NN_func.o </p>
  <p>ar rcs libstaticneural.a NN_func.o </p>
  <p>gcc test.c -L. -lstaticneural -otest.o <em style="color:red"> <--- check no errors </em></p>
  <p>./test.o <font color="red"></em> <--- check no errors </em></font></p>
  <p>python3 setup.py build_ext --inplace </p>
  <p><b>copy the .so file in one of the python paths </b></p>
  <p>python3 test.py <font color="red"><em> <--- check no errors </em></font></p>

# Guides
<p><a href=http://chimera.labs.oreilly.com/books/1230000000393/ch15.html#_discussion_241>Explain the meaning of the py_to_C file </a></p>
<p><a href=http://www.adp-gmbh.ch/cpp/gcc/create_lib.html>Create dynamic and static library, link them.</a></p>
<p><a href=https://docs.python.org/3/c-api/arg.html#arg-parsing>Parsing normal arguments from python to C</a></p>
<p><a href=https://docs.scipy.org/doc/numpy-1.13.0/user/c-info.how-to-extend.html>Parse numpy arrays and handle them from python to C</a></p>	  
