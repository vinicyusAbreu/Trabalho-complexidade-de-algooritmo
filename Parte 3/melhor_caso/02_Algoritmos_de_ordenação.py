def contadoring_sort(lista):
    valor_maximo = max(lista)
    contador = [0] * (valor_maximo + 1)
    ordernar_lista = [0] * len(lista)

    for num in lista:
        contador[num] += 1

    for i in range(1, valor_maximo + 1):
        contador[i] += contador[i - 1]

    for num in reversed(lista):
        ordernar_lista[contador[num] - 1] = num
        contador[num] -= 1

    return ordernar_lista


lista = [10, 5, 2, 3, 7, 8]
ordernar_lista = contadoring_sort(lista)
print(ordernar_lista)
