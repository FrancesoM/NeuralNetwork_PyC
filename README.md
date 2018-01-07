# NeuralNetwork_PyC
Functions to create and train neural networks. 

The aim of this repository is to develop functions to create and train neural networks. To enhance the didactic power I will progressively rewrite all the python functions in C, exposing the APIs to python. This may increase the performances and will for sure give me a better understanding of both languages. 

# Build the library (should work on both linux and MAC)
You can get along with the python functions. As this project goes on, I want to rewrite them in C. The python module will always be present and will be always available. If you want to try the C functions, you must run follow these steps (next an autoconf/make script will be added):

  <p><b>open pyCext.c and modify the path to your Python.h header</b></p>
  <p>gcc -c NN_func.c -o NN_func.o </p>
  <p>ar rcs libstaticneural.a NN_func.o </p>
  <p>gcc test.c -L. -lstaticneural -otest.o <em> <--- check no errors </em></p>
  <p>./test.o </em> <--- check no errors </em></p>
  <p>python3 setup.py build_ext --inplace </p>
  <p><b>copy the .so file in one of the python paths </b></p>
  <p>python3 test.py <em> <--- check no errors </em></p>
