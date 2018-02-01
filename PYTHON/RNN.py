#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:02:21 2018

@author: francescomaio

RNN basic implementation

"""

import numpy as np

def sign(x,W):
    
    P = W.dot(x.T)
    #print('P',P)
    ret = np.zeros(x.shape)
    for i,val in enumerate(P):
        ret[i] = -1 if val<0 else 1
    
    return ret

x_dim = 15
pattern_num = 2

#learning patterns
X = np.array([[1,-1,-1,-1,1,1,1,-1,1,-1,1,1,-1,-1,1],
              [-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,-1,1]])

#estimate initial weights
W = np.zeros((x_dim,x_dim))
for i in range(0,pattern_num):
    W = W + np.tensordot(X[i],X[i].T,axes=0)

W = W*(1/x_dim)

print("Matrice dei pesi")
print(W)

i1 = X[0,:]
b1 = sign(i1,W)
it1 = 0
while( (i1==b1).all() != True  ):
    
    #update the input
    for i,val in enumerate(b1):
        i1[i] = b1[i]
    
    b1 = sign(i1,W)
    it1 = it1+1

print("Bacino di attrazione per s1 dopo %d iterazioni:"%it1)    
print(b1)


i2 = X[1,:]
b2 = sign(i2,W)
it2 = 0
while( (i2==b2).all() != True  ):
    
    #update the input
    for i,val in enumerate(b2):
        i2[i] = b2[i]
    
    b2 = sign(i2,W)
    it2 = it2+1

print("Bacino di attrazione per s2 dopo %d iterazioni:"%it2)
print(b2)

print("\n\n")

print("Net dynaimcs")

i_t0 = np.array([1,-1,-1,-1,1,1,1,-1,1,-1,1,1,1,-1,1])
print("Input:")
print(i_t0)

iteration = 1
o_t0 = sign(i_t0,W)
print("Iteration: ",iteration)
print(o_t0)


#print (o_t0)
#i_next = np.zeros(i_t0.shape)

#print(i_t0,o_t0,(i_t0==o_t0).all())

while( (i_t0==o_t0).all() != True  ):
    
    #update the input
    for i,val in enumerate(o_t0):
        i_t0[i] = o_t0[i]
    
    o_t0 = sign(i_t0,W)
    
    iteration = iteration+1
    print("Iteration: ",iteration)
    print(o_t0)
    
if( (o_t0==b1).all() == True ):
    print("Convergenza al bacino 1")
elif ( (o_t0==b2).all() == True ):
    print("Convergenza al bacino 2")
else:
    print("La rete non converge")
    
    

