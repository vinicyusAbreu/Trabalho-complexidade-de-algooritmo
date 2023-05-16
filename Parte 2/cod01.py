lista = list(range(100000001))


def busca_linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


target_element = 100000000

result = busca_linear(lista, target_element)
if result != -1:
    print(f"Elemento {target_element} encontrado no índice {result}.")
else:
    print(f"Elemento {target_element} não encontrado na lista.")
