#Instalación

Para realizar la instalacion es necesario tener algunas configuraciones previa en la consola linux

sudo apt-get install libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test

Si ya tienes python3 puedes proceder a instalar OpenCV

ingresa a python3 y ejecuta

python3
  pip3 install opencv-contrib-python==4.1.0.25

Una forma de validar que todo esta bien, es ejecutando este codigo

>>> import cv2
>>> cv2.__version__
'4.1.0'

![imagen](https://user-images.githubusercontent.com/6835007/138108151-01748e07-1775-4574-bcbc-78c9632bfd3f.png)

