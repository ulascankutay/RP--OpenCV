import cv2
import numpy as np

img =cv2.imread("a1.jpg")

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_grey,(5,5),0) # median buluır benzer 

_, th = cv2.threshold(img_blur,250,270,cv2.THRESH_BINARY) # iki katmanlı beyaz ve siyah 

conters,_ = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE,) #contours değerini buluyor


for cnt in conters: #koşelerdeki noktaları gezip conters değerini buluyor 
    area = cv2.contourArea(cnt) # alan hesaplama 
    print(area)
    if area>27484 : # alana göre ekran bastırma
        cv2.drawContours(img,[cnt],-1,(0,255,0),2) # liste hainde gelen noktaları çiziyor 


cv2.imshow("th",th)
cv2.imshow("counters",img)
cv2.waitKey(0)
cv2.destroyAllWindows()