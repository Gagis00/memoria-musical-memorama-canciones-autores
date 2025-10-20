import os

def mostrar_instrucciones():
    """
    Lee y muestra las instrucciones del juego desde instrucciones.txt,
    siempre en el mismo directorio que este archivo .py
    """
    ruta = os.path.join(os.path.dirname(__file__), "instrucciones.txt")
    try:
        archivo = open(ruta, 'r', encoding='utf-8')
        texto = archivo.read()
        print("\n" + texto)
        archivo.close()
    except FileNotFoundError:
        print("El archivo instrucciones.txt no se encontró en el mismo directorio que instrucciones.py.")