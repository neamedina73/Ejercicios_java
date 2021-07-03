#Escribir un programa que pregunte al usuario cinco números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
numeros = []
for i in range(5):
    numeros.append(int(input('Ingrese el número ganador: ')))
    numeros.sort()
    print('Los números ganadores son: '+ str(numeros))