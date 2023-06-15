#Importar librería cv2
import cv2

#Leer imagen
img = cv2.imread('Quito1.jpg')

#Características del texto
texto = "Quito"
ubicacion = (50,300)
font = cv2.FONT_HERSHEY_TRIPLEX
tamañoLetra = 10
colorLetra = (221,82,196)
grosorLetra = 10

#Escribir texto
cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)

#Guardar imagen
cv2.imwrite('textoQuito.jpg', img)

#Mostrar imagen
cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
