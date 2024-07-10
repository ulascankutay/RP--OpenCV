import cv2
import numpy as np

img =np.zeros((600,800,3),np.uint8)


cv2.rectangle(img,(100,100),(600,800),(0,0,250),2)
cv2.line(img,(0,300),(800,300),(0,0,255),2,3)
cv2.putText(img,"FPS : 60",(100,100),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)

cv2.imshow("black",img)




cv2.waitKey(0)
cv2.destroyAllWindows()