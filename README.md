# Memorama Musical 🎵

> **El objetivo principal de este juego es emparejar correctamente tarjetas que contienen títulos de canciones famosas con su autor y año de la canción. Estimulando la memoria, la atención a los detalles y, muy importante, cultura general o aprendizaje cultural.**

---

## Descripción

> Memorama Musical: Empareja tarjetas con títulos de canciones, autores y años.  
> El objetivo es **estimular la memoria, atención y aprendizaje cultural**, ayudando al desarrollo cognitivo a través del reconocimiento y asociación de información musical.

---

## Datos Generales

- **Materia:** `Programación`
- **Nombre:** `Raúl Antonio Guerrero Canales`
- **Matrícula:** `A01277404`
- **Carrera:** `IMT Ingeniería en Mecatrónica`
- **Fecha:** `19/10/2025`

---

## Reglas e Instrucciones

> 1. El objetivo es emparejar correctamente tarjetas que contienen títulos de canciones famosas con su autor y año de la canción.
> 2. El tablero es de 4x4, con 8 canciones y sus pares correspondientes (cada par consta de una carta con el título y otra con el autor y año).
> 3. En cada ronda puedes voltear dos cartas. Si forman el par correcto (título y autor/año de la misma canción), se retiran del tablero y sumas puntos.
> 4. Si no logras emparejar, las cartas se vuelven a poner boca abajo y se suma un intento.
> 5. El juego termina cuando se han emparejado todos los pares o cuando decides salir escribiendo `salir` al seleccionar fila o columna.
> 6. El puntaje final toma en cuenta los aciertos, los intentos y la época de las canciones.
> 7. Al hacer un par correcto, se muestra un dato curioso de la canción.
>
> **¡Diviértete y pon a prueba tu memoria musical!**

---

## Instalación

> **Clona el repositorio:**
> 
> ```bash
> git clone https://github.com/Gagis00/memoria-musical-memorama-canciones-autores.git
> cd memoria-musical-memorama-canciones-autores
> ```
>
> **Instala las dependencias (Python 3.7+):**
> 
> ```bash
> pip install colorama
> ```

---

## Uso

> Ejecuta el juego desde la terminal con:
> 
> ```bash
> python main.py
> ```
> 
> Sigue las instrucciones en pantalla para seleccionar cartas, emparejar y sumar puntos.

---

## Estructura del Proyecto y Subsistemas

> ### `main.py`
> Menú principal, gestiona la interacción del usuario y llama a las funciones del resto de módulos.

```python
Variables:
- Ninguna significativa (solo variables locales de menú).

Funciones:
- main(): Muestra el menú principal, gestiona la interacción del usuario y llama a las funciones del resto de módulos.
```

> ### `juego.py`
> Lógica principal del memorama, aquí se controlan el puntaje, los intentos y el estado del tablero.

```python
Variables:
- puntos: puntaje acumulado por el jugador.
- intentos: número de intentos realizados.
- pares_encontrados: lista de pares correctos encontrados.
- datos_curiosos: lista de datos curiosos mostrados tras cada par.
- tablero_real: matriz con las cartas reales (título/datos).
- tablero_visible: matriz con el estado actual visible del tablero.

Funciones:
- jugar(): función principal, contiene la lógica del juego.
- puntaje_por_epoca(): calcula el puntaje según la década de la canción.
- todas_descubiertas(): verifica si todas las cartas están descubiertas.
- formatea_carta_titulo(): da formato al título de la carta.
- formatea_carta_datos(): da formato a los datos de la carta.
```

> ### `baraja.py`
> Crea y mezcla la baraja de cartas del juego.

```python
Variables:
- baraja: lista con todas las cartas mezcladas (cada canción tiene dos cartas: título y datos).

Funciones:
- crear_baraja(): genera la baraja con las canciones seleccionadas y las mezcla aleatoriamente.
```

> ### `tablero.py`
> Genera y muestra el tablero visible y real.

```python
Variables:
- tablero: matriz con las cartas organizadas en filas y columnas.
- tablero_visible: matriz que muestra el estado visible ("??", título, datos, "✔").

Funciones:
- crear_tablero(): organiza las cartas en el tablero.
- crear_tablero_visible(): crea la matriz con todas las cartas cubiertas.
- mostrar_tablero(): imprime el tablero visible en terminal.
```

> ### `solicitar_posicion.py`
> Valida y solicita la posición que el usuario quiere destapar.

```python
Funciones:
- solicitar_posicion(): pide y valida la posición de la carta que el usuario quiere destapar.
```

> ### `canciones_2010s.py`, `canciones_1990s_2010.py`, `canciones_1970s_1990.py`
> Listas de canciones por década, cada una incluye el título, autor, año, época y un dato curioso.

```python
Variables:
- CANCIONES_2010s, CANCIONES_1990s_2010, CANCIONES_1970s_1990: listas de diccionarios con información de cada canción (título, autor, año, dato curioso, época).

Funciones:
- No tienen funciones, solo almacenan los datos.
```

> ### `presentacion.py`
> Información general y descripción del juego.

```python
Funciones:
- datos_generales(): muestra autor, materia, matrícula, etc.
- descripcion_juego(): muestra la descripción y beneficios del juego.
```

> ### `instrucciones.txt`
> Contiene las instrucciones y reglas detalladas del juego, que se muestran al usuario durante la experiencia de juego.

---