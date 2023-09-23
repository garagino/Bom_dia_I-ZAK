import cv2
import dlib

detector_facial = dlib.get_frontal_face_detector()

captura_camera = cv2.VideoCapture(0)

width = captura_camera.get(3)
height = captura_camera.get(4)
centro_camera = (int(width/2), int(height/2))

while True:
    ret, frame = captura_camera.read()
    cv2.circle(frame, centro_camera, 5, (0, 0, 255), thickness=-1)

    try:
        deteccoes = detector_facial(frame, 1)

        y = (deteccoes[0].top() + deteccoes[0].bottom()) / 2
        x = (deteccoes[0].left() + deteccoes[0].right()) / 2

        cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), thickness= -1)

        cv2.line(frame, centro_camera, (int(x), int(y)), (0, 0, 255), 2)

        cv2.putText(frame, f'distancia = {int(x) - centro_camera[0]}', (200,200), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 1, cv2.LINE_AA)

    except:
        #caso nenhuma face seja detectada
        cv2.putText(frame, 'Erro', (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()