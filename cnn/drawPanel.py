import cv2
import numpy as np

def mouse_callback(event,x,y,flags,userdata):
    print(startPt)
    if(userdata[1] == "l"):
        # startPt = userdata[2]
        # endPt = userdata[3]
        if(event==cv2.EVENT_LBUTTONDOWN):
            if(startPt == (-1,-1)):
                startPt = (x,y)
            if(startPt != (-1,-1)):
                endPt = (x,y)
                cv2.line(img,startPt,endPt,(0,0,255),2,16)
                cv2.imshow("aa",userdata[0])
                startPt = (-1,-1)   
                endPt = (-1,-1)
        if(event==cv2.EVENT_MOUSEMOVE):
            if(startPt != (-1,-1)):
                endPt = (x,y)
                cv2.line(userdata[0],startPt,endPt,(0,0,255),100,16)
                cv2.imshow("aa",userdata[0])
    print(event,x,y,flags,userdata[1])


img = np.zeros((540,860,3),np.uint8)
cv2.imshow("aa",img) 
flag = '0'

startPt = (-1,-1)
endPt = (-1,-1)
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