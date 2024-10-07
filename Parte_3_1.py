import cv2 as cv
#4. Aplicação de Filtros: Implementar filtros como GaussianBlur, Canny, Sobel.
'''• Aplicação de Filtros: Desfoque (Blur), Detecção de Bordas (Canny, Sobel), Filtro Laplaciano. '''

imagem = cv.imread("archive/data/Lena.png")

img_cinza = cv.cvtColor(imagem,cv.COLOR_RGB2GRAY)
#Etapa 1: Redução de ruído e suavização de bordas -->filtro gaussiano
#tamanho do kernel gaussiano,matriz de tamanho 3x5 que será usada para calcular o desfoque.
kernel = (3,5)
#desvio padão de desfoque de imagem para X
desvio = 0.5#altere drásticamente esse valor e veja a imagem quase sem elementos capturados
#geralmente sigmaY assume o valor de X quando não especificada
#Passo 2: Encontrando o gradiente de intensidade --> Gx(horizontal) e Gy(vertical)
# --> algoritmos de Sobel
img_gauss = cv.GaussianBlur(src=img_cinza, ksize=kernel,sigmaX=desvio)

#Etapa 3: Supressão não máxima para --> obter bordas finas -->para ver se há um máximo local
# -->. Se não for, o pixel será suprimido
#Etapa 4: limiar de histerese --> Definimos os valores de limite minVal e maxVal para pixels
#limite minVal
limite_min = 70#abaixo desse valor o pixel é descartado
limite_max = 135#acima desse o pixel é mantido
result_final = cv.Canny(img_gauss, limite_min, limite_max)
#altere os limites drásticamente e veja a diferença nas bordas e nos detalhes capturados
lista = [result_final]

cv.imshow("Imagem original: ",imagem)
cv.imshow("Imagem manipulada: ",result_final)
cv.waitKey(0)
cv.destroyAllWindows()

def salvar(porta):
    for x, y in enumerate(lista):
        cv.imwrite("imagems_salvas/img1" + str(x) + ".jpg", y)

salvar(True)
