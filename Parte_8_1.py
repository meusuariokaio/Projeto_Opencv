'''9. Salvar Imagens Processadas: Salvar imagens processadas com cv2.imwrite().
• Análise de Imagens: Análise de Forma, Análise de Textura (Local Binary Patterns). '''
'''10. Teste e Validação: Testar cada funcionalidade com diferentes tipos de imagens.'''

#são muitas variáveis e calculos, por favor aguarde ao executar
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage.exposure import histogram

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def local_bi_paterns(caminho):
    # Função para exibir imagens
    def exibe_imagem(imagem, titulo=''):
        plt.imshow(imagem, cmap='gray')
        plt.title(titulo)
        plt.axis('off')
        plt.show()

    # Função para calcular LBP
    def calculate_lbp(imagem, radius=1, neighbors=8):
        lbp_imagem = np.zeros_like(imagem, dtype=np.uint8)
        for i in range(radius, imagem.shape[0] - radius):
            for j in range(radius, imagem.shape[1] - radius):
                centro = imagem[i, j]
                binary_string = ''
                for n in range(neighbors):
                    theta = 2.0 * np.pi * n / neighbors
                    x = int(i + radius * np.cos(theta))
                    y = int(j - radius * np.sin(theta))
                    binary_string += '1' if imagem[x, y] > centro else '0'
                lbp_imagem[i, j] = int(binary_string, 2)
        return lbp_imagem

    # Carregar a imagem em escala de cinza
    imagem = cv.imread(caminho, cv.IMREAD_GRAYSCALE)

    # Aplicar LBP
    lbp_imagem = calculate_lbp(imagem)

    # Exibir a imagem original e a imagem com LBP
    exibe_imagem(imagem, 'Imagem Original')
    exibe_imagem(lbp_imagem, 'Imagem com LBP')

    # Histograma dos padrões LBP
    hist, _ = np.histogram(lbp_imagem, bins=np.arange(257), range=(0, 256))
    hist = hist.astype("float")
    hist /= hist.sum()

    # Exibir o histograma
    plt.bar(np.arange(len(hist)), hist, width=0.8, color='gray')
    plt.title('Histograma de LBP')
    plt.show()

    return imagem, lbp_imagem

def salvar_img(caminho):
    #as duas variaveis respectivamente serão armazenadas
    img_cinza, lbp_imagem = local_bi_paterns(caminho)

    #armazena ambas
    cv.imwrite("imagems_salvas/imagem_original3.jpg", img_cinza)
    cv.imwrite("imagems_salvas/imagem_lbp3.jpg", lbp_imagem)

    #verifica se foram armazenadas
    if cv.imwrite('imagems_salvas/imagem_original3.jpg', img_cinza) and cv.imwrite('imagems_salvas/imagem_lbp3.jpg', lbp_imagem):
        print('A imagem foi salva')
    else:
        print('A imagem não foi salva')

#chamar a função para salvar as imagens
#salvar_img("archive/histograma.jpg")
#salvar_img("archive/histograma2.jpg")
salvar_img("archive/histograma3.jpg")
#salvar_img("archive/histograma4.jpg")
