# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:30:39 2021

@author: Alejandro AJ
"""

#Bucle o ciclos, algo que se va a repetir hasta que cumpla una condición

import math
numero = int(input('Ingrese un número: '))

while numero<0:
    print('Error, Debe ingresar un número positivo: ')
    numero = int(input('Ingrese un número: '))
    
    print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")