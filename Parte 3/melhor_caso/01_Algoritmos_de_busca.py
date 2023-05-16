def busca_binaria(arr, alvo):
    baixo = 0
    alto = len(arr) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2

        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1

    return -1


vetor = [1, 3, 5, 7, 9, 11, 13, 15]
elemento_procurado = 1


indice = busca_binaria(vetor, elemento_procurado)


if indice != -1:
    print(f"Elemento {elemento_procurado} encontrado na posição {indice}!")
else:
    print(f"Elemento {elemento_procurado} não encontrado.")
