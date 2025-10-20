from colorama import Fore
from tablero import crear_tablero, mostrar_tablero
from solicitar_posicion import solicitar_posicion

def jugar():
    """
    Permite jugar una ronda sencilla: inicializa el tablero, muestra el tablero,
    solicita una jugada, actualiza el tablero y muestra el tablero actualizado.
    """
    print("\n¡Comienza el juego!")
    renglones = 6
    columnas = 6  
    tablero = crear_tablero(renglones, columnas)
    puntos = 0
    mostrar_tablero(tablero)
    
    respuesta = "s"
    while respuesta == "s":
        print(Fore.YELLOW + f"\nPuntos acumulados: {puntos}")
        print("Realiza una jugada (elige una celda para revelar temporalmente):")
        fila, columna = solicitar_posicion(tablero)
        tablero[fila][columna] = "X"
        mostrar_tablero(tablero)
        puntos += 1
        respuesta = input("¿Deseas hacer otra jugada? (s/n): ").strip().lower()
        while respuesta not in ["s", "n"]:
            respuesta = input("Por favor ingresa 's' para sí o 'n' para no: ").strip().lower()