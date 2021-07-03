# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:54:18 2021

@author: Alejandro AJ
"""

global lista_productos

lista_productos = list()
#Atributos del producto
class Producto:
    codProd = 0
    nomProd = ''
    
def menuPrograma():
    opcion = 0
    finmenu = 4
    while opcion != finmenu:
        #Mostrar el menú
        print('Menú')
        print('1.- Registrar producto')
        print('2.- Mostrar producto')
        print('3.- Buscar producto')
        print('4.- Salir')
        opcion = input('Digite la opción:')
        if opcion == 1:
            registrarProducto()
        elif opcion == 2:
            mostrarProducto()
        elif opcion == 3:
            buscarProducto()
        elif opcion == 4:
            salir()
    
def registrarProducto():
    print('Registro de productos')
    pro1 = Producto()
    #objetos de productos
    pro1.codProd = input('Ingrese el código del producto: ')
    pro1.nomProd = input('Ingrese el nombre del producto: ')
    
    lista_productos.append(pro1)

def mostrarProducto():
    print('Mostrar lista de los productos')
    for pro1 in lista_productos:
        print(pro1.codProd,'-', pro1.nomProd)
    
def buscarProducto():
    print('Buscar un producto')
    codProd = input('Ingrese el código a buscar: ')
    for pro1 in lista_productos:
        if pro1.codProd == codProd:
            print(pro1.codProd,'-', pro1.nomProd)
    
    
def salir():
    print('Gracias por usar esta aplicación')
        
menuPrograma()
