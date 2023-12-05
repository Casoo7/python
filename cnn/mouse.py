import cv2
import numpy as np
# 鼠标事件
def mouse_callback(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)

cv2.namedWindow("aa",cv2.WINDOW_NORMAL)
cv2.resizeWindow("aa",1920,1080)
cv2.setMouseCallback('aa',mouse_callback,"howlll")
img = np.zeros((1080,1920,3),np.uint8)
while True:
    cv2.imshow("aa",img)
    
    key = cv2.waitKey(1)# 摄像头用1
    if(key == ord("q")):
        break
cv2.destroyAllWindows()