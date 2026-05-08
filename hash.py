

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def nombres_normalizados(self, nombre):
        return nombre.strip().lower()

    def hash_function(self, nombre):
        nombre = self.nombres_normalizados(nombre)
        suma = 0

        for letra in nombre:
            suma += ord(letra)

        posicion = suma % self.size
        return posicion

    def insert(self, nombre, dato):
        nombre = self.nombres_normalizados(nombre)
        posicion = self.hash_function(nombre)

        for elemento in self.table[posicion]:
            if elemento[0] == nombre:
                print("El nombre ya existe, actualizando dato.")
                print("Datos encontrados:", elemento[1], elemento[2])
                print("\nActualizar datos??? (s/n): ")
                respuesta = input().lower()
                if respuesta == "s":
                    self.table[posicion].remove(elemento)
                    self.table[posicion].append((nombre, dato))
                    print("Dato actualizado.")
                return

        self.table[posicion].append((nombre, dato))
        print("Dato insertado en la posicion", posicion)

    def search(self, nombre):
        nombre = self.nombres_normalizados(nombre)
        posicion = self.hash_function(nombre)

        for elemento in self.table[posicion]:
            if elemento[0] == nombre:
                return {
                    "nombre": elemento[0],
                    "dato": elemento[1]
                }

        return None

    def display(self):
        print("\n" + "=" * 85)
        print(f"{'POSICION':<10} | {'NOMBRE':<25} | {'EDAD':<10} | {'NOTA':<10}")
        print("=" * 85)

        for i, bucket in enumerate(self.table):
            if len(bucket) == 0:
                print(f"{i:<10} | {'[---]':<25} | {'-':<10} | {'-':<10}")
            else:
                for nombre, dato in bucket:
                    print(f"{i:<10} | {nombre:<25} | {str(dato['edad']):<10} | {str(dato['nota']):<10}")

        print("=" * 85)

tabla = HashTable(50)

tabla.insert("Juan Pablo Duarte", {"edad": 30, "nota": 85})
tabla.insert("Beyonce", {"edad": 25, "nota": 92})
tabla.insert("Bad Bunny", {"edad": 40, "nota": 25})
tabla.insert("Shakira", {"edad": 35, "nota": 78})
tabla.insert("Fausto", {"edad": 28, "nota": 90})


while True:
    print()
    print("MINI SISTEMA HASH")
    print("1. Insertar")
    print("2. Buscar")
    print("3. Mostrar tabla")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        nota = input("Nota: ")

        dato = {
            "edad": edad,
            "nota": nota
        }

        tabla.insert(nombre, dato)
        print("Dato insertado correctamente.")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        resultado = tabla.search(nombre)

        if resultado is not None:
            print("Persona Encontrada:")
            print(" Nombre:", resultado["nombre"])
            print(" Dato:", resultado["dato"])
        else:
            print("No encontrado.")

    elif opcion == "3":
        tabla.display()

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opcion no valida.")