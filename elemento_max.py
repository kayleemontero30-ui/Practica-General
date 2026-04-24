import time
import timeit
import cProfile
import random
from memory_profiler import profile

@profile
def find_max_twice(arr):
    max_val = arr[0]
    for num in arr:
            if num > max_val:
                max_val = num

    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

@profile
def find_max_detailed(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        current_element = arr[i]
        if current_element > max_val:
            max_val = current_element

    return max_val

def array_prueba(n):
    return [random.randint(1, 1000000) for _ in range(n)]

arr = array_prueba(100000)
max1 = find_max_detailed(arr)
max2 = find_max_twice(arr)

print("Máximo método 1:", max1)
print("Máximo método 2:", max2)
print("¿Dan el mismo resultado?", max1 == max2)

t1 = timeit.timeit(lambda: find_max_detailed(arr), number=100)
t2 = timeit.timeit(lambda: find_max_twice(arr), number=100)
print("Comparacion de tiempos:")
print("Método 1:", t1)
print("Método 2:", t2)
if t1 < t2:
    print(f"\nComparación: Método 1 < Método 2")
    print(f"El método 1 es más rápido que el método 2 por {t2 - t1:.8f} s en total.")
    print(f"Conclusión: el mejor método en tiempo es el Método 1.")
elif t1 > t2:
    print(f"\nComparación: Método 1 > Método 2")
    print(f"El método 2 es más rápido que el método 1 por {t1 - t2:.8f} s en total.")
    print(f"Conclusión: el mejor método en tiempo es el Método 2.")
else:
    print(f"\nComparación: Método 1 = Método 2")
    print("Conclusión: ambos métodos tardan prácticamente lo mismo.")


print("cProfile para cada método:")
print("Metodo 1:")
cProfile.run("find_max_detailed(arr)")
print("Metodo 2:")
cProfile.run("find_max_twice(arr)")


