from canciones_2010s import CANCIONES_2010s
from canciones_1990s_2010 import CANCIONES_1990s_2010
from canciones_1970s_1990 import CANCIONES_1970s_1990
import random

def crear_baraja(num_2010s, num_1990s_2010, num_1970s_1990):
    seleccion_2010s = random.sample(CANCIONES_2010s, num_2010s)
    seleccion_1990s_2010 = random.sample(CANCIONES_1990s_2010, num_1990s_2010)
    seleccion_1970s_1990 = random.sample(CANCIONES_1970s_1990, num_1970s_1990)
    canciones_partida = seleccion_2010s + seleccion_1990s_2010 + seleccion_1970s_1990
    baraja = canciones_partida * 2 
    random.shuffle(baraja)
    return baraja