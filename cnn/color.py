import cv2
import numpy as np

def callback():
    pass

cv2.namedWindow("aa",cv2.WINDOW_NORMAL)
cv2.resizeWindow("aa",961,1200)

colorspaces = [cv2.COLOR_BGR2RGBA,cv2.COLOR_BGR2BGRA,cv2.COLOR_BGR2GRAY,cv2.COLOR_BGR2HSV,cv2.COLOR_BGR2YUV]

cv2.createTrackbar('R','aa',0,4,callback)
 

img = cv2.imread("E:\\vv\\i.webp")

while True:
    index = cv2.getTrackbarPos('R','aa')
    cvt_img = cv2.cvtColor(img,colorspaces[index])
    cv2.imshow("aa",cvt_img)
    key = cv2.waitKey(1)
    if(key == ord("q")):
        break
cv2.destroyAllWindows()