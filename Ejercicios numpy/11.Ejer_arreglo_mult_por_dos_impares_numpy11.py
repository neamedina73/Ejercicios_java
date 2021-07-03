# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:20:22 2021

@author: Alejandro AJ
"""

import numpy as np

A = np.array([[2,3],[4,5]])
for j in range(0,2):
    A[1][j]=A[1][j]*2
    print(A)