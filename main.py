import cv2
from datetime import *

import time

global personInRoom
personInRoom = False


data = cv2.CascadeClassifier("fullbody_data.xml")

webcam = cv2.VideoCapture(0)


def on():
    print("Light turn on function goes here")


def off():
    print("Light turn off function goes here")


while True:

    successful_frame_read, frame = webcam.read()
    greyscaleimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = data.detectMultiScale(greyscaleimg)

    try:
        if faces.any():
            if personInRoom:
                off()
                time.sleep(240)
            else:
                personInRoom = True
                on()
                time.sleep(240)

    except:
        pass

    key = cv2.waitKey(1)
