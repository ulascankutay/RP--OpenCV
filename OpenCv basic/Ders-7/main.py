import cv2 


img=cv2.imread("1.jpg")
print(img.shape)

r = cv2.resize(img,(250,120))


cv2.imshow("r",r)
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

