#Implementa un Borgo Sort y luego algortimo de ordenación de tu elección para organizar una lista de
#números enteros en orden ascendente.
#Tareas:
<<<<<<< HEAD
#Escribe el código para el algoritmo en el lenguaje de programación que prefieras (no necesariamente
=======
#scribe el código para el algoritmo en el lenguaje de programación que prefieras (no necesariamente
>>>>>>> db6451f2b3fb930b6dfd7419b2a3a9ab0fd54f9e
#Python).
#Asegúrate de probar tu implementación con al menos tres conjuntos de datos diferentes.
#Prueba al menos una lista aleatoria, una ordenada y una invertida. Para el Bogo Sort usa una lista de 8 o
#menos elementos.
#Mide empíricamente la complejidad temporal.

<<<<<<< HEAD
Import random

BogoSort(lista):
    Mientras la lista no este ordenada:
        Generar una permutacion aleatoria de la lista
    Retornar la lista ordenada
=======
import random 

def BogoSort(lista):
    while not esta_ordenada(lista):
        random.shuffle(lista)
    return lista

def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

lista_aleatoria = [5, 2, 9, 1, 5, 6]
>>>>>>> db6451f2b3fb930b6dfd7419b2a3a9ab0fd54f9e
