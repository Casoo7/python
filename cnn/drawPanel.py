import cv2
import numpy as np

def mouse_callback(event,x,y,flags,userdata):
    if(userdata[1] == "l"):
        if(event==cv2.EVENT_LBUTTONDOWN):
            cv2.line(userdata[0],(0,0),(500,500),(0,0,255),100,16)
            cv2.imshow("aa",userdata[0]) 
    print(event,x,y,flags,userdata[1])


img = np.zeros((1080,1920,3),np.uint8)
cv2.imshow("aa",img) 
flag = '0'
userdata=[img,flag]
cv2.setMouseCallback('aa',mouse_callback,userdata)

while True:
    key = cv2.waitKey(1)
    if(key == ord("q")):
        break
    if(key == ord("l")):
        userdata[1] = 'l'
        cv2.setMouseCallback('aa',mouse_callback,userdata)
    if(key == ord("c")):
        cv2.setMouseCallback('aa',mouse_callback,"c")
    if(key == ord("e")):
        cv2.setMouseCallback('aa',mouse_callback,"e")
    if(key == ord("p")):
        cv2.setMouseCallback('aa',mouse_callback,"p")
    if(key == ord("f")):
        cv2.setMouseCallback('aa',mouse_callback,"f")
cv2.destroyAllWindows()