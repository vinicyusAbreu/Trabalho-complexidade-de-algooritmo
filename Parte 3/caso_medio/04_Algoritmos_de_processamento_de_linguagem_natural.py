import spacy


def analise_sintatico(texto):
    nlp = spacy.load('en_core_news_sm')
    doc = nlp(texto)
    return doc


tamanho_texto = [100, 200, 500, 1000]

for tamanho in tamanho_texto:
    texto = " ".join(["hello"] * tamanho)

    doc = analise_sintatico(texto)

    print(f"Texto tamanho: {tamanho} palavras")

    print(doc)
