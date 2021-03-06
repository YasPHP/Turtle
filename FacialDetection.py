# -*- coding: utf-8 -*-
"""
@author: alana
"""

import numpy as np
import cv2
from os import listdir
from os.path import isfile, join

# directory path of face filter images
mypath='./NTFaces'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
face_list = np.empty(len(onlyfiles), dtype=object)

# loops through possible face filter images in the directory outlined in the path
for n in range(0, len(onlyfiles)):
  face_list[n] = cv2.imread( join(mypath,onlyfiles[n]) )

# Haar Cascade classifier is an effective object detection approach
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
# calls the video camera
cap = cv2.VideoCapture(0)
chosen_face = 0

# infinite loop - keeps camera on
while(1):
    

    # face tracker image overlay
    overlay = face_list[chosen_face]
    
    # the captured media is read
    ret, img = cap.read()
    
    # colour converted from red, green, blue to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # receives a frame (img) as an argument and runs the classifier cascade over the image. 
    # the algorithm looks at subregions of the image in multiple scales, to detect faces of varying sizes.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # face tracking loop
    for (x,y,w,h) in faces:
        
        # adds rectangle around face tracker
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        
        # the text displayed on top of the framed face's rectangle
        cv2.putText(img,"Face Detected",(x,y),1,1,(0,255,0),2)
        
        # image is overlayed on top of face tracker rectangle
        try: img[y:y+overlay.shape[0], x:x+overlay.shape[1]] = overlay
          
        # otherwise, no overlay is placed
        except: continue
        
    # shows the face cover on webcam stream
    cv2.imshow('Face Cover',img)
    
    # the keyboard key in question
    k = cv2.waitKey(30) & 0xff
    
    # escape button to close window
    if k == 27:
        break
    # spacebar command to alternate face filters
    if k == 32:
        if chosen_face == len(face_list) - 1:
            chosen_face = 0
        else:
            chosen_face += 1
        
    
# closes all windows, including webcam capture
cv2.destroyAllWindows()
cap.release()
