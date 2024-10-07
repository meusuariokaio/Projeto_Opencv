#Shi-Tomasi para detecção de cantos
#bibliotecas necessárias
import cv2 as cv
import numpy as np


def detect_canto(caminho):
    img = cv.imread(caminho)

    #transforma a imagem em cinza
    img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #função de detecção de cantos Shi-Tomasi
    #detecta apenas os 100 melhores corners
    #você pode alterar o número para o resultado que deseja
    cantos = cv.goodFeaturesToTrack(img_cinza, 100, 0.01, 10)

    # converte os valores dos cantos para inteiros
    cantoint = np.int_(cantos)

    # os cantos são marcados com bolas azuis(rgb(blue,green,red))
    # pinta de azul os cantos das bordas
    for i in cantoint:
        x, y = i.ravel()
        cv.circle(img, (x, y), 3, (0, 0, 255), -1)#função para criar bola circular

    #resultado
    #cv.imshow("Imagem com bordas",img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    lista = [img]
    for x, y in enumerate(lista):
        cv.imwrite("imagems_salvas/abcde" + str(x) + ".jpg", y)

#detect_canto("archive/data/tabuleiro.jpg")
#detect_canto("archive/histograma.jpg")
#detect_canto("archive/histograma2.jpg")
#detect_canto("archive/histograma3.jpg")
detect_canto("archive/histograma4.jpg")