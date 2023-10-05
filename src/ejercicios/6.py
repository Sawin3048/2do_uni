from utils import console
cantidad = console.number('Ingrese la cantidad de números a sumar: ')
numbers = []
for n in range(cantidad):
    numbers.append(console.number())

print('La suma es: ', sum(numbers))
