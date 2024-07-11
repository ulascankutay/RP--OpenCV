import cv2
import numpy as np

img1 = np.zeros((600,400),np.uint8)
img2 = np.zeros((600,400),np.uint8)


cv2.line(img2,(0,300),(600,300),(255,0,0),2)


cv2.putText(img1,"ULAS CAN KUTAY",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,255,2)
cv2.rectangle(img1,(100,300),(200,200),(255,0,0),-1)

cv2.imshow("ekran1",img1)
cv2.imshow("ekran2",img2)



cv2.waitKey(0)
cv2.destroyAllWindows()