def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivô = list[0]
        menor = [i for i in list[1:] if i <= pivô]
        maior = [i for i in list[1:] if i > pivô]
        return quick_sort(menor) + [pivô] + quick_sort(maior)


"""lista = list(range(1001, -1, -1))  RecursionError: profundidade máxima de
recursão excedida na comparação
"""
lista = list(range(101, -1, -1))
print(quick_sort(lista))
