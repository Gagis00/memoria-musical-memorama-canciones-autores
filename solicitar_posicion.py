def solicitar_posicion(tablero):
    """
    Solicita al usuario una posición válida (fila y columna) en el tablero.
    Valida que sean números, que estén dentro del rango del tablero,
    y permite salir escribiendo 'salir'.
    """
    filas = len(tablero) #Número de filas en el tablero
    columnas = len(tablero[0]) #Número de columnas en el tablero
    posicion_valida = False #Inicializa la validación de posición
    while not posicion_valida: #Mientras la posición no sea válida
        fila = input(f"Ingrese la fila (1 a {filas}) o 'salir' para terminar: ").strip().lower() #Solicita la fila
        if fila == "salir": 
            return ("salir", "salir")
        columna = input(f"Ingrese la columna (1 a {columnas}) o 'salir' para terminar: ").strip().lower() #Solicita la columna
        if columna == "salir":
            return ("salir", "salir")
        if fila.isdigit() and columna.isdigit(): #Verifica si ambos son dígitos
            fila = int(fila) #Convierte fila a entero
            columna = int(columna) #Convierte columna a entero
            if 1 <= fila <= filas and 1 <= columna <= columnas: #Verifica si están dentro del rango
                posicion_valida = True #Marca la posición como válida
                return (fila-1, columna-1) #Retorna la posición real
            else:
                print("La fila o columna están fuera de rango.") #Mensaje de error por rango
        else:
            print("Por favor, ingrese números válidos o 'salir'.") #Mensaje de error por formato