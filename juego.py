from colorama import Fore, Style
from baraja import crear_baraja
from tablero import crear_tablero, crear_tablero_visible, mostrar_tablero
from solicitar_posicion import solicitar_posicion
import time

def puntaje_por_epoca(epoca):
    if epoca == "2010s":
        return 3
    elif epoca == "1990s-2010":
        return 2
    elif epoca == "1970s-1990":
        return 1
    else:
        return 1

def todas_descubiertas(tablero_visible):
    return all(cell == "✔" for row in tablero_visible for cell in row)

def formatea_carta_titulo(carta):
    return f"{carta['titulo']}"

def formatea_carta_datos(carta):
    return f"{carta['autor']}, {carta['anio']}"

def jugar():
    print(Fore.CYAN + "\n¡Bienvenido al Memorama Musical!")
    renglones = 6
    columnas = 6

    # Crear la baraja y tableros
    baraja = crear_baraja(3, 6, 9)
    tablero_real = crear_tablero(renglones, columnas, baraja)
    tablero_visible = crear_tablero_visible(renglones, columnas)  # Sólo "??" o "✔"

    puntos = 0
    intentos = 0
    pares_encontrados = []
    datos_curiosos = []

    print(Fore.CYAN + "El juego comienza con un tablero cubierto. ¡Listo para comenzar?\n")
    mostrar_tablero(tablero_visible)

    while not todas_descubiertas(tablero_visible):
        print(Fore.YELLOW + f"\nIntentos: {intentos}")
        print(f"Puntaje: {puntos}")
        if pares_encontrados:
            print(Fore.GREEN + "Pares encontrados:")
            for par in pares_encontrados:
                print(" - " + par)
            print(Fore.MAGENTA + "Datos curiosos:")
            for dato in datos_curiosos:
                print(" - " + dato)
        print(Style.RESET_ALL)  # Reset color

        # Seleccionar primera carta
        while True:
            print(Fore.CYAN + "Selecciona la primera carta para voltear:")
            f1, c1 = solicitar_posicion(tablero_visible)
            if tablero_visible[f1][c1] == "??":
                break
            else:
                print(Fore.RED + "¡Esa carta ya está descubierta! Elige otra.")

        # Mostrar la carta (titulo o datos, aleatorio por diseño o puedes elegir que siempre sea título primero)
        es_titulo = True  # Cambia a False si quieres mostrar datos primero y después el título
        if es_titulo:
            tablero_visible[f1][c1] = formatea_carta_titulo(tablero_real[f1][c1])
        else:
            tablero_visible[f1][c1] = formatea_carta_datos(tablero_real[f1][c1])
        mostrar_tablero(tablero_visible)

        # Seleccionar segunda carta
        while True:
            print(Fore.CYAN + "Selecciona la segunda carta para voltear:")
            f2, c2 = solicitar_posicion(tablero_visible)
            if tablero_visible[f2][c2] == "??" and (f2, c2) != (f1, c1):
                break
            else:
                print(Fore.RED + "¡Esa carta ya está descubierta o es la misma! Elige otra.")

        # La segunda carta debe mostrar el complemento (si primera fue título, esta es datos y viceversa)
        if es_titulo:
            tablero_visible[f2][c2] = formatea_carta_datos(tablero_real[f2][c2])
        else:
            tablero_visible[f2][c2] = formatea_carta_titulo(tablero_real[f2][c2])
        mostrar_tablero(tablero_visible)

        intentos += 1

        carta1 = tablero_real[f1][c1]
        carta2 = tablero_real[f2][c2]

        # Comprobación de par: título de una y datos de la otra, y viceversa
        es_par = (
            (carta1['titulo'] == carta2['titulo'] and
             carta1['autor'] == carta2['autor'] and
             carta1['anio'] == carta2['anio'])
        )

        if es_par and (
            (es_titulo and tablero_visible[f1][c1] == carta1['titulo'] and
             tablero_visible[f2][c2] == formatea_carta_datos(carta2)) or
            (not es_titulo and tablero_visible[f1][c1] == formatea_carta_datos(carta1) and
             tablero_visible[f2][c2] == carta2['titulo'])
        ):
            print(Fore.GREEN + "\n¡Correcto! Has encontrado el par:")
            par_str = f"{carta1['titulo']} <> {carta1['autor']}, {carta1['anio']}"
            print(par_str)
            print(Fore.MAGENTA + f"Dato curioso: {carta1['curioso']}\n")
            puntos += puntaje_por_epoca(carta1['epoca'])
            pares_encontrados.append(par_str)
            datos_curiosos.append(f"{carta1['titulo']}: {carta1['curioso']}")
            # Palomita en ambas posiciones
            tablero_visible[f1][c1] = "✔"
            tablero_visible[f2][c2] = "✔"
        else:
            print(Fore.RED + "\n¡No son par!\n")
            # Espera unos segundos para que el usuario vea el error
            time.sleep(1.7)
            tablero_visible[f1][c1] = "??"
            tablero_visible[f2][c2] = "??"

    # Juego terminado
    print(Fore.CYAN + "\n¡Felicidades! ¡Has encontrado todos los pares!")
    mostrar_tablero(tablero_visible)
    print(Fore.YELLOW + f"Intentos totales: {intentos}")
    print(f"Puntaje total: {puntos}")
    print(Fore.GREEN + "Pares encontrados:")
    for par in pares_encontrados:
        print(" - " + par)
    print(Fore.MAGENTA + "Datos curiosos:")
    for dato in datos_curiosos:
        print(" - " + dato)
    print(Style.RESET_ALL)