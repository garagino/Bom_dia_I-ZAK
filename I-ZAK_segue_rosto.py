import cv2
import dlib

detector_facial = dlib.get_frontal_face_detector()

captura_camera = cv2.VideoCapture(0)

width = captura_camera.get(3)
height = captura_camera.get(4)
centro_camera = (int(width / 2), int(height / 2))

while True:
    ret, frame = captura_camera.read()

    try:
        deteccoes = detector_facial(frame, 1)

        y = (deteccoes[0].top() + deteccoes[0].bottom()) / 2
        x = (deteccoes[0].left() + deteccoes[0].right()) / 2

    except:
        #sem faces detectadas
        retorno = 0

    else:
        retorno = centro_camera[0] - x


