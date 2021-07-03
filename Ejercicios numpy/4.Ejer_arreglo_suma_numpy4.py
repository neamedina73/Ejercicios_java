# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:00:30 2021

@author: Alejandro AJ
"""

import numpy as np

a = np.array([[10, 20, 30], [40, 50, 60], [70, 80 , 90]])
b = np.array([1, 2, 3])
c = np.empty_like(a)

print(a.shape)


import numpy as np
iguales = np.array([[1,1,1],[2,2,2],[3,3,3]])
ale = np.array([[10,20,30],[1,1,1],[1,2,3]])
c = np.array([[4,4,4],[5,5,5],[3,6,3]])
print(iguales.dot(ale))

import numpy as np
a = np.array([[4,3,2],[5,6,7]])
b = np.array([[2,2,2],[3,3,6]])
c = np.array([[5,3,8],[6,7,9]])

print((a*b)-c)

import numpy as np
a = np.array([[10,20,30],[40,50,60],[70,80,90]])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a.dot(b))





