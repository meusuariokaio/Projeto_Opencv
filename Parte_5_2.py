#translação
import cv2 as cv
import numpy as np

def transform(caminho_img):

    #variavel recebe image
    img = cv.imread(caminho_img)

    #altura e largura da imagem pelo tamanho da imagem
    altura,largura = img.shape[:2]

    #Pode-se alterar a distancia da altura e largura pelo almento do valor do divisor
    var_altura, var_largura = altura / 4, largura / 4

    #transforma o formato e define o plano cartesiano(x,y) da imagem para
    translação = np.float32([[1,0,var_largura],[0,1,var_altura]])

    #função cv.warpAffine() efetura a translação da imagem nos valores definidos
    img_translação = cv.warpAffine(img,translação,(largura,altura))

    cv.imshow("Imagem antes: ",img)
    cv.imshow("Imagem com translação: ",img_translação)
    cv.imwrite("imagems_salvas/Parte_5_2.jpg", img_translação)
    cv.waitKey(0)
    cv.destroyAllWindows()

#transform("archive/histograma.jpg")
#transform("archive/histograma2.jpg")
#transform("archive/histograma3.jpg")
#transform("archive/histograma4.jpg")