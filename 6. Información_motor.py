# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:19:10 2021

@author: Alejandro AJ
"""

class motor:
    
    def __init__ (self, numero, cilindrage, combustible, velocidades, potencia):
        self.numero = numero
        self.cilindrage = cilindrage
        self.combustible = combustible
        self.velocidades = velocidades
        self.potencia = potencia

    def imprimir_numero_cilindrage(self):
        print(self.numero)
        print(self.cilindrage)
    
    def imprimir_combustible_velocidades(self):
        print(self.combustible)
        print(self.velocidades)
    
    def imprimir_potencia(self):
        print(self.potencia)
        
mymotor = motor('xj236587', 3000, 'acpm', 6, 3500)
mymotor.imprimir_combustible_velocidades()
mymotor.imprimir_numero_cilindrage()
mymotor.imprimir_potencia()