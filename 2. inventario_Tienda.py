# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:28:00 2021

@author: Alejandro AJ
"""
#programa realizado por Nelson Acuña del Grupo 72 Mision Tic 2022
#Programa inventario de una tienda de barrio "El Oasis"

global listaPorductos
listaPorductos = []

class Inventario:
    
    #modulo constructor
    def __init__(self):
        self.nombreTienda = 'TIENDA EL OASIS'
        self.direccion = 'Carrera 3A N° 6-119'
        self.nomProducto = input('Digite el nombre del producto: ')
        self.tipoProducto = input('Digite el grupo del producto: ')
        self.precioProducto = float(input('Digite el precio: '))
        self.stock = 100
        self.cantProducto = int(input('Cuántos productos desea?: '))
        self.venta = 0
        self.descuento =0
    
    #Información básica de los productos tienda
    def infoTienda(self):
        print('\n')
        print('//////////////////////////')
        print(self.nombreTienda)
        print(self.direccion)
        print('Cant. productos existentes: ',self.stock)
        print(self.nomProducto)
        print(self.tipoProducto)
        print('Valor Unitario: ', self.precioProducto)
        print('Cant. productos vendidos: ',self.cantProducto)
        
        
     #venta del producto, stock y agotados   
    def ventas (self):
        self.stock = self.stock - self.cantProducto
        if self.stock <= 5:
            print('¡Alerta...!Este producto se agotó: ', self.stock)
        else:
            print('Cant. productos en stock: ',self.stock)
            
    #Descuentos de los productos
    def descuentos(self):
        self.venta = self.precioProducto * self.cantProducto
        print('El valor de su compra es de: ',self.venta)      
        if self.venta > 250000:
            self.descuento = self.venta * 0.10
            self.pagoTotal = self.venta - self.descuento
            print('Tiene un descuento de:',round(self.descuento,2))
            print('El pago con descuento es de: ', self.pagoTotal)
        else:
            print('No tiene ningún descuento')
            
    #Imprime la factura        
    def imprimirfactura (self):
        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
        print('Compras mayores a $ 250.000, tienen un descuento del 10%')
        print('Gracias por su compra!')
tienda1 = Inventario()
tienda1.infoTienda()
tienda1.ventas()
tienda1.descuentos()
tienda1.imprimirfactura()