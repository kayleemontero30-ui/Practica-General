import requests
import json

def obtener_rick_and_morty(nombre):
    url = f"https://rickandmortyapi.com/api/character/72"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return False
    
nombre = input("Introduce el nombre del personaje de Rick and Morty: ")
datos = { nombre: obtener_rick_and_morty(nombre) }

with open("rick_and_morty.json", "w") as archivo:    
    json.dump(datos, archivo)