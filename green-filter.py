import numpy as np
import cv2
import random
from python_utils import CFEVideoConf, image_resize
import glob
import math


cap = cv2.VideoCapture(0)

# frames_per_seconds = 20
# save_path='saved-media/filter.mp4'
# config = CFEVideoConf(cap, filepath=save_path, res='480p')
# out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)


def apply_color_overlay(frame, intensity=0.5, blue=0, green=0, red=0):
    frame = verify_alpha_channel(frame)
    frame_h, frame_w, frame_c = frame.shape
    sepia_bgra = (blue, green, red, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)
    return frame


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA) 
    #cv2.imshow('frame',frame)

    color_overlay = apply_color_overlay(frame.copy(), intensity=.8, red=123, green=231)
    cv2.imshow('color_overlay',color_overlay)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
