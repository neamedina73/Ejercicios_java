# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:41:38 2021

@author: Alejandro AJ
"""

import numpy as np

a = np.array([[21,12,3],[14,25,6]])
print(a[(a%2==0)]) #"Devuelve una tupla de numeros divisibles entre dos"
print(a[(a%2==0)&(a>7)])
a = np.array([[21,12,3],[14,25,6]])
print(a[(a%3==0)]) #"Devuelve una tupla de numeros divisibles entre tres"
print(a[(a%3==0)&(a<7)])
