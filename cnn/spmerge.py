import cv2
import numpy as np

img = np.zeros((1080,1920,3),np.uint8)

count = 0
while count<100:
    count=count+1
    img[100,count,0] = 255
    
roi = img[100:300,100:300]
roi[:] = [255,0,0]

b,g,r = cv2.split(img)

cv2.imshow("aa",img)  
cv2.imshow("bb",b)  

while True:
    key = cv2.waitKey(1)
    if(key == ord("q")):
        break
cv2.destroyAllWindows()