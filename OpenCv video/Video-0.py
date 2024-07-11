import cv2 
import imutils

cap = cv2.VideoCapture(0)


while True :
    ret,frame = cap.read() # doğru okunma ret okunan deger frame 
    frame = imutils.resize(frame,width=1080) #yeniden boyutlanıdrma
    cv2.rectangle(frame,(10,600),(1000,400),(255,0,0),2)
    if ret == False:
        break
    cv2.imshow("onkamera",frame)

    if cv2.waitKey(30) & 0xff == 27 :
        break

cap.release()
cv2.destroyAllWindows()