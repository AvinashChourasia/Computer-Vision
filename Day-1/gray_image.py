import cv2
img = cv2.imread("sevak2.png")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImage.png",grayImg)
cv2.imshow("Original",img)
cv2.imshow("GrayImage",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
