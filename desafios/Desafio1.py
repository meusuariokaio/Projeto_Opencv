import cv2

#variável que armazena a imagem

imagem1 = 'download.jpg'

#variável que armazena o arquivo xml

cascade_path1 = 'cascade_facas.xml'

#cria o classificador

clf1 = cv2.CascadeClassifier(cascade_path1)

#lê a imagem

img1 = cv2.imread(imagem1)

#converte para cinza

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

#função da detecção

deteccoes1 = clf1.detectMultiScale(gray1, scaleFactor=1.01, minNeighbors=5, minSize=(1,1))

#desenha o retângulo com as coordenadas obtidas

for(x,y,w,h) in deteccoes1:
    img1 = cv2.rectangle(img1, (x,y), (x+w, y+h), (0,0,255), 2)
#para visualizar a imagem
cv2.imshow('Classificador 1', img1)
#mantém a janela aberta até que eu digite uma tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
