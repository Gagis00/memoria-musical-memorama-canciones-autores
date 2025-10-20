def crear_tablero(renglones, columnas, baraja):
    # Llena el tablero real con objetos de canciones de la baraja
    tablero = []
    idx = 0
    for i in range(renglones):
        fila = []
        for j in range(columnas):
            fila.append(baraja[idx])
            idx += 1
        tablero.append(fila)
    return tablero

def crear_tablero_visible(renglones, columnas):
    # Tablero que ve el usuario: solo "??" al principio
    return [["??" for _ in range(columnas)] for _ in range(renglones)]

def mostrar_tablero(tablero_visible):
    ren = len(tablero_visible)
    col = len(tablero_visible[0])
    print("   ", end="")
    for c in range(col):
        print(f"{c+1:>5}", end="")
    print()
    print("   " + "+----"*col + "+")
    for r in range(ren):
        print(f"{r+1:>2} |", end="")
        for c in range(col):
            print(f"{tablero_visible[r][c]:>4}|", end="")
        print()
        print("   " + "+----"*col + "+")