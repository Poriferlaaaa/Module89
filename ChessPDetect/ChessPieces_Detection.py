import cv2 
import numpy as np 
from threading import Thread
import detection_ as detectCP

def capture2Images():
    path = "captureImg/"
    # path2 = "captureImgTop/"
    cam = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
    # cam2 = cv2.VideoCapture(2 + cv2.CAP_DSHOW)

    cam.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off
    cam.set(28,28)
    cam.set(17,6500) #set WHITE_BALANCE
    cam.set(3, 1280) # set the Horizontal resolution 
    cam.set(4, 720) # Set the Vertical resolution

    # cam2.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off
    # cam2.set(28,28)
    # cam2.set(17,6500) #set WHITE_BALANCE
    # cam2.set(3, 1280) # set the Horizontal resolution 
    # cam2.set(4, 720) # Set the Vertical resolution

    check, frame = cam.read()
    # check2, frame2 = cam2.read()
        # cv2.imshow("i", frame)
    cv2.imwrite(path + str(1) + '.jpg',frame)
    # cv2.imwrite(path + str(1) + '.jpg',frame2)

    print ("capture end")

def getdata():
    # capture2Images()
    info = detectCP.main(detectCP.parse_opt())
    return info
    
if __name__ == "__main__":   
    getdata()