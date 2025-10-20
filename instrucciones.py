def abre_instrucciones(nombre_archivo="instrucciones.txt"):
    """
    Abre el archivo de instrucciones.
    Si no existe, pide repetir hasta que se proporcione un archivo válido.
    """
    existe = False
    while not existe:
        try:
            archivo = open(nombre_archivo, 'r', encoding='utf-8')
            existe = True
        except FileNotFoundError:
            print('El archivo no existe. Intenta de nuevo.')
            nombre_archivo = input("Nombre del archivo de instrucciones: ")
    return archivo

def mostrar_instrucciones():
    """
    Lee y muestra las instrucciones del juego desde instrucciones.txt.
    """
    archivo = abre_instrucciones()
    texto = archivo.read()
    print("\n" + texto)
    archivo.close()