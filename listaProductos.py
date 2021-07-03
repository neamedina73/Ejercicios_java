# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:13:08 2021

@author: Alejandro AJ
"""

#global listaPorductos
#listaPorductos = list()]

class Producto:
    
    def __init__(self):
        self.codigoProd = int(input('Ingrese el código: '))
        self.nomProd = "Galletas"
        self.fechVenc = '12/05/2023'
        self.grpProd = "Alimentos"

    def Imprimir(self):
        print('Código',self.codigoProd)
        print(self.nomProd)
        print(self.fechVenc)
        print(self.grpProd)
    
    

producto1 = Producto()
producto1.Imprimir()
    
