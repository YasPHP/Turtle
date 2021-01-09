# import OpenCV + NumPy
import cv2
import numpy as np

# calls the video camera
cap = cv2.VideoCapture(0)

# infinite loop - keeps camera on
while(1):

    # reads each frame of the video (opencv interprets video into a series of images)
    _, frame = cap.read()

    # for easy processing: converting colour from RGB/BGR to HSV!
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # range of colours
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    # a mask for the video's frames
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # resulting frame with the mask
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # shows the original frame
    cv2.imshow('Original',frame)

    # Canny Edge Outline Detector function
    edges = cv2.Canny(frame,100,200)

    # shows the outlined video footage
    cv2.imshow('Edges',edges)

    k = cv2.waitKey(5) & 0xFF

    # click the escape button on keyboard to exit camera view
    if k == 27:
        break

# closes the webcam window
cv2.destroyAllWindows()
cap.release()
