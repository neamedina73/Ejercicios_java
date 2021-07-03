# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:00:30 2021

@author: Alejandro AJ
"""

import numpy as np

a2 = np.array([[1,2,3],[4.3,2.1,5.6]])
a3 = np.array([[1,2,3],[4.3,2.1,5.6],[0.5,7,10]])
print(a2)
print(a3)
print('Numero de elementos en a2:', a2.size)#devuelve el número de elementos del array
print('Numero de elementos en a3:', a3.size)#devuelve el número de elementos del array
print('Devuelve una tupla condimensiones del array:', a2.shape, a3.shape)
print('Devuelve el tipo de datos del array:',a2.dtype, a3.dtype)
print('Devuelve el número de dimensiones:', a2.ndim, a3.ndim)

