import heapq
from collections import defaultdict


def criar_tabela_frequencia(data):
    tabela_frequencia = defaultdict(int)
    for simbolo in data:
        tabela_frequencia[simbolo] += 1
    return tabela_frequencia


class No:
    def __init__(self, simbolo, frequencia):
        self.simbolo = simbolo
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia


def construir_arvore_huffman(tabela_frequencia):
    fila_prioridade = []
    for simbolo, frequencia in tabela_frequencia.items():
        no = No(simbolo, frequencia)
        heapq.heappush(fila_prioridade, no)

    while len(fila_prioridade) > 1:
        no_esquerda = heapq.heappop(fila_prioridade)
        no_direita = heapq.heappop(fila_prioridade)
        no_pai = No(None, no_esquerda.frequencia + no_direita.frequencia)
        no_pai.esquerda = no_esquerda
        no_pai.direita = no_direita
        heapq.heappush(fila_prioridade, no_pai)

    return fila_prioridade[0]


def construir_tabela_codigos(root):
    tabela_codigos = {}

    def percorrer_arvore(no, codigo):
        if no.simbolo is not None:
            tabela_codigos[no.simbolo] = codigo
            return
        percorrer_arvore(no.esquerda, codigo + "0")
        percorrer_arvore(no.direita, codigo + "1")
    percorrer_arvore(root, "")
    return tabela_codigos


def comprimir_huffman(data):
    tabela_frequencia = criar_tabela_frequencia(data)
    arvore_huffman = construir_arvore_huffman(tabela_frequencia)
    tabela_codigos = construir_tabela_codigos(arvore_huffman)
    dados_codificados = "".join(tabela_codigos[simbolo] for simbolo in data)
    return dados_codificados, tabela_codigos


def descomprimir_huffman(dados_codificados, tabela_codigos):
    tabela_codigos_invertida = {
        codigo: simbolo for simbolo, codigo in tabela_codigos.items()
        }
    codigo_atual = ""
    dados_decodificados = []
    for bit in dados_codificados:
        codigo_atual += bit
        if codigo_atual in tabela_codigos_invertida:
            simbolo = tabela_codigos_invertida[codigo_atual]
            dados_decodificados.append(simbolo)
            codigo_atual = ""
    return dados_decodificados


dados = "Olá, Mundo!"
dados_codificados, tabela_codigos = comprimir_huffman(dados)
print("Dados codificados:", dados_codificados)
dados_decodificados = descomprimir_huffman(dados_codificados, tabela_codigos)
print("Dados decodificados:", "".join(dados_decodificados))
