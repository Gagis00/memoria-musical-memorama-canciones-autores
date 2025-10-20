def mostrar_instrucciones():
    """
    Lee y muestra las instrucciones del juego desde instrucciones.txt.
    """
    try:
        archivo = open("instrucciones.txt", 'r', encoding='utf-8')
        texto = archivo.read()
        print("\n" + texto)
        archivo.close()
    except FileNotFoundError:
        print("El archivo instrucciones.txt no se encontró en la carpeta actual.")