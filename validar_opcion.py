def validar_opcion_int(opcion):
    """
    valida que la opcion ingresada en el menu principal sea un entero
    si no lo es, solicita al usuario hasta obtener un valor valido
    """
    valido = False 
    while not valido:
        try:
            opcion = int(opcion)
            valido = True
        except:
            print("Error, opción no válida")
            opcion = input("Opción deseada: ")
    return opcion