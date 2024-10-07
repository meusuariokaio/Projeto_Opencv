import cv2 as cv
#Parte 2_2
#Redimensionamento de imagem


'''
cv2. INTER_AREA: Isso é usado quando precisamos reduzir uma imagem.
cv2. INTER_CUBIC: Isso é lento, mas mais eficiente.
cv2. INTER_LINEAR: Isso é usado principalmente quando o zoom é 
necessário. Esta é a técnica de interpolação padrão no OpenCV.
stretch_near = cv2.resize(image, (780, 540), 
               interpolation = cv2.INTER_LINEAR)
'''


imagem = cv.imread("archive/data/cara.jpg")
ncorpo = (200,200)
antes = (800,563)
img = cv.resize(imagem,ncorpo)
ims = cv.resize(imagem,antes)

lista = [img,ims]

cv.imshow(f"Tamanho anterior: {antes}",ims)
cv.imshow(f"Novo tamanho: {ncorpo}",img)

cv.waitKey(0)#Milisegundos
cv.destroyAllWindows()


def salvar(porta):
    for x, y in enumerate(lista):
        cv.imwrite("imagems_salvas/imag" + str(x) + ".jpg", y)

salvar(True)