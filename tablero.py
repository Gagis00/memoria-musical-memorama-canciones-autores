'''
Maneja la creación y visualización del tablero del juego
'''

def crear_tablero(renglones, columnas, baraja): #Crea el tablero del juego
    '''
    Crea un tablero con las cartas distribuidas.
    '''
    tablero = [] #Inicializa el tablero vacío
    idx = 0 #Índice para recorrer la baraja
    for i in range(renglones): #Para cada fila
        fila = [] #Inicializa la fila vacía
        for j in range(columnas): #Para cada columna
            fila.append(baraja[idx]) #Agrega una carta a la fila
            idx += 1 #Avanza al siguiente índice de la baraja
        tablero.append(fila) #Agrega la fila al tablero
    return tablero #Regresa el tablero completo

def crear_tablero_visible(renglones, columnas):
    # Tablero lleno de "??"
    return [["??" for _ in range(columnas)] for _ in range(renglones)]

def mostrar_tablero(tablero_visible): 
    '''
    Imprime el tablero formateado
    '''
    ren = len(tablero_visible) # Número de filas
    col = len(tablero_visible[0]) # Número de columnas
    ancho = max([len(str(tablero_visible[r][c])) for r in range(ren) for c in range(col)] + [2]) # Ancho máximo de celda
    print("   ", end="") # imprime los encabezados de columna
    for c in range(col): # Para cada columna
        print(f"{c+1:>{ancho}}", end="") # Imprime el número de columna con el ancho adecuado
    print() 
    print("   " + ("+" + "-"*ancho)*col + "+") # Imprime la línea superior del tablero
    for r in range(ren): # Para cada fila
        print(f"{r+1:>2} |", end="") # Imprime el número de fila
        for c in range(col): # Para cada columna
            print(f"{str(tablero_visible[r][c]):>{ancho}}|", end="") # Imprime el contenido de la celda con el ancho adecuado
        print()
        print("   " + ("+" + "-"*ancho)*col + "+") # Imprime las separaciones