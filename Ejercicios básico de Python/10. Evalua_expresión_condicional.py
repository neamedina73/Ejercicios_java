# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:19:32 2021

@author: Alejandro AJ
"""
#Evalúa la expresión lógica condición1 y ejecuta el primer bloque de código si es True; si no, 
#evalúa la siguientes condiciones hasta llegar a la primera que es True y ejecuta el bloque de código asociado. 
#Si ninguna condición es True ejecuta el bloque de código después de else:.
edad = int(input('Ingrese su edad: '))

if edad <= 18:
    print('Es menor')
elif edad >= 65:
    print('Juvilado')
else:
    print('Activo')