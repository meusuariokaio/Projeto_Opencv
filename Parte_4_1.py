'''5. Detecção de Características: Usar detectores de cantos e contornos.'''
'''• Detecção de Características: Detecção de Cantos (Harris, Shi-Tomasi), 
Detecção de Contornos, Pontos de Interesse (SIFT/SURF). '''
#O médoto Harris faz quase as mesma coisa do método Canny
#Diferença: detecta cantos internos da imagem
#Bordas são tratadas como grandes gradientes de imagems,
#logo quando aplica-se os métodos do Harris os cantos são mensurados
import cv2 as cv
import numpy as np

def detect_crttc(caminho_img):#função que recebe parametro do caminho da imagem
    #armazena a imagem em uma variável
    img = cv.imread(caminho_img)
    #transforma a imagem em tons de cinza
    img_cinza = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    #variável recebe uma função que modifica o tipo do dado
    operação = np.float32(img_cinza)
    #aplica o  cv.cornerHarris método para detectar o canto
    operado = cv.cornerHarris(operação,blockSize=2,ksize=5,k=0.07)
    #blockSize é o tamanho da vizinhança
    #ksize é o tamanho da abertura do operador
    #Os resultados serão marcados através dos cantos dilatados
    img_alt = cv.dilate(operado,kernel=None)
    #Reverte para imagem original com valor de limite "ideal"
    #Semenhante ao Canny
    img[img_alt > 0.01 * img_alt.max()] = [0, 0, 255]
    #cv.imshow("Imagem com bordas detectadas: ",img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    lista = [img]
    for x, y in enumerate(lista):
        cv.imwrite("imagems_salvas/risosa" + str(x) + ".jpg", y)

#detect_crttc("archive/histograma.jpg")
#detect_crttc("archive/histograma2.jpg")
#detect_crttc("archive/histograma3.jpg")
detect_crttc("archive/histograma4.jpg")