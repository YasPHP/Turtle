# -*- coding: utf-8 -*-
"""
@author: alana
"""
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    
# calls the video camera
cap = cv2.VideoCapture(0)

# infinite loop - keeps camera on
while(1):

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(img,"Face Detected",(x,y),1,1,(0,255,0),2)
        
        

    cv2.imshow('Face Detector',img)
    
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
    
    



cv2.destroyAllWindows()
cap.release()