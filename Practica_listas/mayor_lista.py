lista=[3,5,7,1,10,9,1000]
#en  estructura de datos y algoritmos
#el mayor o mayor (ignorando los indices del inico ya reservados)y se saca de la lista
indice_actual = 0
menor = 0
for indice, elemento in lista: #FALTA UNA COSA (AVERIGUA QUE)
    if indice >= indice_actual:
        pass
    else:
        if elemento < menor:
            menor = elemento
        indice_actual+=1
lista[0] = menor #FALTA UNA COSA (AVERIGUA QUE)
print(lista)

#se anade el menor a la lista en la primera posicion