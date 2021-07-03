# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:20:22 2021

@author: Alejandro AJ
"""

import numpy as np

lista_de_numeros = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
for i in range(0,12,2):
    print('Valor anterior: ', lista_de_numeros[i+1])
    lista_actual=lista_de_numeros[i+1]*2
    print('Valor actual: ', lista_actual)
    