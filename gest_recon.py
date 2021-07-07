import streamlit as st
import cv2,pyautogui
from cvzone.HandTrackingModule import HandDetector
from win32api import GetSystemMetrics
import sys,os


'''
In order to close game, Display left hand smallest finger to camera
'''



frameST = st.empty()
croppedST = st.empty()
label = st.empty()

st.title('Hand gesture recognition- Lets Play with just hands')

def exit():
    pass
    #os.system("taskkill /f /im  python.exe")

if True:
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    detector = HandDetector(detectionCon=0.5, maxHands=1)

    while True:
        success, img = cap.read()
        img = cv2.flip(img,1)
        img = detector.findHands(img)

        lmList, bboxInfo = detector.findPosition(img)
        if lmList:
            bbox = bboxInfo['bbox']
            fingers = detector.fingersUp()
            print(fingers)
            if fingers==[0,0,0,0,1]:
                exit()

            totalFingers = fingers.count(1)
            if int(totalFingers)==4 or int(totalFingers)==5:
                (x, y) = pyautogui.position()
                mov_x = 0.9375*width
                mov_y = 0.8240*height
                pyautogui.click(mov_x, mov_y)
                pyautogui.moveTo(x, y)

        frameST.image(img, channels="BGR")
        #cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



