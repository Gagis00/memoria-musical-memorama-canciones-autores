# Memorama Musical 🎵

**El objetivo principal de este juego es emparejar correctamente tarjetas que contienen títulos de canciones famosas con su autor y año de la canción. Estimulando la memoria, la atención a los detalles y, muy importante, cultura general o aprendizaje cultural.**

---

## Descripción

Memorama Musical: Empareja tarjetas con títulos de canciones, autores y años.

El objetivo es estimular la memoria, atención y aprendizaje cultural, ayudando al desarrollo cognitivo a través del reconocimiento y asociación de información musical.

---

## Datos Generales

- **Materia:** Programación
- **Nombre:** Raúl Antonio Guerrero Canales
- **Matrícula:** A01277404
- **Carrera:** IMT Ingeniería en Mecatrónica
- **Fecha:** 19/10/2025

---

## Reglas e Instrucciones

1. El objetivo es emparejar correctamente tarjetas que contienen títulos de canciones famosas con su autor y año de la canción.
2. El tablero es de 4x4, con 8 canciones y sus pares correspondientes (cada par consta de una carta con el título y otra con el autor y año).
3. En cada ronda puedes voltear dos cartas. Si forman el par correcto (título y autor/año de la misma canción), se retiran del tablero y sumas puntos.
4. Si no logras emparejar, las cartas se vuelven a poner boca abajo y se suma un intento.
5. El juego termina cuando se han emparejado todos los pares o cuando decides salir escribiendo 'salir' al seleccionar fila o columna.
6. El puntaje final toma en cuenta los aciertos, los intentos y la época de las canciones.
7. Al hacer un par correcto, se muestra un dato curioso de la canción.

¡Diviértete y pon a prueba tu memoria musical!

---

## Instalación

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/Gagis00/memoria-musical-memorama-canciones-autores.git
    cd memoria-musical-memorama-canciones-autores
    ```

2. **Instala las dependencias (Python 3.7+):**
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

## Estructura del Proyecto

- **main.py**: Menú principal y arranque del juego.
- **juego.py**: Lógica principal del memorama.
- **baraja.py**: Crea y mezcla la baraja de cartas.
- **tablero.py**: Genera y muestra el tablero.
- **solicitar_posicion.py**: Valida y solicita las posiciones de las cartas.
- **canciones_2010s.py**, **canciones_1990s_2010.py**, **canciones_1970s_1990.py**: Listas de canciones por década.
- **presentacion.py**: Información general y descripción.
- **instrucciones.txt**: Reglas detalladas del juego.

---

