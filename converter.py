import cv2
import numpy as np
import os

# Playing video from file:
vid = cv2.VideoCapture('badapple.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret , frame = vid.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    
    cv2.imwrite(name, frame)
    if currentFrame%1000 == 0:
        print("Converting...")
    # To stop duplicate images
    currentFrame+=1
    
print("Converted: " + str(currentFrame))
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()