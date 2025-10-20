'''
Inserta las instrucciones desde el .txt de instrucciones
'''

import os #Importar os para manejar rutas de archivos

def mostrar_instrucciones():
    """
    Lee y muestra las instrucciones del juego desde instrucciones.txt,
    siempre en el mismo directorio que este archivo .py
    """
    ruta = os.path.join(os.path.dirname(__file__), "instrucciones.txt") #genera una ruta de acceso a el archivo instrucciones.txt
    try: #Intenta abrir el archivo
        archivo = open(ruta, 'r', encoding='utf-8') #Abrir el archivo en modo lectura con codificación utf-8
        texto = archivo.read() #Leer el contenido del archivo
        print("\n" + texto) #Imprimir el contenido leído
        archivo.close() #Cerrar el archivo
    except FileNotFoundError: #Si no se encuentra el archivo
        print("El archivo instrucciones.txt no se encontró en el mismo directorio que instrucciones.py.") #Mensaje de error