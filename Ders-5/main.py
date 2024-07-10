import cv2

# dahili kamera 0 usb ile takılı olan 1
cap=cv2.VideoCapture(0)


while True :
     #Görüntü okuma
    _,frame  =cap.read()

    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0Xfff ==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()