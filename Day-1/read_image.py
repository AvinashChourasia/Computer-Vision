import cv2
img = cv2.imread("sevak.png")
cv2.imshow("Sevak Logo",img)
cv2.imwrite("Sevak_Logo.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
