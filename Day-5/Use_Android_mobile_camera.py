import numpy as np
import cv2
import imutils
import urllib.request

url="http://100.78.74.220:8080/shot.jpg"
while True:
    imgpath = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgpath.read()),dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    img = imutils.resize(img,width=800)
    cv2.imshow("Camerafeed",img)
    if ord('q') == cv2.waitKey(1):
        exit(0)
