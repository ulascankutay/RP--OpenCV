import cv2 

img1 = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")

img3 = cv2.imread("grey1.jpg")
img4 = cv2.imread("grey2.jpg")

# Toplama
result = cv2.add(img1,img2)
result2 = cv2.addWeighted(img1,0.8,img2,0.2,0)

# Çikarma

sonuc = cv2.subtract(img3,img4)


cv2.imshow("sonuc",sonuc)

# cv2.imshow("result",result)
# cv2.imshow("result2",result2)

# cv2.imshow("1",img1)
# cv2.imshow("2",img2)



cv2.imshow("grey1",img3)
cv2.imshow("grey2",img4)






cv2.waitKey(0)
cv2.destroyAllWindows()