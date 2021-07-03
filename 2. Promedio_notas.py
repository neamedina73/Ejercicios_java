# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 07:33:57 2021

@author: Alejandro AJ
"""

#Programa que permite saber si un alumno Aprobó o Reprobó la asignatura.
class Estudiante:

    def __init__(self):
        self.nombre = input("Ingrese el nombre del estudiante:")
        self.apellido = input("Ingrese el apellido del estudiante:")
        self.nota1 = float(input("Ingrese la nota 1:"))  
        self.nota2 = float(input("Ingrese la nota 2:"))
        self.nota3 = float(input("Ingrese la nota 3:"))
        self.prome = 0

    def imprimir(self):      
        print("Nombre:",self.nombre)
        print("Apellido:",self.apellido)
        print("Nota 1",self.nota1)
        print("Nota 2",self.nota2)
        print("Nota 3",self.nota3)
        print("El promedio es:", round (self.prome,2))
        
    def promedio(self):
        self.prome = (self.nota1 + self.nota2 + self.nota3)/3

    def promover_estudiante(self):   
        if self.prome>=3.0:
            print("Aprobó la asignatura.")
        else:
            print("Reprobó la asignatura.")

estudiante1 = Estudiante()
estudiante1.promedio()
estudiante1.imprimir()
estudiante1.promover_estudiante()
