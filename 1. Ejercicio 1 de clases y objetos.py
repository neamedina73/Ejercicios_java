class Humano:
    def __init__ (self, edad): #Primer método de la clase humano.
        self.edad = edad
    
    def hablar(self, mensaje):
        print(mensaje)

nelson = Humano(48)
pedro = Humano(29)

print('Soy Nelson y tengo', nelson.edad,'años.')
print('Soy Pedro y tengo', pedro.edad,'años.')
nelson.hablar('- Hola Pedro')
pedro.hablar('- Hi Nelson')

