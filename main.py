"""
Archivo principal del proyecto
Aqui se ejecuta la demostración de la optimización de una función por un enjambre de particulas PSO
"""

# librerias
import numpy as np
import matplotlib.pyplot as plt
from funciones import esfera
#from funciones import multimodal

funcion = esfera
#funcion = multimodal
class Pez:
    """
    Definición de un "pez" (partícula)
    """
    def __init__(self,limites):
        self.posicion = np.random.uniform(limites[0],limites[1],2)
        self.velocidad = np.random.uniform(-1,1,2)
        self.mejor_posicion = self.posicion
        self.mejor_score = np.inf

    def actualizar_velocidad(self, mejor_posicion_cardumen, w, c1, c2):
        """
        Actualiza la velocidad de la partícula
        """
        r1 = np.random.uniform(0,1,2)
        r2 = np.random.uniform(0,1,2)
        self.velocidad = w*self.velocidad + c1*r1*(self.mejor_posicion - self.posicion) + c2*r2*(mejor_posicion_cardumen - self.posicion)

    def actualizar_posicion(self, limites):
        """
        Actualiza la posición de la partícula
        """
        self.posicion = self.posicion + self.velocidad*1
        self.posicion = np.clip(self.posicion, limites[0], limites[1])

    def evaluar_score(self, funcion):
        """
        Evalua el score de la partícula
        """
        score = funcion(self.posicion)
        if score < self.mejor_score:
            self.mejor_score = score
            self.mejor_posicion = self.posicion
        return score


# Algoritmo PSO

def algoritmo_pso(limite,num_peces,max_iteraciones,w,c1,c2):
    """
    Algoritmo de optimización por enjambre de partículas (PSO)
    A cada particula la hemos llamado un "pez" y a todos los peces un "cardumen"
    """
    cardumen_mejor_posicion = np.random.uniform(limite[0],limite[1],2)
    cardumen_mejor_score = float('inf')

    # inicializar cardumen
    cardumen = []
    for _ in range(num_peces):
        pez = Pez(limite)
        cardumen.append(pez)

    # iterar
    for iteracion in range(max_iteraciones):
        for pez in cardumen:
            pez.actualizar_velocidad(cardumen_mejor_posicion,w,c1,c2)
            pez.actualizar_posicion(limite)
            score = pez.evaluar_score(funcion)

            if score < cardumen_mejor_score:
                cardumen_mejor_score = score
                cardumen_mejor_posicion = pez.posicion

            plt.scatter(pez.posicion[0],pez.posicion[1],color='blue',alpha=0.3)
        plt.title(f"PSO. Iteración: {iteracion}")
        plt.xlim(limite[0],limite[1])
        plt.ylim(limite[0],limite[1])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    return cardumen_mejor_posicion, cardumen_mejor_score

# Ejecutar algoritmo
limite = [-5,5]
num_peces = 20
max_iteraciones = 5
w = 0.5
c1 = 0.5
c2 = 0.5
mejor_posicion, mejor_score = algoritmo_pso(limite,num_peces,max_iteraciones,w,c1,c2)
print(f"Mejor posición: {mejor_posicion}")
print(f"Mejor score: {mejor_score}")
