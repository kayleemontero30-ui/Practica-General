#numero de fallos permitidos para laberinto con funcion factorial

from math import factorial


def fallos_permitidos(dead_ends):
    n = dead_ends
    return factorial(n)

def calcular_fallos(fallos, n):
    if fallos >= n:
        print("Has alcanzado el número máximo de fallos. Fin del juego.")
        return True
    

def registrar_fallo(n):
    fallos = 0
    ########lo que se cuenta como fallo
    print(f"Fallo {fallos} de {fallos_permitidos}")
    return registrar_fallo  