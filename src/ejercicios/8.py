from utils import console
import math

pares = []
impares = []

amount = console.number('Cuantos números desea ingresar?\n')

for x in range(amount):
    n = console.number()
    if n % 2 == 0:
        pares.append(n)
    else: 
        impares.append(n)

print('La suma de los pares es: ', sum(pares))
print('El producto de los impares es: ', math.prod(impares))
