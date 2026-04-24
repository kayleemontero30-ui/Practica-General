#Implementa un Borgo Sort y luego algortimo de ordenación de tu elección para organizar una lista de
#números enteros en orden ascendente.
#Tareas:
#scribe el código para el algoritmo en el lenguaje de programación que prefieras (no necesariamente
#Python).
#Asegúrate de probar tu implementación con al menos tres conjuntos de datos diferentes.
#Prueba al menos una lista aleatoria, una ordenada y una invertida. Para el Bogo Sort usa una lista de 8 o
#menos elementos.
#Mide empíricamente la complejidad temporal.

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