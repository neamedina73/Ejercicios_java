# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:16:21 2021

@author: Alejandro AJ
"""

class Mascota:
    def __init__(self):
        self.id=input('Ingrese ID de Mascota: ')
        self.datos=input('Ingrese Nombre y apellidos de la Mascota: ')
        self.peso=float(input('Ingrese el peso de la Mascota: '))
    
    def imprimir(self):
        print('id',self.id)
        print('Peso',self.peso)
        
    def pasa_peso(self):
        if self.peso>5 and self.peso <=25:
            print('Felicitaciones')
        elif self.peso<=4:
            print('No corresponde a razas pequeñas')
        elif self.peso>26:
            print('Valor no admitido')
Mascota1 = Mascota()
Mascota1.imprimir()
Mascota1.pasa_peso()