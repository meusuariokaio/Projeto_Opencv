#1. Configuração do Ambiente: Instalar Python e a biblioteca OpenCV.
'''As imagems adequadas para o tratamentos foram criadas por uma IA de modo que
o tratamento pelos métodos opencv sejam aproveitadas ao máximo'''
import cv2 as cv
#2. Leitura e Exibição de Imagens: Criar um script para carregar e exibir imagens.

'''• Leitura e Exibição de Imagens: Carregar imagens de diferentes formatos 
(JPEG, PNG, BMP) usando cv2.imread(). Exibir as imagens carregadas utilizando cv2.imshow(). '''

imgjpg = cv.imread("archive/data/garota.jpg")
imgbmp = cv.imread("archive/data/garota.bmp")
imgif = cv.imread("archive/data/garota.gif")
imgjpeg = cv.imread("archive/data/garota.jpeg")
imgpng = cv.imread("archive/data/garota.png")
cv.imshow("Formato .JPG: ",imgjpg)
cv.imshow("Formato .BMP: ", imgbmp)
cv.imshow("Formato .GIF: ",imgif)
cv.imshow("Formato .JPEG", imgjpeg)
cv.imshow("Formato .PNG: ", imgpng)
cv.waitKey(10000)#10segundos antes de fechar
cv.destroyAllWindows()

def salvar(porta):
    if (porta):
        #imgjpg = cv.imread("archive/data/garota.jpg")
        cv.imwrite("imagems_salvas/garota.jpg",imgjpg)
        #imgbmp = cv.imread("archive/data/garota.bmp")
        cv.imwrite("imagems_salvas/garota.bmp", imgbmp)
        #imgif = cv.imread("archive/data/garota.gif")
    if porta:
        cv.imwrite("imagems_salvas/garota.gif", imgif)
        #imgjpeg = cv.imread("archive/data/garota.jpeg")
        cv.imwrite("imagems_salvas/garota.jpeg", imgjpeg)
        #imgpng = cv.imread("archive/data/garota.png")
        cv.imwrite("imagems_salvas/garota.png", imgpng)

salvar(True)