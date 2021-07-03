# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:14:10 2021

@author: Alejandro AJ
"""
#Operaciones matemáticas a nivel de array

import numpy as np

#a.dot(b) : Devuelve el array resultado del producto matricial 
#de los arrays a y b siempre y cuando sus dimensiones sean 
#compatibles.

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,1],[2,2],[3,3]])
print(a.dot(b))

#[[14 14]
#[32 32]]

#Y para trasponer una matriz se utiliza el método
print(a.T)
#[[1 4]
#[2 5]
#[3 6]]
