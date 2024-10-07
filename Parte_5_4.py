#Subtração
import cv2 as cv


def subtração(caminhoimg1,caminhoimg2):

    img = cv.imread(caminhoimg1)
    img2 = cv.imread(caminhoimg2)
    #subtrai elementos de uma imagem na outra
    subtraido = cv.subtract(img,img2)


    cv.imshow("Imagem 1: ",img)
    cv.imshow("Imagem 2: ",img2)
    cv.imshow("Subtração de imagems",subtraido)
    cv.imwrite("imagems_salvas/Parte_5_4.jpg",subtraido)
    cv.waitKey(0)
    cv.destroyAllWindows()

subtração("archive/data/lena_tmpl.jpg","archive/data/lena.jpg")
#subtração("archive/data/aloeGT.png","archive/data/aloeL.jpg")
#subtração("archive/data/mask.png","archive/data/tmpl.png")
