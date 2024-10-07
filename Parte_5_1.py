'''• Transformações Geométricas: Rotação, Translação, Transformação de
Perspectiva (Homografia), Correção de Distorção. '''
from Parte_4_5 import imagem_cinza

'''6. Transformações Geométricas e Operações Aritméticas: Implementar 
rotacionamento, translação e operações como soma e subtração de imagens.'''

#Rotacionamento
import cv2 as cv
import numpy as np


def redimensionar(caminhoimg):
    # Carregar a imagem
    img = cv.imread(caminhoimg)

    # Converter a imagem para escala de cinza
    img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Fatores de redimensionamento
    fator1 = 3.0  # Aumentar o tamanho
    fator2 = 1 / 3.0  # Reduzir o tamanho

    # Redimensionar a imagem
    img_ampliada = cv.resize(img_cinza, None, fx=fator1, fy=fator1, interpolation=cv.INTER_LINEAR)
    img_reduzida = cv.resize(img_cinza, None, fx=fator2, fy=fator2, interpolation=cv.INTER_LINEAR)

    # Exibir as imagens redimensionadas
    cv.imshow("Imagem Ampliada", img_ampliada)
    cv.imshow("Imagem Reduzida", img_reduzida)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Salvar as imagens redimensionadas
    cv.imwrite("imagems_salvas/Parte_5_1_ampliada.jpg", img_ampliada)
    cv.imwrite("imagems_salvas/Parte_5_1_reduzida.jpg", img_reduzida)


# Chamar a função para redimensionar e salvar a imagem
redimensionar(caminhoimg="archive/histograma.jpg")
