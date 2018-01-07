#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:24:27 2018

@author: francescomaio
"""
# setup.py

from distutils.core import setup, Extension

setup(name='neural',
      ext_modules=[
        Extension('neural',
                  ['pyCext.c'],
                  include_dirs = [],
                  define_macros = [('FOO','1')],
                  undef_macros = ['BAR'],
                  library_dirs = ['/Users/francescomaio/Desktop/PoliMI/Neuroengineering/NeuralNetwork_PyC/'],
                  libraries = ['staticneural']
                  )
        ]
)
      
