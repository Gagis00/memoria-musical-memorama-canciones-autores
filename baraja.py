'''
Creamos la baraja con canciones de diferentes décadas
'''

from canciones_2010s import CANCIONES_2010s #regresa las canciones de los 2010s
from canciones_1990s_2010 import CANCIONES_1990s_2010 #regresa las canciones de los 1990s a 2010
from canciones_1970s_1990 import CANCIONES_1970s_1990 #regresa las canciones de los 1970s a 1990
import random #Inicia un random

def crear_baraja(num_2010s, num_1990s_2010, num_1970s_1990): 
    '''
    Crea una baraja mezclada con canciones de diferentes décadas.
    '''
    seleccion_2010s = random.sample(CANCIONES_2010s, num_2010s) #Selecciona canciones aleatorias de los 2010s
    seleccion_1990s_2010 = random.sample(CANCIONES_1990s_2010, num_1990s_2010) #Selecciona canciones aleatorias de los 1990s a 2010
    seleccion_1970s_1990 = random.sample(CANCIONES_1970s_1990, num_1970s_1990) #Selecciona canciones aleatorias de los 1970s a 1990
    canciones_partida = seleccion_2010s + seleccion_1990s_2010 + seleccion_1970s_1990 #Combina todas las selecciones
    baraja = [] #Inicializa la baraja vacía
    for cancion in canciones_partida: #Para cada canción seleccionada
        baraja.append({"tipo": "titulo", **cancion}) #Agrega el título a la baraja
        baraja.append({"tipo": "datos", **cancion}) #Agrega los datos del autor a la baraja
    random.shuffle(baraja) #Mezcla la baraja
    return baraja #Regresa la baraja mezclada