import json

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
ciudad = input("Introduce tu ciudad: ")

datos = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad,
    "ciudad": ciudad
}
with open("nombre.json", "w") as archivo:
    json.dump(datos, archivo)