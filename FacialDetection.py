# -*- coding: utf-8 -*-
"""
@author: alana
"""

import numpy as np
import cv2
from os import listdir
from os.path import isfile, join

mypath='./NTFaces'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
face_list = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  face_list[n] = cv2.imread( join(mypath,onlyfiles[n]) )


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
# calls the video camera
cap = cv2.VideoCapture(0)

chosen_face = 0

# infinite loop - keeps camera on
while(1):
    

    overlay = face_list[chosen_face]
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(img,"Face Detected",(x,y),1,1,(0,255,0),2)
        
        img[y:y+overlay.shape[0], x:x+overlay.shape[1]] = overlay
        

    cv2.imshow('Face Cover',img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if k == 32:
        if chosen_face == len(face_list) - 1:
            chosen_face = 0
        else:
            chosen_face += 1
        
    

cv2.destroyAllWindows()
cap.release()