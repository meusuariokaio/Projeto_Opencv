'''7. Operações Morfológicas: Usar erosão e dilatação.
 Operações Morfológicas: Erosão, Dilatação, Segmentação de Objetos.'''

#erosão
import cv2 as cv
import numpy as np

def erodilat(caminho_img):

    img = cv.imread(caminho_img)

    matriz = np.ones((5,5), np.uint8)

    img_erodida = cv.erode(img,matriz,iterations=1)
    img_dilatada = cv.dilate(img, matriz, iterations=1)


    cv.imshow("Imagem original: ",img)
    cv.imshow("Imagem erodida: ",img_erodida)
    cv.imshow("Imagem dilatada: ",img_dilatada)
    cv.imwrite("imagems_salvas/Parte_6_1.jpg", img_erodida)
    cv.imwrite("imagems_salvas/Parte_6_2.jpg", img_dilatada)
    cv.waitKey(0)
    cv.destroyAllWindows()


erodilat("archive/histograma.jpg")
#erodilat("archive/histograma2.jpg")
#erodilat("archive/histograma3.jpg")
#erodilat("archive/histograma4.jpg")