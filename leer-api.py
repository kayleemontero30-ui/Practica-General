import json

with open("nombre.json", "r") as archivo:
    datos = json.load(archivo)
    print(datos)