import cv2
import numpy as np

def callback():
    pass

cv2.namedWindow("aa",cv2.WINDOW_NORMAL)
cv2.resizeWindow("aa",1920,1080)

cv2.createTrackbar('R','aa',0,255,callback)
cv2.createTrackbar('G','aa',0,255,callback)
cv2.createTrackbar('B','aa',0,255,callback)
 

img = np.zeros((1080,1920,3),np.uint8)
while True:
    r = cv2.getTrackbarPos('R','aa')
    g = cv2.getTrackbarPos('G','aa')
    b = cv2.getTrackbarPos('B','aa')
    
    img[:] = [b,g,r]
    
    cv2.imshow("aa",img)
    key = cv2.waitKey(1)# 摄像头用1
    if(key == ord("q")):
        break
cv2.destroyAllWindows()