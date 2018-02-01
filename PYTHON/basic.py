#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 15:51:56 2018

@author: francescomaio
"""

import numpy as np

logistic = lambda x:1/(1+np.exp(-x))
hyperbolic = lambda x: (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

activation_functions = {
        'heavyside':lambda x:0 if x < 0 else 1,
        'sign':lambda x:-1 if x < 0 else 1,
        'logistic':logistic,
        'logistic_prime':lambda x: logistic(x)*(1-logistic(x)),
        'hyperbolic':hyperbolic,
        'hyperbolic_prime':lambda x:1-hyperbolic(x)**2
        }

def error(prediction,output):
    return 0.5*np.power(prediction-output,2)

class layer(object):
    
    def __init__(self,n_nodes,n_inputs,activation_f='logistic'):
        #the connection element w(i,j) connects the node i to the input j
        #the matrix has dimensions [n_nodes x n_inputs+1] because the input 
        #vector has always a -1 and the last column is the threshold for each
        #node, and it is a part of the weight matrix.
        #the weigths are random initialized. 
        self.n_nodes = n_nodes
        self.n_inputs= n_inputs
        self.connection_weigths = np.random.rand(n_nodes,n_inputs+1)
        self.activation_f = activation_f
        
    def layer_output(self,input_vector,prediction=None):
        
        #If we give a prediction we can also calculate the error
        P = np.dot(self.connection_weights,input_vector.T)
        O = np.zeros(self.n_nodes)
        
        for i in range(self.n_nodes):
            O[i] = activation_functions[self.activation_f](P[i])
            
        if prediction != None:
            E = error(prediction,O)
            return O,E
        else:
            return O
        
    
    
    
    

"""
class perceptron(object):
    
    def __init__(self,activation_f='logistic'):
        self.activation = activation_functions[activation_f]
        
    def out(self,P):
        #w is the vector of weights
        #x is the vector of inputs
        return self.activation(P)
"""
            