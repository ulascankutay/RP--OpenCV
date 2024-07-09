import cv2


img=cv2.imread("image.png")

b,c,r=cv2.split(img)

merge = cv2.merge((b,c,r))

cv2.imshow("mavi",b)
cv2.imshow("yeşil",c)
cv2.imshow("kirmizi",r)

cv2.imshow("merge",merge)

# cv2.imshow("frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()