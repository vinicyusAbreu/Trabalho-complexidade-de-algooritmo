def busca_em_largura(grafo, inicio, objetivo):
    visitados = set()
    fila = [(inicio, [inicio])]

    while fila:
        no, caminho = fila.pop(0)
        if no == objetivo:
            return caminho

        visitados.add(no)
        vizinhos = grafo[no]
        for vizinho in vizinhos:
            if vizinho not in visitados:
                fila.append((vizinho, caminho + [vizinho]))

    return None


grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

no_inicio = 'A'
no_objetivo = 'D'

resultado = busca_em_largura(grafo, no_inicio, no_objetivo)
if resultado:
    print(f"Caminho encontrado: {' -> '.join(resultado)}")
else:
    print("Não foi possível encontrar um caminho até o nó objetivo.")
