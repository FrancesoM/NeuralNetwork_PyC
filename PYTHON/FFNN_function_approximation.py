#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:36:15 2018

@author: francescomaio
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def logsig(P):
    return (1/(1+np.exp(-P)))

def net(x,w1,w2,w3,s1,s2,s3,g1,g2,g3,s4):
    A = logsig(w1*x-s1)
    B = logsig(w2*x-s2)
    C = logsig(w3*x-s3)
    
    return g1*A + g2*B + g3*C - s4

fig, ax = plt.subplots(2)
x_vec = np.arange(-1,1,0.005)
y_vec = np.zeros(x_vec.shape)
t_vec = np.zeros(x_vec.shape)

for i,x in enumerate(x_vec):
    t_vec[i] = logsig(50*x)#40*(x-0.4))
    y_vec[i] = net(x,50,50,50,50*(0.2),50*(0.5),50*(0.7),-1,-1,-1,0)
    print(i,x,t_vec[i])
    
ax[0].plot(x_vec,t_vec)
ax[1].plot(x_vec,y_vec)
plt.show()

    




