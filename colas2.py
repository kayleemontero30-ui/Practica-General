#Cola: Simula una fila de personas esperando para ser atendidas en una tienda.
#• Cada vez que llega una persona, se coloca al final de la fila.
#• Cada vez que una persona es atendida, se retira de la fila.
#• Instrucciones: Crea una cola con deque y añade cinco personas. Luego, retira a las tres primeras
#personas que llegaron. A las personas que no sean atendidas dales un descuento para el próximo día.
#Muestra el estado de la cola después de cada operación

from collections import deque
cola = deque()

cola.append("Maria")
print (cola)
cola.append("Sara Nieto")
print (cola)
cola.append("Pedro")
print (cola)
cola.append("Ana")
print (cola)
cola.append("Luis")
print (cola)


cola.popleft()
print (cola)
cola.popleft()
print (cola)
cola.popleft()
print (cola)