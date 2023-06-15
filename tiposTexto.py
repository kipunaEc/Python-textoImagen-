import cv2

#Leer imagen
img = cv2.imread('Quito.jpg')

#Tipos de letra - Fuentes de texto
font0 = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_PLAIN
font2 = cv2.FONT_HERSHEY_DUPLEX
font3 = cv2.FONT_HERSHEY_COMPLEX
font4 = cv2.FONT_HERSHEY_TRIPLEX
font5 = cv2.FONT_HERSHEY_COMPLEX_SMALL
font6 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
font7 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
font8 = cv2.FONT_ITALIC

tipoLetra = [font0,font1,font2,font3,font4,font5,font6,font7,font8]
texto = "Quito"
tamañoLetra = 3
grosorLetra = 2

#Bucle for, escribir 9 veces Quito
for i in range(9):   
    #Color de letra BGR, cambia conforme cambia i
    colorLetra = (221-20*i, 256-15*i, 10+50*i)
        
    #La ubicación mantiene en 50 el eje X (ancho)
    # y cambia en multiplos de 70 el eje Y (alto)
    ubicacion = (50,80+70*i)

    #Escribe el texto en la imagen
    cv2.putText(img, texto, ubicacion, tipoLetra[i], tamañoLetra, colorLetra, grosorLetra, cv2.LINE_AA)

#Guardar imagen
cv2.imwrite('Quito0.jpg', img)

#Mostrar imagen
cv2.imshow('Quito',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
