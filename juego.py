from colorama import Fore
from baraja import crear_baraja
from tablero import crear_tablero, crear_tablero_visible, mostrar_tablero
from solicitar_posicion import solicitar_posicion

def puntaje_por_epoca(epoca):
    if epoca == "2010s":
        return 1
    elif epoca == "1990s-2010":
        return 2
    elif epoca == "1970s-1990":
        return 3
    else:
        return 1

def todas_descubiertas(tablero_visible):
    return all(cell != "??" for row in tablero_visible for cell in row)

def formatea_carta(carta):
    return f"{carta['titulo']} <> {carta['autor']}, {carta['anio']}"

def jugar():
    print("\n¡Comienza el juego!")
    renglones = 6
    columnas = 6

    baraja = crear_baraja(3, 6, 9)
    tablero_real = crear_tablero(renglones, columnas, baraja)
    tablero_visible = crear_tablero_visible(renglones, columnas)

    puntos = 0
    intentos = 0
    seguir_jugando = True
    pares_encontrados = []
    datos_curiosos = []

    while seguir_jugando and not todas_descubiertas(tablero_visible):
        mostrar_tablero(tablero_visible)
        print(Fore.YELLOW + f"\nIntentos: {intentos}")
        print("Pares encontrados:")
        for par in pares_encontrados:
            print(f"- {par}")
        print("Datos interesantes:")
        for dato in datos_curiosos:
            print(f"- {dato}")
        print("-" * 60)

        # Primera carta
        print("Ingresa la columna y la fila de la primera carta que quieres levantar")
        f1, c1 = solicitar_posicion(tablero_visible)
        carta1 = tablero_real[f1][c1]
        tablero_visible[f1][c1] = formatea_carta(carta1)
        mostrar_tablero(tablero_visible)

        # Segunda carta
        print("Ingresa la columna y la fila de la segunda carta que quieres levantar")
        f2, c2 = solicitar_posicion(tablero_visible)
        carta2 = tablero_real[f2][c2]
        tablero_visible[f2][c2] = formatea_carta(carta2)
        mostrar_tablero(tablero_visible)

        # Sumar intento
        intentos += 1

        # Revisar si es par
        if (f1, c1) != (f2, c2) and \
           carta1['titulo'] == carta2['titulo'] and \
           carta1['autor'] == carta2['autor'] and \
           carta1['anio'] == carta2['anio']:
            print(Fore.GREEN + f";Correcto! Has encontrado el par:\n{formatea_carta(carta1)}")
            print(f"Dato curioso: {carta1['curioso']}\n")
            puntos += puntaje_por_epoca(carta1['epoca'])
            # Guarda par y dato para mostrar en la lista
            pares_encontrados.append(formatea_carta(carta1))
            datos_curiosos.append(f"{carta1['titulo']} <> {carta1['autor']}, {carta1['anio']}: {carta1['curioso']}")
        else:
            print(Fore.RED + "No es par. Intenta de nuevo.")
            tablero_visible[f1][c1] = "??"
            tablero_visible[f2][c2] = "??"

        # Preguntar si seguir jugando (igual que antes)
        if not todas_descubiertas(tablero_visible):
            respuesta = input("¿Deseas seguir jugando? (s/n): ").strip().lower()
            while respuesta not in ["s", "n"]:
                respuesta = input("Por favor ingresa 's' para sí o 'n' para no: ").strip().lower()
            if respuesta == "n":
                seguir_jugando = False

    # Mensaje final
    if todas_descubiertas(tablero_visible):
        print(Fore.MAGENTA + "¡Felicidades! Has encontrado todos los pares.")
    print(f"Puntaje final por canciones: {puntos}")
    print(f"Intentos totales: {intentos}")

    print("Resumen de pares encontrados:")
    for par in pares_encontrados:
        print(f"- {par}")
    print("Resumen de datos interesantes:")
    for dato in datos_curiosos:
        print(f"- {dato}")