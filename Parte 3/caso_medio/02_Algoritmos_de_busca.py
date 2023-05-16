def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
alvo = 23

indice = busca_binaria(lista_ordenada, alvo)
if indice != -1:
    print(f"O elemento {alvo} foi encontrado no índice {indice}.")
else:
    print(f"O elemento {alvo} não foi encontrado na lista.")
