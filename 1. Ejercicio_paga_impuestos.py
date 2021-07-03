# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:43:26 2021

@author: Alejandro AJ
"""
class  Empleado:
    def __init__(self):
        self.nombre=input('Ingrese el nombre del empleado:')
        self.sueldo=float(input('Ingrese el sueldo:'))
    
    def imprimir(self):
        print('Nombre',self.nombre)
        print('Sueldo',self.sueldo)
    
    def paga_impuestos(self):
        if self.sueldo>3000:
            print('Debe pagar impuesto')
        else:
            print('No debe pagar impuestos')
        
empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()