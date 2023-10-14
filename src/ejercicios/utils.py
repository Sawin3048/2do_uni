import os
import time
import platform
from colorama import init, Fore

init(autoreset=True)


class __Console__:
    def __init__(self) -> None:
        self.__CLEAR_INTRUCTION__ = 'cls' if platform.system() == 'Windows' else 'clear'

    def number(self, text: str = 'Ingrese un número: ') -> int:
        while True:
            try:
                return int(input(text))
            except ValueError:
                print(Fore.RED + 'El dato ingresado no es de tipo numerico')
                print(Fore.GREEN + 'Ingrese un número válido')
                time.sleep(2)
                self.clear()

    def someNumbers(self, amount: int = 1) -> list[int]:
        numbers = []
        for n in range(amount):
            print(Fore.YELLOW + str(n + 1) + '/' + str(amount))
            numbers.append(self.number())
        return numbers

    def clear(self) -> None:
        os.system(self.__CLEAR_INTRUCTION__)


console = __Console__()
