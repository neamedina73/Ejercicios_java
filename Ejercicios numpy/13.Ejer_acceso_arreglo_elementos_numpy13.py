# -*- coding: utf-8 -*-
"""
Created on Sat May 29 15:32:15 2021

@author: Alejandro AJ
"""
#Acceso a elementos de un arreglo
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a[1,0])#accede al elemento de la fila 1 columna 0
print(a[1][0])#De otra forma accede al mismo elemento
print(a[:,0:2])