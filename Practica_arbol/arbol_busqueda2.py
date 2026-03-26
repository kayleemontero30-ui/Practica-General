#Implementar un árbol binario de búsqueda (BST) y realizar los tres recorridos en Python.
# Crear un árbol con al menos 6 nodos, usando clases y objetos.
# Implementar funciones para realizar preorden, inorden, y postorden.
# Ejecuta varios ejemplos con árboles distintos y mide el tiempo que tardan con time.time()
class Nodo:
    def __init__(self, value):
        self.valor = value
        self.left = None
        self.right = None

def print_three(nodo, level=0):
    if nodo is not None:
        print_three(nodo.right, level + 1)
        print(' ' * 8 * level + '-'  *4 + '>' + str(nodo.valor))
        print_three(nodo.left, level + 1) 


def recorrido_inorden(nodo):
    if nodo:
        recorrido_inorden(nodo.left)
        print(nodo.valor)
        recorrido_inorden(nodo.right)

def recorrido_preorden(nodo):
    if nodo:
        print(nodo.valor)
        recorrido_preorden(nodo.left)
        recorrido_preorden(nodo.right)

def recorrido_postorden(nodo):
    if nodo:
        recorrido_postorden(nodo.left)
        recorrido_postorden(nodo.right)
        print(nodo.valor)

#creacion de mi arbolito
raiz = Nodo(1)
raiz.left = Nodo(2)
raiz.right = Nodo(3)
raiz.left.left = Nodo(4)
raiz.left.right = Nodo(5)
raiz.right.left = Nodo(6)
raiz.right.right = Nodo(7)
raiz.left.left.left = Nodo(8)
raiz.left.left.right = Nodo(9)
raiz.left.right.left = Nodo(10)
raiz.left.right.right = Nodo(11)
raiz.right.left.left = Nodo(12)
raiz.right.left.right = Nodo(13)
raiz.right.right.left = Nodo(14)
raiz.right.right.right = Nodo(15)

print("Preorder:")
recorrido_preorden(raiz)

print("Postorder:")
recorrido_postorden(raiz)

print("Inorder:")
recorrido_inorden(raiz)

print("Arbol Visual:")
print_three(raiz)