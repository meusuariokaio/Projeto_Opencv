#operações como soma e subtração de imagens

import cv2 as cv
import numpy as np

def soma_img(caminho_img1, caminho_img2):

    #recebe duas imagem que vão ser somadas
    img = cv.imread(caminho_img1)
    img2 = cv.imread(caminho_img2)

    #função cv que soma as imagems
    #parametros: 1ªimagem,peso na imagem resultante,2ªimagem, peso na imagem final
    #gamma não adição extra
    #as cores das imagems devem ser bastante vibrantes apra um contraste
    somando = cv.addWeighted(img,0.5,img2,0.4,0)

    cv.imshow("Imagem original 1: ", img)
    cv.imshow("Imagem original 2: ", img2)
    cv.imshow("Imagem resultante 3: ",somando)
    cv.imwrite("imagems_salvas/Parte_5_3.jpg", somando)
    cv.waitKey(0)
    cv.destroyAllWindows()

#soma_img("archive/histograma.jpg","archive/histograma2.jpg")
soma_img("archive/histograma3.jpg","archive/histograma4.jpg")
