import cv2
import dlib

detector_facial = dlib.get_frontal_face_detector()

captura_camera = cv2.VideoCapture(0)

repeticao = True

while True:
  ret, frame = captura_camera.read()
  deteccoes = detector_facial(frame, 1)
  if len(deteccoes) == 0:
      repeticao = True
  for face in deteccoes:
    l, t, r, b = face.left(), face.top(), face.right(), face.bottom()
    cv2.rectangle(frame, (l, t), (r, b), (255, 255, 255), 2)
    distancia_vert = abs(t-b)
    distancia_hor = abs(l-r)
    if (distancia_hor >= 63 and distancia_hor >= 62) and repeticao:
        print("Bom Dia")
        repeticao = False
    if (distancia_hor < 63 and distancia_hor < 62):
        repeticao = True
  cv2.imshow("Video", frame)
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break
captura_camera.release()