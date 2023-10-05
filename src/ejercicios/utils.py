import os
import time
import platform
from colorama import init, Fore

init(autoreset=True)


class __Console:
    def __init__(self) -> None:
        self.__CLEAR_INTRUCTION = 'cls' if platform.system() == 'Windows' else 'clear'

    def number(self, text: str = 'Ingrese un número: ') -> int:
        isCorrect = False
        while not isCorrect:
            try:
                n = int(input(text))
                isCorrect = True
                return n
            except ValueError:
                print(Fore.RED + 'El dato ingresado no es de tipo numerico')
                print(Fore.GREEN + 'Ingrese un número válido')
                time.sleep(2)
                self.clear()

    def someNumbers(self, amount: int = 1) -> list[int]:
        numbers = []
        for n in range(amount):
            print(Fore.YELLOW + n, '/', amount)
            numbers.append(self.number())
        return numbers

    def clear(self) -> None:
        os.system(self.__CLEAR_INTRUCTION)


console = __Console()
