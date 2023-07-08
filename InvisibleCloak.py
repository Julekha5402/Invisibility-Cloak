import numpy as np
import cv2
import time
print("!!!Invisibility is no more a dream!!!")
cap=cv2.VideoCapture(0)
time.sleep(3)
for i in range(30):
    retval,back=cap.read()
back=np.flip(back,axis=1)
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,img = cap.read()
    if ret:
        img=np.flip(img,axis=1)
        hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        lower_red = np.array([170, 120, 70])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)
        mask1+=mask2
        mask = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
        img[np.where(mask==255)]=back[np.where(mask==255)]

        cv2.imshow("MAGIC BEGINS!!!",img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
