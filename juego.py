'''
Aqui esta la logica completa del juego
'''

from colorama import Fore, Style #Importar estilos de colorama
from baraja import crear_baraja #Importar función para crear la baraja
from tablero import crear_tablero, crear_tablero_visible, mostrar_tablero #Importar funciones del tablero
from solicitar_posicion import solicitar_posicion #Importar función para solicitar posición

def puntaje_por_epoca(epoca): # Asigna puntaje según la época de la canción
    if epoca == "2010s":
        return 3
    elif epoca == "1990s-2010":
        return 2
    elif epoca == "1970s-1990":
        return 1
    else:
        return 1

def todas_descubiertas(tablero_visible): # Verifica si todas las celdas ya estan descubiertas con la "✔"
    return all(cell == "✔" for row in tablero_visible for cell in row) # Retorna True si todas las celdas son "✔"

def formatea_carta_titulo(carta): #Enseña el título de la carta
    return f"{carta['titulo']}" 

def formatea_carta_datos(carta): #Enseña los datos de la carta
    return f"{carta['autor']}, {carta['anio']}"

def mostrar_carta(tablero_visible, tablero_real, fila, columna):
    if tablero_real[fila][columna]["tipo"] == "titulo":
        tablero_visible[fila][columna] = formatea_carta_titulo(tablero_real[fila][columna])
    else:
        tablero_visible[fila][columna] = formatea_carta_datos(tablero_real[fila][columna])

def jugar(): #Función principal del juego
    print(Fore.CYAN + "\n¡Bienvenido al Memorama Musical!") 
    ##### -------- Configuración del juego -------- #####
    renglones = 4 
    columnas = 4

    baraja = crear_baraja(1, 3, 4) # Crea una baraja con 1 canción de 2010s, 3 de 1990s-2010 y 4 de 1970s-1990
    tablero_real = crear_tablero(renglones, columnas, baraja) # Crea el tablero con las cartas
    tablero_visible = crear_tablero_visible(renglones, columnas) #Crea el tablero inicial con "??"

    puntos = 0 # Inicializa puntos en 0
    intentos = 0 # Inicializa intentos en 0
    pares_encontrados = [] # Lista para almacenar pares encontrados
    datos_curiosos = [] # Lista para almacenar datos curiosos

    print(Fore.CYAN + "El juego comienza con un tablero cubierto. ¡Listo para comenzar?\n")
    mostrar_tablero(tablero_visible) # Muestra el tablero inicial

    juego_activo = True # Indica si el juego está activo
    while juego_activo and not todas_descubiertas(tablero_visible): # Mientras el juego esté activo y no se hayan descubierto todas las cartas
        print(Fore.YELLOW + f"\nIntentos: {intentos}") # Muestra los intentos
        print(f"Puntaje: {puntos}") # Muestra el puntaje
        if pares_encontrados: # Si hay pares encontrados, los muestra
            print(Fore.GREEN + "Pares encontrados:") 
            for par in pares_encontrados: # Enseña los pares encontrados
                print(" - " + par)
            print(Fore.MAGENTA + "Datos curiosos:")
            for dato in datos_curiosos: # Enseña los datos curiosos
                print(" - " + dato)
        print(Style.RESET_ALL)

        seleccion_valida_1 = False # Solicita la primera carta
        while not seleccion_valida_1 and juego_activo: # Mientras no sea válida y el juego esté activo
            f1, c1 = solicitar_posicion(tablero_visible) # Solicita posición
            if f1 == "salir": # Opción de salir si el jugador quiere
                print("¡Juego terminado por el usuario!") 
                juego_activo = False #Juego acabado
            elif tablero_visible[f1][c1] == "??": # Verifica si la carta está cubierta
                seleccion_valida_1 = True # Marca la selección como válida
            else:
                print(Fore.RED + "¡Esa carta ya está descubierta! Elige otra.") # Mensaje de error si la carta ya está descubierta

        if not juego_activo: # Si el juego ha terminado
            return # Sale de la función

        # Mostrar la carta 1 según su tipo
        mostrar_carta(tablero_visible, tablero_real, f1, c1)
        mostrar_tablero(tablero_visible)

        seleccion_valida_2 = False # Solicita la segunda carta
        while not seleccion_valida_2 and juego_activo: # Mientras no sea válida y el juego esté activo
            f2, c2 = solicitar_posicion(tablero_visible) # Solicita posición
            if f2 == "salir": # Opción de salir si el jugador quiere
                print("¡Juego terminado por el usuario!")
                juego_activo = False #Juego acabado
            elif tablero_visible[f2][c2] == "??" and (f2, c2) != (f1, c1): # Verifica si la carta está cubierta y no es la misma que la primera
                seleccion_valida_2 = True # Marca la selección como válida
            else:
                print(Fore.RED + "¡Esa carta ya está descubierta o es la misma! Elige otra.")

        if not juego_activo: # Si el juego ha terminado
            return

        # Mostrar la carta 2 según su tipo
        mostrar_carta(tablero_visible, tablero_real, f2, c2)
        mostrar_tablero(tablero_visible)

        intentos += 1 # Suma los intentos

        carta1 = tablero_real[f1][c1] # Obtiene primera carta seleccionada
        carta2 = tablero_real[f2][c2] # Obtiene segunda carta seleccionada

        es_par = ( carta1['titulo'] == carta2['titulo'] and carta1['autor'] == carta2['autor'] and carta1['anio'] == carta2['anio']) # Verifica si son par

        if es_par: # Si son par
            print(Fore.GREEN + "\n¡Correcto! Has encontrado el par:") 
            par_str = f"{carta1['titulo']} <> {carta1['autor']}, {carta1['anio']}" #Da formato al par encontrado
            print(par_str) #Muestra el par encontrado
            print(Fore.MAGENTA + f"Dato curioso: {carta1['curioso']}\n") #Muestra el dato curioso
            puntos += puntaje_por_epoca(carta1['epoca']) # Suma puntos según la época
            pares_encontrados.append(par_str) # Agrega el par a la lista de encontrados
            datos_curiosos.append(f"{carta1['titulo']}: {carta1['curioso']}") # Agrega el dato curioso a la lista
            tablero_visible[f1][c1] = "✔" # Marca la carta como descubierta
            tablero_visible[f2][c2] = "✔" # Marca la carta como descubierta
        else:
            print(Fore.RED + "\n¡No son par!\n") # Mensaje de error
            tablero_visible[f1][c1] = "??" # Vuelve a cubrir la carta
            tablero_visible[f2][c2] = "??" # Vuelve a cubrir la carta

    print(Fore.CYAN + "\n¡Felicidades! ¡Has encontrado todos los pares o has salido del juego!")
    mostrar_tablero(tablero_visible) # Muestra el tablero final
    print(Fore.YELLOW + f"Intentos totales: {intentos}") # Muestra los intentos totales
    print(f"Puntaje total: {puntos}") # Muestra el puntaje total
    print(Fore.GREEN + "Pares encontrados:") # Muestra los pares encontrados
    for par in pares_encontrados: # Recorre los pares encontrados
        print(" - " + par) # Muestra cada par encontrado
    print(Fore.MAGENTA + "Datos curiosos:") # Muestra los datos curiosos
    for dato in datos_curiosos: # Recorre los datos curiosos
        print(" - " + dato) # Muestra cada dato curioso
    print(Style.RESET_ALL)