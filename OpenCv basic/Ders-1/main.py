import cv2

image = cv2.imread("image.png")

roi = image[0:50,0:150]


cv2.imshow("Roi",roi)
cv2.imwrite("image3.png",roi)
cv2.imshow("frame",image)
cv2.waitKey(3000)
cv2.destroyAllWindows()
