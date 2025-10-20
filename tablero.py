def crear_tablero(renglones, columnas):
    """
    Crea un tablero vacío representado como una lista de listas.
    Cada celda comienza con '??' para indicar que está oculta.
    """
    tablero = []
    for r in range(renglones):
        fila = []
        for c in range(columnas):
            fila.append('??')
        tablero.append(fila)
    return tablero

def mostrar_tablero(tablero):
    """
    Imprime el tablero en pantalla de manera formateada.
    """
    ren = len(tablero)
    col = len(tablero[0])
    
    print("   ", end="")
    for c in range(col):
        print(f"{c+1:>5}", end="")
    print()
    print("   " + "+----"*col + "+")

    for r in range(ren):
        print(f"{r+1:>2} |", end="")
        for c in range(col):
            print(f"{tablero[r][c]:>4}|", end="")
        print()
        print("   " + "+----"*col + "+")