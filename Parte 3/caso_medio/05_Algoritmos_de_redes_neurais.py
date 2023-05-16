import tensorflow as tf
import time


def criar_rede_neural(tamanho_entrada, camadas_ocultas, tamanho_saida):
    modelo = tf.keras.models.Sequential()
    modelo.add(tf.keras.layers.Dense(camadas_ocultas[0], activation='relu',
                                     input_shape=(tamanho_entrada,)))

    for i in range(1, len(camadas_ocultas)):
        modelo.add(tf.keras.layers.Dense(camadas_ocultas[i],
                                         activation='relu'))

    modelo.add(tf.keras.layers.Dense(tamanho_saida, activation='softmax'))
    return modelo


def medir_tempo_execucao(tamanho_entrada, camadas_ocultas, tamanho_saida):
    modelo = criar_rede_neural(tamanho_entrada, camadas_ocultas, tamanho_saida)
    modelo.compile(optimizer='adam', loss='categorical_crossentropy',
                   metrics=['accuracy'])

    dados_entrada = tf.random.uniform((1, tamanho_entrada))

    rótulos = tf.random.uniform((1, tamanho_saida))

    tempo_inicial = time.time()
    modelo.fit(dados_entrada, rótulos, epochs=1, verbose=0)
    tempo_final = time.time()

    tempo_execucao = tempo_final - tempo_inicial
    return tempo_execucao


tamanhos_entrada = [100, 200, 500, 1000]
tamanhos_camadas_ocultas = [[50, 50], [100, 100], [200, 200, 200],
                            [500, 500, 500, 500]]
tamanho_saida = 10

"""Avaliar a complexidade de caso médio
para diferentes tamanhos de entrada e camadas ocultas"""
for i, tamanho_entrada in enumerate(tamanhos_entrada):
    camadas_ocultas = tamanhos_camadas_ocultas[i]

    tempo_execucao = medir_tempo_execucao(tamanho_entrada, camadas_ocultas,
                                          tamanho_saida)
    print(f"Tamanho de entrada: {tamanho_entrada} "
          f"| Camadas ocultas: {camadas_ocultas} "
          f"| Tempo de execução: {tempo_execucao} segundos")
