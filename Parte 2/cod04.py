def busca_binaria(arr, target):
    inicio = 0
    fim = len(arr) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr[meio] == target:
            return meio
        elif arr[meio] < target:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


lista = list(range(100000001))

target_element = 1000000001

result = busca_binaria(lista, target_element)

if result != -1:
    print(f"Elemento {target_element} encontrado no índice {result}.")
else:
    print(f"Elemento {target_element} não encontrado na lista.")
