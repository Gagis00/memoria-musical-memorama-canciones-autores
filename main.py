from colorama import Fore, Style
import colorama

from presentacion import datos_generales, descripcion_juego
from instrucciones import mostrar_instrucciones
from validar_opcion import validar_opcion_int
from juego import jugar

def main():
    colorama.init(autoreset=True)
    opcion = 0
    while opcion != 5:
        print(Style.BRIGHT + Fore.BLUE + "\nJuego de Memorama Musical")
        print("1) Datos Generales")
        print("2) Descripción del juego")
        print("3) Instrucciones y reglas")
        print("4) Jugar")
        print("5) Terminar")
        opcion = validar_opcion_int(input("Opción deseada: "))
        if opcion == 1:
            datos_generales()
        elif opcion == 2:
            descripcion_juego()
        elif opcion == 3:
            mostrar_instrucciones()
        elif opcion == 4:
            jugar()
        elif opcion == 5:
            print(Fore.GREEN + "\n¡Gracias por jugar! Hasta la próxima.\n")

main()