'''3. Implementação de Pré-processamento de Imagens:
Adicionar a funcionalidade de converter e redimensionar imagens.'''
import cv2 as cv


'''• Pré-processamento de Imagens: 
Conversão de Cores, Redimensionamento, Equalização de Histograma. '''

imgjpg = cv.imread("archive/data/garota.jpg")

sol = cv.cvtColor(imgjpg,cv.COLOR_BGR2YCrCb)#converte imagem para uma paleta de cores
outra = cv.cvtColor(imgjpg,cv.COLOR_RGBA2GRAY)#cinza
cor2 = cv.cvtColor(imgjpg,cv.COLOR_BGR2HSV)#avermelhado
cor3 = cv.cvtColor(imgjpg,cv.COLOR_BGRA2YUV_I420)#acinzentado e 4 partes
cor4 = cv.cvtColor(imgjpg,cv.COLOR_RGB2HLS_FULL)#azulado
cor5 = cv.cvtColor(imgjpg,cv.COLOR_BGR2Lab)#amarelado
lista = [sol,outra,cor2,cor3,cor4,cor5]
#Converter cores

cv.imshow("Cor Amarelado: ",sol)
cv.imshow("Cor Cinza: ",outra)
cv.imshow("Cor 2: ",cor2)
cv.imshow("Cor 3: ",cor3)
cv.imshow("Cor 4: ",cor4)
cv.imshow("Cor 5: ", cor5)

cv.waitKey(0)#Milisegundos
cv.destroyAllWindows()

def salvar(porta):
    for x,y in enumerate(lista):
            cv.imwrite("imagems_salvas/img"+str(x)+".jpg",y)

salvar(True)