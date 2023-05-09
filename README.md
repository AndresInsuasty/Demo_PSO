# Demo_PSO
Demostración de algoritmo Particle Swarm Optimization.
Se minimiza funciones matematicas con el algoritmo de Particle swarm optimization.

Se asume de manera didactia que las particulas de enjambres son "peces" y el grupo o enjambre se ha denominado *"cardumen"*.

## Estructura de archivos
.
├── img
├── .pylintrc
├── funciones.py
├── main.py
├── README.md
└── requirements.txt

**funciones.py**: Archivo donde se encuentran las funciones para ser minimizadas.
Ejemplo: 
```python
import numpy as np
def esfera(vector_x):
    """
    Función esfera
    """
    cor_x = vector_x[0]
    cor_y = vector_x[1]
    return cor_x**2 + cor_y**2
```

**main.py**: Archivo principal donde se crea la definición de particula o "pez" y se crea un cardumen de peces para realizar busqueda de un punto minimo en la funcion que se elija.

## Ejemplos de desarrollo

### función multimodal para minimizar
![funcionMultimodal](img/multimodal_function.jpg "Función")

### PSO corriendo
![PSO](img/iteracion_multimodal_4.png "ejecución")
