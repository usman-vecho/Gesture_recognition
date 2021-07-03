import streamlit as st
import cv2,pyautogui
from cvzone.HandTrackingModule import HandDetector

st.title('Project - Arabic Sign Language')

cap = cv2.VideoCapture(0)
frameST = st.empty()
croppedST = st.empty()
label = st.empty()

cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=1)




while True:

    success, img = cap.read()


    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    if lmList:
        bbox = bboxInfo['bbox']


        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        if int(totalFingers)==4 or int(totalFingers)==5:
            (x, y) = pyautogui.position()

            pyautogui.click(1800, 890)

            pyautogui.moveTo(x, y)
        #cv2.putText(img, f'Fingers:{totalFingers}', (bbox[0] + 200, bbox[1] - 30),cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    img2 = img.copy()
    img2 = cv2.resize(img2,(200,100))
    #cv2.imshow("Image", img2)
    frameST.image(img, channels="BGR")
    #label.info(f'Fingers:{totalFingers}')
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
#cap.release()
#cv2.destroyAllWindows()


