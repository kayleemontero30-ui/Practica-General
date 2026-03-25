


class Estanteria:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregadoa la parte superior:", libro)
        return libro

    def retirar_libro(self):
        if self.libros:
            libro = self.libros.pop()
            print("Libro retirado de la parte superior:", libro)
            return libro
        else:
            return "La estantería está vacía."
        
    def estado_pila(self):
        print("Estado actual de la estanteria:", self.libros)

pila = Estanteria()
pila.agregar_libro("Romeo y Julieta")
pila.estado_pila()
pila.agregar_libro("El Principito")
pila.estado_pila()
pila.agregar_libro("My Little Pony")
pila.estado_pila()
pila.retirar_libro()
pila.estado_pila()
pila.retirar_libro()
pila.estado_pila()

#pila = []
#pila.append("Romeo y Julieta")
#print (pila)
#pila.append("El Principito")
#print (pila)
#pila.append("My Little Pony")
#print (pila)
#pila.pop()
#print (pila)
#pila.pop()
#print (pila)