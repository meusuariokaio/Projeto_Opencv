#Usando SURF
import cv2
import cv2 as cv

#imagem
imagem = cv.imread('archive/histograma.jpg')
imagem_cinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)

#detector SURF
surf = cv2.xfeatures2d.SURF_create(400)#O SURF_create() não existe no opencv

#pontos de interesse e calcular
keypoints, descritores = surf.detectAndCompute(imagem_cinza, None)

#define os pontos de interesse na imagem
imagem_com_keypoints = cv.drawKeypoints(imagem, keypoints, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#exibe
cv.imshow("Imagem transformada: ", imagem)

cv.imwrite("imagems_salvas/parte_4_5.jpg",imagem)
cv.waitKey(0)
cv.destroyAllWindows()