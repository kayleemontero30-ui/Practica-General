import time
import timeit
import random as randit 

#Top-down
def caminos_top_down(m, n, memo=None):
    if memo is None:
        memo = {}

    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1: 
        return 1
    
    if (m, n) in memo:
        return memo[(m, n)]
    
    memo[(m, n)] = caminos_top_down(m - 1, n, memo) + caminos_top_down(m, n - 1, memo)
    return memo[(m, n)]

#Bottom-up
def caminos_bottom_up(m, n):
    if m <= 0 or n <= 0:
        return 0
    tabla = [[1] * (n) for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            tabla[i][j] = tabla[i - 1][j] + tabla[i][j - 1]
    
    return tabla[m - 1][n - 1]

def generar_tabla_caminos(m, n):
    if m <= 0 or n <= 0:
        return []

    tabla = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            tabla[i][j] = tabla[i - 1][j] + tabla[i][j - 1]

    return tabla

def imprimir_tabla_bonita(tabla):
    if not tabla:
        print("Tabla vacía")
        return

    ancho = len(str(tabla[-1][-1])) + 1

    print("\nCuadrícula generada:\n")
    for fila in tabla:
        for valor in fila:
            print(f"{valor:>{ancho}}", end="")
        print()


def imprimir_tabla(tabla):
    for fila in tabla:
        print(fila)


#genera valores aleatorios para m y n entre 1 y 15 pero la matriz es siempre cuadrada, es decir, m = n
m = randit.randint(50, 80)
n = randit.randint(50, 80)

print("Cuadricula cuadrada de tamano:", (m, n))
tabla = generar_tabla_caminos(m, n)

print("Caminos Top-Down:", caminos_top_down(m, n))
print("Caminos Bottom-Up:", caminos_bottom_up(m, n))

inicio = time.time()
caminos_top_down(m, n)
fin = time.time()
print("Tiempo Top-Down con time:", fin - inicio)

inicio = time.time()
caminos_bottom_up(m, n)
fin = time.time()
print("Tiempo Bottom-Up con time:", fin - inicio)


t1 = timeit.timeit(lambda: caminos_top_down(m, n), number=100)
t2 = timeit.timeit(lambda: caminos_bottom_up(m, n), number=100)

print("Tiempo Top-Down con timeit:", t1)
print("Tiempo Bottom-Up con timeit:", t2)
print("Cuadricula Generada:")
imprimir_tabla_bonita(tabla)
