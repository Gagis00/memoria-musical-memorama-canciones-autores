from colorama import Fore, Style
import colorama

from presentacion import datos_generales, descripcion_juego
from validar_opcion import validar_opcion_int
from solicitar_posicion import solicitar_posicion
from juego import jugar

def main():
    colorama.init(autoreset=True)
    opcion = 0
    while opcion != 4:
        print(Style.BRIGHT + Fore.BLUE + "\nJuego de Memorama Musical")
        print("1) Datos Generales")
        print("2) Descripción del juego")
        print("3) Jugar")
        print("4) Terminar")
        opcion = validar_opcion_int(input("Opción deseada: "))
        if opcion == 1:
            datos_generales()
        elif opcion == 2:
            descripcion_juego()
        elif opcion == 3:
            jugar()
        elif opcion == 4:
            print(Fore.GREEN + "\n¡Gracias por jugar! Hasta la próxima.\n")


main()