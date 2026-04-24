with open("nombre.txt", "w") as archivo:
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    edad = int(input("Introduce tu edad: "))
    ciudad = input("Introduce tu ciudad: ")
    
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Apellido: {apellido}\n")
    archivo.write(f"Edad: {edad}\n")
    archivo.write(f"Ciudad: {ciudad}\n")
