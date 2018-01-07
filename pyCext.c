//
//  pyCext.c
//  Neural_Functions
//
//  Created by Francesco Maio on 06/01/18.
//  Copyright © 2018 Francesco Maio. All rights reserved.
//
///Users/francescomaio/anaconda3/include/python3.6m

#include </Users/francescomaio/anaconda3/include/python3.6m/Python.h>
#include "NN_func.h"

/*float heavyside(float P);*/
static PyObject *py_heavyside(PyObject *self, PyObject *args) {
    float P, result;
    
    //Parse the elements as a float
    if (!PyArg_ParseTuple(args,"f", &P)) {
        return NULL;
    }
    result = heavyside(P);
    return Py_BuildValue("f", result);
}

/*float logistic(float P);*/
static PyObject *py_logistic(PyObject *self, PyObject *args) {
    float P, result;
    
    //Parse the elements as a float
    if (!PyArg_ParseTuple(args,"f", &P)) {
        return NULL;
    }
    result = logistic(P);
    return Py_BuildValue("f", result);
}

/* Module method table */
static PyMethodDef NN_Methods[] = {
    {"heavyside",  py_heavyside, METH_VARARGS, "Heavyside activation function"},
    {"logistic", py_logistic, METH_VARARGS, "Logistic activation function"},
    {NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef neuralmodule = {
    PyModuleDef_HEAD_INIT,
    "neural",           /* name of module */
    "A simple neural module",  /* Doc string (may be NULL) */
    -1,                 /* Size of per-interpreter state or -1 */
    NN_Methods       /* Method table */
};

/* Module initialization function */
PyMODINIT_FUNC
PyInit_neural(void) {
    return PyModule_Create(&neuralmodule);
}












