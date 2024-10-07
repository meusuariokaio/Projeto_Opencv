#SIFT (Scale-Invariant Feature Transform)
#bilblitecas
import cv2 as cv

def variante_escala(caminhoimg):
    imagem = cv.imread(caminhoimg)
    imagem_cinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)

    # Inicializar o detector SIFT
    #tem de "forçar" esse comando diretamente
    #criando um método contrutor com parantro imagem_cinza da classe
    #SIFT_create no __init__.pyi
    imagemsift = cv.SIFT_create()

    #detectar pontos de interesse e calcula
    keypoints, descritores = imagemsift.detectAndCompute(imagem_cinza, None)

    #coloca os pontos de interesse na imagem
    imagemdetectada = cv.drawKeypoints(imagem, keypoints, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Mostrar a imagem
    #cv.imshow("Original", imagem)
    #cv.imshow("Imagem transformada: ", imagemdetectada)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    lista = [imagemdetectada]
    for x, y in enumerate(lista):
        cv.imwrite("imagems_salvas/dados3" + str(x) + ".jpg", y)
#variante_escala('archive/histograma.jpg')
#variante_escala('archive/histograma2.jpg')
#variante_escala('archive/histograma3.jpg')
variante_escala('archive/histograma4.jpg')
