import cv2


def deteccao_image(image):
    cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = cv2.Canny(cinza, 100, 200)
    return detector


tamanho_imagem = [100, 200, 500, 1000]


for tamanho in tamanho_imagem:
    print(f"Image tamanho: {tamanho}x{tamanho} ")
