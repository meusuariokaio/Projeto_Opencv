'''8. Segmentação e Análise de Imagens: Implementar técnicas como Watershed.
• Segmentação de Imagens: Limiarização, Watershed Algorithm.'''

#watershed
#limiarização com cv.threshold()
import cv2 as cv
import numpy as np

def watershed(caminho_img):
    #Recebendo a imagem
    img = cv.imread(caminho_img)
    #Transformando o rgb em cinza
    cinza = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    #Binarizando a imagem
    prim, seg = cv.threshold(cinza,0,225,cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    #cria uma matriz de ums de tamanho 3x3 com tipo de dado uint8
    matriz = np.ones((3,3), np.uint8)
    #remoção de ruídos da imagem
    abertura = cv.morphologyEx(seg,cv.MORPH_OPEN, matriz,iterations=2)
    forma_x = cv.dilate(abertura,matriz,iterations=3)
    #imagem, tamanho da mascara,
    transf = cv.distanceTransform(abertura, cv.DIST_L2,5)
    #imagem,limite máximo
    prim, forma_y = cv.threshold(transf,0.7*transf.max(),255,0)
    #Encontrar regiões desconhecidas e definindo o tipo do dado
    forma_y = np.uint8(forma_y)
    #subtração de imagems(a imagem do eixo x e a do eixo y)
    subtração = cv.subtract(forma_x,forma_y)
    #Marcar os componentes conectados
    prim, marcas = cv.connectedComponents(forma_y)
    marcas = marcas + 1
    marcas[subtração == 225] = 0
    #Aplica-se o algoritmo watershed
    marcas = cv.watershed(img,marcas)
    img[marcas == -1] = [255,0,0]

    cv.imshow("Imagem transformada: ", img)
#    cv.imshow("Cinza: ", cinza)

    cv.imwrite("imagems_salvas/Parte_7_1.jpg", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

#watershed("archive/histograma.jpg")
#watershed("archive/histograma2.jpg")
#watershed("archive/histograma3.jpg")
#watershed("archive/histograma4.jpg")
#watershed("archive/minions.jpg")
watershed("archive/ela_modified.jpg")
