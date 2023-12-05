import cv2


fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw = cv2.VideoWriter("E:\\vv\\2.mkv",fourcc,25,(1920,1080))

cv2.namedWindow("aa",cv2.WINDOW_NORMAL)
cv2.resizeWindow("aa",1920,1080)
cap = cv2.VideoCapture("E:\\vv\\1.mkv")

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow('aa',frame)
        
        vw.write(frame)
        
        key = cv2.waitKey(40)# 摄像头用1
        if(key == ord("q")):
            break
        
cap.release()
vw.release()
cv2.destroyAllWindows()
