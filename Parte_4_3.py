#biblioteca
import numpy as np
import cv2 as cv
#Detecção de Contornos
def detect_bordas(caminhoimg):
    #leitura da imagem
    img = cv.imread(caminhoimg)

    #comverte imagem para cinza
    cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #detecta cantos com a função cv.goodFeaturesToTrack()
    canto = cv.goodFeaturesToTrack(cinza, 27, 0.01, 10)
    novocanto = np.int_(canto)#o equivalente do np.int0() na função que transforma em inteiro é o np.int_()

    # we iterate through each corner,
    # making a circle at each point that we think is a corner.
    for i in novocanto:
        x, y = i.ravel()#coordenada do canto detectado do loop de cada novocanto detectado
        #cv.circle() cria um circulo nos cantos detectados
        # imagem,posição,radio do circulo,rgb.
        cv.circle(img, (x, y), 3, (0,0,255), -1)

    #cv.imshow("Imagem com bordas detectadas: ", img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    lista = [img]
    for x, y in enumerate(lista):
        cv.imwrite("imagems_salvas/forma3" + str(x) + ".jpg", y)

#detect_bordas(caminhoimg="archive/histograma.jpg")
#detect_bordas(caminhoimg="archive/histograma2.jpg")
#detect_bordas(caminhoimg="archive/histograma3.jpg")
detect_bordas(caminhoimg="archive/histograma4.jpg")
