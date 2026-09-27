# Python 3 — Creador de HTML (Chrome Web Store)

Aplicación de escritorio hecha con **Python 3** y **Tkinter** para generar las páginas **HTML** de una publicación en la Chrome Web Store a partir de una lista de juegos y sus URLs.

## ¿Qué hace?

Es una interfaz gráfica sencilla con dos campos y dos botones:

1. **Ingresar los nombres de los juegos** y **las URLs de los juegos**.
2. **Agregar al documento** → añade una línea a `nombre.txt` y otra a `urls.txt`.
3. **Crear los archivos** → ejecuta el script generador `py.py` 20 veces, que toma esos datos y produce los archivos HTML.

## Archivos

| Archivo | Descripción |
|---|---|
| `creador.py` | Interfaz gráfica (Tkinter) y lógica de escritura. |
| `nombre.txt` | Lista de nombres de juegos (se genera al usar la app). |
| `urls.txt` | Lista de URLs (se genera al usar la app). |
| `py.py` | Script generador de HTML que invoca la app. **No está incluido en el repositorio.** |

## Requisitos

- **Python 3** con **Tkinter** (viene incluido en la mayoría de instalaciones de Python).
- Un archivo `py.py` en la misma carpeta que `creador.py` (el generador de HTML en sí).

## Uso

```bash
python creador.py
```

Escribe el nombre y la URL de cada juego, pulsa **Agregar al documento** por cada uno y, al terminar, **Crear los archivos**.

## Notas

- `nombre.txt` y `urls.txt` se crean en el directorio de trabajo y se van **acumulando** (se abren en modo `a+`); bórralos si quieres empezar de cero.
- El repositorio solo incluye la GUI (`creador.py`); el script `py.py` que genera los HTML no forma parte de él.
