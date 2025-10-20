from colorama import Fore, Style
import colorama

from presentacion import datos_generales, descripcion_juego #Importar funciones de presentación
from instrucciones import mostrar_instrucciones #Importar función de instrucciones
from validar_opcion import validar_opcion_int #Importar función de validación de opción
from juego import jugar #Importar función del juego

def main():
    colorama.init(autoreset=True) #Inicializa colorama
    opcion = 0 
    while opcion != 5: 
        ## Menú principal ##
        print(Style.BRIGHT + Fore.BLUE + "\nJuego de Memorama Musical")
        print("1) Datos Generales")
        print("2) Descripción del juego")
        print("3) Instrucciones y reglas")
        print("4) Jugar")
        print("5) Terminar") 
        opcion = validar_opcion_int(input("Opción deseada: "))
        if opcion == 1:
            datos_generales() #Llamar a la función de datos generales
        elif opcion == 2:
            descripcion_juego() #Llamar a la función de descripción del juego
        elif opcion == 3:
            mostrar_instrucciones() #Llamar a la función de instrucciones
        elif opcion == 4:
            jugar() #Llamar a la función del juego
        elif opcion == 5:
            print(Fore.GREEN + "\n¡Gracias por jugar! Hasta la próxima.\n") #Mensaje de despedida

main()