# Memorama Musical 🎵

&nbsp;

## Descripción

Memorama Musical es un juego en el que debes emparejar tarjetas que contienen títulos de canciones famosas con su autor y año. Estimula la memoria, la atención a los detalles y la cultura general, ayudando al desarrollo cognitivo a través del reconocimiento y asociación de información musical.

&nbsp;

> **Objetivo:** Emparejar correctamente títulos de canciones con su autor y año de la canción, poniendo a prueba tu memoria y aprendiendo datos curiosos sobre la música.

&nbsp;

## Datos Generales

- **Materia:** `Programación`
- **Nombre:** `Raúl Antonio Guerrero Canales`
- **Matrícula:** `A01277404`
- **Carrera:** `IMT Ingeniería en Mecatrónica`
- **Fecha:** `19/10/2025`

&nbsp;

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

&nbsp;

## Entrega Inicial

La versión inicial del código base se encuentra en el archivo:  
`codigo_global`

&nbsp;

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

&nbsp;

## Uso

Ejecuta el juego desde la terminal con:

```bash
python main.py
```

Sigue las instrucciones en pantalla para seleccionar cartas, emparejar y sumar puntos.

&nbsp;

## Estructura del Proyecto y Subsistemas

&nbsp;

### main.py

Menú principal, gestiona la interacción del usuario y llama a las funciones del resto de módulos.

```python
Variables:
- opcion: int | Almacena la opción seleccionada por el usuario.

Funciones:
- main(): función principal que muestra el menú y llama a otros módulos.
```

&nbsp;

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

&nbsp;

### baraja.py

Crea y mezcla la baraja de cartas del juego.

```python
Variables:
- baraja: list[dict] | Lista con todas las cartas mezcladas.

Funciones:
- crear_baraja(num_2010s: int, num_1990s_2010: int, num_1970s_1990: int) -> list: genera la baraja con las canciones seleccionadas y las mezcla aleatoriamente.
```

&nbsp;

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

&nbsp;

### solicitar_posicion.py

Valida y solicita la posición que el usuario quiere destapar.

```python
Funciones:
- solicitar_posicion(tablero_visible: list) -> tuple[int, int]: pide y valida la posición de la carta que el usuario quiere destapar.
```

&nbsp;

### validar_opcion.py

Valida las opciones que el usuario introduce en el menú principal.

```python
Funciones:
- validar_opcion_int(entrada: str) -> int: valida que la opción ingresada sea un entero válido.
```

&nbsp;

### presentacion.py

Información general y descripción del juego.

```python
Funciones:
- datos_generales(): muestra autor, materia, matrícula, etc.
- descripcion_juego(): muestra la descripción y beneficios del juego.
```

&nbsp;

### instrucciones.py

Lee y muestra las instrucciones del juego desde el archivo de texto.

```python
Funciones:
- mostrar_instrucciones(): lee e imprime las instrucciones desde instrucciones.txt.
```

&nbsp;

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

&nbsp;

### instrucciones.txt

Contiene instrucciones y reglas detalladas que se muestran al usuario durante la experiencia de juego.

```text
Archivo de texto plano con las reglas y mecánicas del juego.
```

&nbsp;

### codigo_global

Entrega inicial del código base del proyecto.  
Aquí puedes consultar la estructura y lógica original antes de modularizar el proyecto.

&nbsp;

## Bibliografía

Bupa Salud. (s.f.). El juego de memoria para personas mayores: beneficios y tipos. [https://www.bupasalud.com.mx/salud/juego-memoria-personas-mayores](https://www.bupasalud.com.mx/salud/juego-memoria-personas-mayores)  
Jiménez Nájera, M. (2024). Los juegos de mesa potencializan un cerebro ágil y saludable a lo largo de la vida. Observatorio de Innovación Educativa del Tecnológico de Monterrey. [https://observatorio.tec.mx/los-juegos-de-mesa-potencializan-un-cerebro-agil](https://observatorio.tec.mx/los-juegos-de-mesa-potencializan-un-cerebro-agil)  
Equipo Fundación Pasqual Maragall. (2024). Juegos de memoria para adultos: ¿cómo ayudan a ejercitar la mente? [https://blog.fpmaragall.org/juegos-memoria-adultos](https://blog.fpmaragall.org/juegos-memoria-adultos)  

&nbsp;

## Casos de prueba

![caso1](casos_prueba/1.png)
![caso2](casos_prueba/2.png)
![caso3](casos_prueba/3.png)
![caso4](casos_prueba/4.png)
![caso5](casos_prueba/5.png)
![caso6](casos_prueba/6.png)
![caso7](casos_prueba/7.png)
![caso8](casos_prueba/8.png)
![caso9](casos_prueba/9.png)
![caso10](casos_prueba/10.png)
![caso11](casos_prueba/11.png)
![caso12](casos_prueba/12.png)
![caso13](casos_prueba/13.png)
![caso14](casos_prueba/14.png)
![caso15](casos_prueba/15.png)
![caso16](casos_prueba/16.png)
![caso17](casos_prueba/17.png)
![caso18](casos_prueba/18.png)
![caso19](casos_prueba/19.png)
![caso20](casos_prueba/20.png)
![caso21](casos_prueba/21.png)
![caso22](casos_prueba/22.png)
![caso23](casos_prueba/23.png)
![caso24](casos_prueba/24.png)
![caso25](casos_prueba/25.png)
![caso26](casos_prueba/26.png)
![caso27](casos_prueba/27.png)
![caso28](casos_prueba/28.png)
![caso29](casos_prueba/29.png)
![caso30](casos_prueba/30.png)
![caso31](casos_prueba/31.png)
![caso32](casos_prueba/32.png)
![caso33](casos_prueba/33.png)
![caso34](casos_prueba/34.png)
![caso35](casos_prueba/35.png)

&nbsp;

---

Este proyecto fue realizado por **Raúl Antonio Guerrero Canales**  
Estudiante de primer semestre de IMT en el Tec de Monterrey campus Monterrey durante el curso Pensamiento computacional para ingeniería (Gpo 455)

&nbsp;

`Pd: Me esforce mucho en este proyecto, fue complicado ya que nunca había realizado algo asi en python pero me diverti mucho en este mini proyecto aparte me encanta la musica!! y es una meta personal unir tanto tecnología accesible como música`