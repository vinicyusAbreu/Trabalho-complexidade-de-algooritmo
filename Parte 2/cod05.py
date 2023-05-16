class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.valor)


def insere(raiz, valor):
    if raiz is None:
        raiz = No(valor)
    elif valor < raiz.valor:
        raiz.esquerda = insere(raiz.esquerda, valor)
    else:
        raiz.direita = insere(raiz.direita, valor)
    return raiz


def busca(raiz):
    if raiz is not None:
        busca(raiz.esquerda)
        print(raiz.valor, end=" ")
        busca(raiz.direita)


raiz = None

"""lista = list(range(1001, -1, -1))  RecursionError: profundidade máxima de
recursão excedida na comparação
"""
lista = list(range(101, -1, -1))

for elemento in lista:
    raiz = insere(raiz, elemento)


busca(raiz)
