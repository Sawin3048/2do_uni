import os
from time import sleep
os.system('cls')
from colorama import Fore

gato = 'perro'

def __getNumber():
  isOkey = False
  number = None

  while not isOkey:  
    try:
      number = int(input(Fore.RESET + 'Ingrese un número: '))
      isOkey = True
    except: 
      print(Fore.RED + 'Ha ingresado un caracter invalido')
      sleep(1)
      os.system('cls')
  return number


__number = __getNumber()
print(Fore.GREEN + 'El numero devuelto es: ' + str(__number) )
