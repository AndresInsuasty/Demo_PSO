"""
Funciones para el algoritmo de optimización
"""
import numpy as np
def esfera(vector_x):
    """
    Función esfera
    """
    cor_x = vector_x[0]
    cor_y = vector_x[1]
    return cor_x**2 + cor_y**2


def multimodal(vector_x):
    """
    Función multimodal
    """
    cor_x = vector_x[0]
    cor_y = vector_x[1]
    term1 = np.sin(cor_x) + np.sin(3 * cor_y)
    term2 = np.sin(2 * cor_x) + np.sin(4 * cor_y)
    return term1 + term2
