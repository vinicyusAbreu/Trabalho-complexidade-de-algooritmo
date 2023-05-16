def algoritmo_ordenacao(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


lista = [5, 3, 2, 4, 7, 1, 0, 6]

print(algoritmo_ordenacao(lista))
