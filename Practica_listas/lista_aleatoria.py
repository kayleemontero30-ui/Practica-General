#usa como referencia para permutaciones y el cubo de rubix
#forma 1 en estructuras de datos y algoritmos
lista =[8, 5 ,9, 15]#esto debe ser variable

indice_actual=0
lista_indices=[]
lista_resultados=[]
#creamos las dos variables
for elemento in lista:
    lista_indices.append(indice_actual)
    lista_resultados.append(0)
    indice_actual+=1
    print(lista_indices,lista_resultados)

for indice in lista_indices:
    mayor = 0
    for elemento in lista:
        if elemento >mayor and elemento not in lista_resultados:
            mayor = elemento

    lista_resultados[indice]= mayor 
    print
    