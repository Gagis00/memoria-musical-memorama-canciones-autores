def solicitar_posicion(tablero):
    """
    Solicita al usuario una posición válida (fila y columna) en el tablero.
    Valida que sean números y que estén dentro del rango del tablero.
    Parámetros:
        tablero actual del juego
    Retorna:
        Peticion de la fila y columna para su uso posterior
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    posicion_valida = False
    while not posicion_valida:
        fila = input(f"Ingrese la fila (1 a {filas}): ")
        columna = input(f"Ingrese la columna (1 a {columnas}): ")
        if fila.isdigit() and columna.isdigit():
            fila = int(fila)
            columna = int(columna)
            if 1 <= fila <= filas and 1 <= columna <= columnas:
                posicion_valida = True
                return (fila-1, columna-1)
            else:
                print("La fila o columna están fuera de rango.")
        else:
            print("Por favor, ingrese números válidos para fila y columna.")