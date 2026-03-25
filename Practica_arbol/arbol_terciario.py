#Implementar un árbol binario de búsqueda (BST) y realizar los tres recorridos en Python.
# Crear un árbol con al menos 6 nodos, usando clases y objetos.
# Implementar funciones para realizar preorden, inorden, y postorden.
# Ejecuta varios ejemplos con árboles distintos y mide el tiempo que tardan con time.time()

class Nodo:
    def __init__(self, value):
        self.valor = value
        self.left = None
        self.middle = None
        self.right = None
        

#def print_three(nodo, level=0):
 #   if nodo is not None:
  #      print_three(nodo.right, level + 1)
   #     print(' ' * 8 * level + '-'  *4 + '>' + str(nodo.valor))
    #    print_three(nodo.left, level + 1) 


def recorrido_inorder(nodo):
    if nodo:
        recorrido_inorder(nodo.left)
        print(nodo.valor)
        recorrido_inorder(nodo.middle)
        recorrido_inorder(nodo.right)

def recorrido_preorder(nodo):
    if nodo:
        print(nodo.valor)
        recorrido_preorder(nodo.left)
        recorrido_preorder(nodo.middle)
        recorrido_preorder(nodo.right)

def recorrido_postorder(nodo):
    if nodo:
        recorrido_postorder(nodo.left)
        recorrido_postorder(nodo.middle)
        recorrido_postorder(nodo.right)
        print(nodo.valor)


#creacion de mi arbolito
raiz = Nodo(1)
raiz.left = Nodo(2)
raiz.middle = Nodo(3)
raiz.right = Nodo(4)
raiz.left.left = Nodo(5)
raiz.left.middle = Nodo(6)
raiz.left.right = Nodo(7)
raiz.middle.left = Nodo(8)
raiz.middle.middle = Nodo(9)
raiz.middle.right = Nodo(10)
raiz.right.left = Nodo(11)
raiz.right.middle = Nodo(12)
raiz.right.right = Nodo(13)


print("Inorder:")
recorrido_inorder(raiz)

print("Preorder:")
recorrido_preorder(raiz)

print("Postorder:")
recorrido_postorder(raiz)