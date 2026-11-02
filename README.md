# Sistema de biblioteca CarUPS

El programa administra el catálogo, los socios y el análisis de préstamos de una biblioteca pequeña mediante diccionarios y conjuntos de Python.

## Requisitos

- Python 3.

El proyecto utiliza únicamente estructuras y funciones nativas de Python. No requiere instalar paquetes externos.

## Ejecución

Desde la carpeta `unidad_2`, ejecute:

```bash
python main.py
```

## Funcionalidades

### R1 Catálogo de libros

El catálogo utiliza un diccionario (`dict`). El código del libro es la clave y el título y autor conforman su valor. Permite registrar libros y buscarlos directamente por código.

### R2 Catálogo ordenado

El catálogo se presenta en orden ascendente de código mediante `sorted()`. Un TreeMap mantendría las claves ordenadas permanentemente mediante un árbol balanceado, mientras que `dict` prioriza el acceso promedio O(1) y no mantiene orden por clave.

### R3 Socios registrados

Los identificadores de socios se almacenan en un conjunto (`set`). Esta estructura evita duplicados y permite verificar rápidamente si un socio ya está registrado.

### R4 Análisis de préstamos

Los préstamos de novela y ciencia se representan mediante dos conjuntos. El programa calcula:

- Socios que leen ambos géneros mediante intersección.
- Socios que solo leen novela mediante diferencia.
- Total de socios distintos con préstamos mediante unión.

## Complejidad temporal

| Requerimiento | Operación                            | Complejidad promedio |
| ------------- | ------------------------------------ | -------------------: |
| R1            | Registrar un libro en el diccionario |                 O(1) |
| R1            | Buscar un libro por código           |                 O(1) |
| R2            | Ordenar el catálogo con `sorted()`   |           O(n log n) |
| R3            | Registrar o verificar un socio       |                 O(1) |
| R4            | Unión, intersección y diferencia     |             O(n + m) |

`n` y `m` representan las cantidades de elementos procesados.

## Estructura del proyecto

```text
unidad_2/
├── main.py
├── utilidades.py
├── README.md
└── .gitignore
```
