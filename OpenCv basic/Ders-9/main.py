import cv2




img = cv2.imread("a1.jpg")


img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur= cv2.medianBlur(img_grey,7)

edge=cv2.Canny(img_blur,50,150)


cv2.imshow("edge",edge)
cv2.imshow("duz",img)

cv2.waitKey(0)
cv2.destroyAllWindows()