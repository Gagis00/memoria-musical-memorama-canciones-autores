def validar_opcion_int(opcion):
    """
    Valida que la opción ingresada sea un entero.
    Si no lo es, solicita al usuario hasta obtener un valor válido.
    Parámetros:
        opcion ingresada por el usuario
    Regresa:
        la opcion validada como un entero
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