import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while(True):
    exito, imagen = webcam.read()
    coordenadas, imagen_manos = rastreador.findHands(imagen)
    
    cv2.imshow("Proyecto 4 - IA", imagen)
    
    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()