'''usando sobel na imagem'''
import cv2 as cv
import numpy as np

'''Detecta bordas com um derivação para cada pixel, que aponta para uma direção, bem 
com uma taxa de direção, as simulações de imagem geradas pelo sobel detectam a mudança
de direção para o eixo x e y.'''


def detect_bords(img_caminho):#função recebe parametro do caminho da imagem
    img = cv.imread(img_caminho)#imagem lida pelo cv2
    # transforma para cinza para poder ser manipulada
    img_cinza = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    #Sobel para direção x (dx) de tamanho 3 para matriz
    sobelx = cv.Sobel(img_cinza,cv.CV_64F,1,0,ksize=3)
    #sobel para direção y (dy) de tamanho 3 para matriz
    sobely = cv.Sobel(img_cinza,cv.CV_64F,0,1,ksize=3)
    #função de raiz quadrada sobre os eixos x e y sobel que geram a "média" da matriz
    magnitude = np.sqrt(sobelx**2 + sobely**2)
    #formula aplicada sobe a tonalidade da matriz resultante
    magnitudenew = np.uint8(255 * magnitude / np.max(magnitude))

    cv.imshow("Original",img_cinza)
    cv.imshow("Sobel X", sobelx)
    cv.imshow("Sobel Y", sobely)
    #Magnitude detecta um conjuto "x,y" do sobel
    cv.imshow("Magnitude", magnitudenew)
    cv.waitKey(0)
    cv.destroyAllWindows()
    lista = [sobelx,sobely]
    for x, y in enumerate(lista):
        cv.imwrite("imagems_salvas/outs" + str(x) + ".jpg", y)


#detect_bords("archive/histograma.jpg")
#detect_bords("archive/histograma2.jpg")
#detect_bords("archive/histograma3.jpg")
detect_bords("archive/histograma4.jpg")
