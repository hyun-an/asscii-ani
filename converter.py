import cv2
import numpy as np
import os

# Playing video from file:
vid = cv2.VideoCapture('video_to_convert.mp4')

print("Fps: " + str(vid.get(cv2.CAP_PROP_FPS)))

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

currentFrame=4000
def convert():
    currentFrame = 0
    while(True):
        # Capture frame-by-frame
        ret , frame = vid.read()

        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
    
        cv2.imwrite(name, frame)
        if currentFrame%1000 == 0:
            print("Converting...")
            print(currentFrame)
        # To stop duplicate images
        currentFrame+=1
    

def gibFrameCount(currentFrame):
    return currentFrame


try:
    convert()
except cv2.error as e:
    print("Done with Converting")