def solicitar_posicion(tablero):
    """
    Solicita al usuario una posición válida (fila y columna) en el tablero.
    Valida que sean números, que estén dentro del rango del tablero,
    y permite salir escribiendo 'salir'.
    Parámetros:
        tablero actual del juego
    Retorna:
        (fila, columna) como tupla de enteros (base 0),
        o ('salir', 'salir') si el usuario lo indica.
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    posicion_valida = False
    while not posicion_valida:
        fila = input(f"Ingrese la fila (1 a {filas}) o 'salir' para terminar: ").strip().lower()
        if fila == "salir":
            return ("salir", "salir")
        columna = input(f"Ingrese la columna (1 a {columnas}) o 'salir' para terminar: ").strip().lower()
        if columna == "salir":
            return ("salir", "salir")
        if fila.isdigit() and columna.isdigit():
            fila = int(fila)
            columna = int(columna)
            if 1 <= fila <= filas and 1 <= columna <= columnas:
                posicion_valida = True
                return (fila-1, columna-1)
            else:
                print("La fila o columna están fuera de rango.")
        else:
            print("Por favor, ingrese números válidos o 'salir'.")