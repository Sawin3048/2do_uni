from utils import console

numbers = []
for n in range(100):
    numbers.append(console.number())

print('La suma es: ', sum(numbers))
