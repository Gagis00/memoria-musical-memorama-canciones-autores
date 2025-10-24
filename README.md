# Memorama Musical 🎵

## Descripción

Memorama Musical es un juego en el que debes emparejar tarjetas que contienen títulos de canciones famosas con su autor y año. Estimula la memoria, la atención a los detalles y la cultura general, ayudando al desarrollo cognitivo a través del reconocimiento y asociación de información musical.

> **Objetivo:** Emparejar correctamente títulos de canciones con su autor y año de la canción, poniendo a prueba tu memoria y aprendiendo datos curiosos sobre la música.

---

## Datos Generales

- **Materia:** `Programación`
- **Nombre:** `Raúl Antonio Guerrero Canales`
- **Matrícula:** `A01277404`
- **Carrera:** `IMT Ingeniería en Mecatrónica`
- **Fecha:** `19/10/2025`

---

## Reglas e Instrucciones

> **1.** El objetivo es emparejar correctamente tarjetas que contienen títulos de canciones famosas con su autor y año de la canción.  
> **2.** El tablero es de 4x4, con 8 canciones y sus pares correspondientes (cada par consta de una carta con el título y otra con el autor y año).  
> **3.** En cada ronda puedes voltear dos cartas. Si forman el par correcto (título y autor/año de la misma canción), se retiran del tablero y sumas puntos.  
> **4.** Si no logras emparejar, las cartas se vuelven a poner boca abajo y se suma un intento.  
> **5.** El juego termina cuando se han emparejado todos los pares o cuando decides salir escribiendo `salir` al seleccionar fila o columna.  
> **6.** El puntaje final toma en cuenta los aciertos, los intentos y la época de las canciones.  
> **7.** Al hacer un par correcto, se muestra un dato curioso de la canción.  
>
> ¡Diviértete y pon a prueba tu memoria musical!

---

## Entrega Inicial

La versión inicial del código base se encuentra en el archivo:  
`codigo_global`

---

## Instalación

Clona el repositorio:
```bash
git clone https://github.com/Gagis00/memoria-musical-memorama-canciones-autores.git
cd memoria-musical-memorama-canciones-autores
```
Instala las dependencias (Python 3.7+):
```bash
pip install colorama
```

---

## Uso

Ejecuta el juego desde la terminal con:

```bash
python main.py
```

Sigue las instrucciones en pantalla para seleccionar cartas, emparejar y sumar puntos.

---

## Estructura del Proyecto y Subsistemas

---

### main.py
Menú principal, gestiona la interacción del usuario y llama a las funciones del resto de módulos.

```python
Variables:
- opcion: int | Almacena la opción seleccionada por el usuario.

Funciones:
- main(): función principal que muestra el menú y llama a otros módulos.
```

---

### juego.py
Lógica principal del memorama. Controla puntaje, intentos, pares encontrados y estado del tablero.

```python
Variables:
- puntos: int | Puntaje acumulado por el jugador.
- intentos: int | Número de intentos realizados.
- pares_encontrados: list[str] | Pares correctos encontrados.
- datos_curiosos: list[str] | Datos curiosos mostrados tras cada par.
- tablero_real: list[list[dict]] | Matriz con las cartas reales (título/datos).
- tablero_visible: list[list[str]] | Matriz con el estado actual visible del tablero.

Funciones:
- jugar(): función principal, contiene la lógica del juego.
- puntaje_por_epoca(epoca: str) -> int: calcula el puntaje según la década de la canción.
- todas_descubiertas(tablero_visible: list) -> bool: verifica si todas las cartas están descubiertas.
- formatea_carta_titulo(carta: dict) -> str: da formato al título de la carta.
- formatea_carta_datos(carta: dict) -> str: da formato a los datos de la carta.
```

---

### baraja.py
Crea y mezcla la baraja de cartas del juego.

```python
Variables:
- baraja: list[dict] | Lista con todas las cartas mezcladas.

Funciones:
- crear_baraja(num_2010s: int, num_1990s_2010: int, num_1970s_1990: int) -> list: genera la baraja con las canciones seleccionadas y las mezcla aleatoriamente.
```

---

### tablero.py
Genera y muestra el tablero visible y real.

```python
Variables:
- tablero: list[list[dict]] | Matriz con las cartas organizadas en filas y columnas.
- tablero_visible: list[list[str]] | Matriz que muestra el estado visible ("??", título, datos, "✔").

Funciones:
- crear_tablero(renglones: int, columnas: int, baraja: list) -> list: organiza las cartas en el tablero.
- crear_tablero_visible(renglones: int, columnas: int) -> list: crea la matriz con todas las cartas cubiertas.
- mostrar_tablero(tablero_visible: list): imprime el tablero visible en terminal.
```

---

### solicitar_posicion.py
Valida y solicita la posición que el usuario quiere destapar.

```python
Funciones:
- solicitar_posicion(tablero_visible: list) -> tuple[int, int]: pide y valida la posición de la carta que el usuario quiere destapar.
```

---

### validar_opcion.py
Valida las opciones que el usuario introduce en el menú principal.

```python
Funciones:
- validar_opcion_int(entrada: str) -> int: valida que la opción ingresada sea un entero válido.
```

---

### presentacion.py
Información general y descripción del juego.

```python
Funciones:
- datos_generales(): muestra autor, materia, matrícula, etc.
- descripcion_juego(): muestra la descripción y beneficios del juego.
```

---

### instrucciones.py
Lee y muestra las instrucciones del juego desde el archivo de texto.

```python
Funciones:
- mostrar_instrucciones(): lee e imprime las instrucciones desde instrucciones.txt.
```

---

### canciones_2010s.py, canciones_1990s_2010.py, canciones_1970s_1990.py
Listas de canciones por década. Cada lista incluye el título, autor, año, época y un dato curioso.

```python
Variables:
- CANCIONES_2010s: list[dict] | Lista de canciones de los 2010s.
- CANCIONES_1990s_2010: list[dict] | Lista de canciones de 1990s a 2010.
- CANCIONES_1970s_1990: list[dict] | Lista de canciones de 1970s a 1990.

Funciones:
- No tienen funciones, solo almacenan los datos.
```

---

### instrucciones.txt
Contiene instrucciones y reglas detalladas que se muestran al usuario durante la experiencia de juego.

```text
Archivo de texto plano con las reglas y mecánicas del juego.
```

---

### codigo_global
Entrega inicial del código base del proyecto.  
Aquí puedes consultar la estructura y lógica original antes de modularizar el proyecto.

---