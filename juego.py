from colorama import Fore, Style
from baraja import crear_baraja
from tablero import crear_tablero, crear_tablero_visible, mostrar_tablero
from solicitar_posicion import solicitar_posicion

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
    renglones = 4
    columnas = 4

    baraja = crear_baraja(1, 3, 4)
    tablero_real = crear_tablero(renglones, columnas, baraja)
    tablero_visible = crear_tablero_visible(renglones, columnas)

    puntos = 0
    intentos = 0
    pares_encontrados = []
    datos_curiosos = []

    print(Fore.CYAN + "El juego comienza con un tablero cubierto. ¡Listo para comenzar?\n")
    mostrar_tablero(tablero_visible)

    juego_activo = True
    while juego_activo and not todas_descubiertas(tablero_visible):
        print(Fore.YELLOW + f"\nIntentos: {intentos}")
        print(f"Puntaje: {puntos}")
        if pares_encontrados:
            print(Fore.GREEN + "Pares encontrados:")
            for par in pares_encontrados:
                print(" - " + par)
            print(Fore.MAGENTA + "Datos curiosos:")
            for dato in datos_curiosos:
                print(" - " + dato)
        print(Style.RESET_ALL)

        seleccion_valida_1 = False
        while not seleccion_valida_1 and juego_activo:
            f1, c1 = solicitar_posicion(tablero_visible)
            if f1 == "salir":
                print("¡Juego terminado por el usuario!")
                juego_activo = False
            elif tablero_visible[f1][c1] == "??":
                seleccion_valida_1 = True
            else:
                print(Fore.RED + "¡Esa carta ya está descubierta! Elige otra.")

        if not juego_activo:
            return

        tablero_visible[f1][c1] = formatea_carta_titulo(tablero_real[f1][c1])
        mostrar_tablero(tablero_visible)

        seleccion_valida_2 = False
        while not seleccion_valida_2 and juego_activo:
            f2, c2 = solicitar_posicion(tablero_visible)
            if f2 == "salir":
                print("¡Juego terminado por el usuario!")
                juego_activo = False
            elif tablero_visible[f2][c2] == "??" and (f2, c2) != (f1, c1):
                seleccion_valida_2 = True
            else:
                print(Fore.RED + "¡Esa carta ya está descubierta o es la misma! Elige otra.")

        if not juego_activo:
            return

        tablero_visible[f2][c2] = formatea_carta_datos(tablero_real[f2][c2])
        mostrar_tablero(tablero_visible)

        intentos += 1

        carta1 = tablero_real[f1][c1]
        carta2 = tablero_real[f2][c2]

        es_par = (
            carta1['titulo'] == carta2['titulo']
            and carta1['autor'] == carta2['autor']
            and carta1['anio'] == carta2['anio']
        )

        if es_par:
            print(Fore.GREEN + "\n¡Correcto! Has encontrado el par:")
            par_str = f"{carta1['titulo']} <> {carta1['autor']}, {carta1['anio']}"
            print(par_str)
            print(Fore.MAGENTA + f"Dato curioso: {carta1['curioso']}\n")
            puntos += puntaje_por_epoca(carta1['epoca'])
            pares_encontrados.append(par_str)
            datos_curiosos.append(f"{carta1['titulo']}: {carta1['curioso']}")
            tablero_visible[f1][c1] = "✔"
            tablero_visible[f2][c2] = "✔"
        else:
            print(Fore.RED + "\n¡No son par!\n")
            tablero_visible[f1][c1] = "??"
            tablero_visible[f2][c2] = "??"

    print(Fore.CYAN + "\n¡Felicidades! ¡Has encontrado todos los pares o has salido del juego!")
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