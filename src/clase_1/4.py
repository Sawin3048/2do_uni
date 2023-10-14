from utils import console
n = console.number
a, b, c = n(), n(), n()
print('El número mayor es: ', max(a, b, c),
      '\nEl número menor es: ', min(a, b, c))
