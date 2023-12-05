import cv2
import numpy as np

img = np.zeros((1080,1920,3),np.uint8)

cv2.line(img,(0,0),(500,500),(0,0,255),100,16)
cv2.circle(img,(700,700),50,(0,0,255),-1)
cv2.ellipse(img,(900,900),(50,100),0,560,180,(0,0,255),-1)


pts = np.array([(0,0),(100,100),(333,444),(896,102)],np.int32)
cv2.polylines(img,[pts],True,(0,0,255))
cv2.fillPoly(img,[pts],(0,0,255))


cv2.putText(img,"1lnmlksdajfliasjfl",(600,200),cv2.FACE_RECOGNIZER_SF_FR_COSINE,5,(255,0,0))

cv2.imshow("aa",img)  

while True:
    key = cv2.waitKey(1)
    if(key == ord("q")):
        break
cv2.destroyAllWindows()