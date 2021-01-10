# -*- coding: utf-8 -*-
"""
@author: alana
"""

import numpy as np
import cv2

overlay = cv2.imread("Leo-Clear-temp.png")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
# calls the video camera
cap = cv2.VideoCapture(0)


# infinite loop - keeps camera on
while(1):

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        
        print(x,y,x+w,y+h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(img,"Face Detected",(x,y),1,1,(0,255,0),2)
        
        img[y:y+overlay.shape[0], x:x+overlay.shape[1]] = overlay
        

    cv2.imshow('Face Cover',img)
    
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
    

cv2.destroyAllWindows()
cap.release()