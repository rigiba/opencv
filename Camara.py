# este programa en python ejecutae el video y cuando detecta movimiento
# toma 10 capturas de pantalla y las guarda en archivos de imagen png


import cv2

camera = cv2.VideoCapture('aca pones la ruta del video o camara')
for i in range(10):
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
del(camera)
