import numpy as np
import cv2

caminho_aquivo = "D:\\Documentos\\trab-p2\\Parte 3\\melhor_caso\\cinza_image.jpg"


def escala_de_cinza_para_sepia(image):
    altura, largura = image.shape[:2]
    sepia_image = np.zeros((altura, largura, 3), dtype=np.uint8)

    for y in range(altura):
        for x in range(largura):
            cinza = image[y, x]
            sepia = (cinza * 0.393) + (cinza * 0.769) + (cinza * 0.189)
            sepia = min(sepia, 255)
            sepia_image[y, x] = (sepia, sepia * 0.349, sepia * 0.272)

    return sepia_image


cinza_image = cv2.imread(caminho_aquivo, cv2.IMREAD_GRAYSCALE)


sepia_image = escala_de_cinza_para_sepia(cinza_image)


cv2.imwrite(caminho_aquivo, sepia_image)
