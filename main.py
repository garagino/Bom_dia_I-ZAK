import cv2
import dlib
import numpy as np

detector_facial = dlib.get_frontal_face_detector()
captura_camera = cv2.VideoCapture(0)

while True:
    ret, frame = captura_camera.read()
    deteccoes = detector_facial(frame, 1)
    x = (deteccoes[0].top() + deteccoes[0].bottom()) / 2
    y = (deteccoes[0].left() + deteccoes[0].right()) / 2
    print(x, y)
    cv2.circle(frame, (int(y), int(x)), 5, (0,0,255), thickness= -1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()