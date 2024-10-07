import cv2 as cv
import numpy as np
#Parte 2_3
#Equalização de histograma
'''A equalização do histograma faz isso espalhando efetivamente os valores de intensidade mais frequentes.
O método é útil em imagens com planos de fundo e primeiro plano claros ou escuros. '''

#Para essa parte utilizei imagem adequadas para esse tipo de tratamento
img = cv.imread("archive/histograma.jpg")
img2 = cv.imread("archive/histograma2.jpg")
img3 = cv.imread("archive/histograma3.jpg")
img4 = cv.imread("archive/histograma4.jpg")

#Tem que transformar todas para cinza:

imagem = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
imagem2 = cv.cvtColor(img2,cv.COLOR_RGB2GRAY)
imagem3 = cv.cvtColor(img3,cv.COLOR_RGB2GRAY)
imagem4 = cv.cvtColor(img4,cv.COLOR_RGB2GRAY)

#cria um histograma de equalização de imagem utilizando o método cv.equalizeHist()
img_eqlz = cv.resize(cv.equalizeHist(imagem),(300,300))#equalizada e redimensionada para caber na exibição
img_eqlz2 = cv.resize(cv.equalizeHist(imagem2),(300,300))#equalizada e redimensionada
img_eqlz3 = cv.resize(cv.equalizeHist(imagem3),(300,300))#equalizada e redimensionada
img_eqlz4 = cv.resize(cv.equalizeHist(imagem4),(300,300))#equalizada e redimensionada

img_ants = cv.resize(imagem,(300,300))#imagem original redimensionada
img_ants2 = cv.resize(imagem2,(300,300))#imagem original redimensionada
img_ants3 = cv.resize(imagem3,(300,300))#imagem original redimensionada
img_ants4 = cv.resize(imagem4,(300,300))#imagem original redimensionada

#Função numpy que comcatena imagem no retorno(elas não podem ser grandes)
nao_eqlz = np.hstack((img_ants,img_ants2,img_ants3,img_ants4))
equalizada = np.hstack((img_eqlz,img_eqlz2,img_eqlz3,img_eqlz4))

cv.imshow("Imagem original: ", imagem)
cv.imshow("Imagems originais :", nao_eqlz)
cv.imshow("Imagems alteradas:",equalizada)
lista = [imagem,imagem2,imagem3,imagem4, nao_eqlz,equalizada]


cv.waitKey(0)
cv.destroyAllWindows()

def salvar(porta):
    for x, y in enumerate(lista):
        cv.imwrite("imagems_salvas/imagem" + str(x) + ".jpg", y)

salvar(True)