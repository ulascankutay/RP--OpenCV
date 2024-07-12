import cv2
import numpy as np
img =cv2.imread("a1.jpg")

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_grey,(5,5),0)


edges = cv2.Canny(img_blur,50,150)

kernel0 = np.ones((20,20),np.uint8)

dilated_img = cv2.dilate(edges,kernel0, iterations=1)

cv2.imshow("dilate",dilated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
