import cv2
import time
import os
import HTModule as htm

Wcam, Hcam = 640, 480

cam = cv2.VideoCapture(0)
cam.set(3, Wcam)
cam.set(4, Hcam)

detector = htm.handDetector()


ptime = 0

while True:
    success, img = cam.read()
    if not success:
        print("Failed to capture image")
        break

    img = detector.findHands(img)
    lmList = detector.FindPosition(img)

    tipIds = [4, 8, 12, 16, 20]

    if len(lmList)!=0:
        fingers = []

        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range (1,5):
            if lmList[tipIds[id]][2]<lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        f = 0
        for i in range(5):
            f+=fingers[i]

        cv2.putText(img, str(f), (20,30), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3)


    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)


    cv2.imshow("Finger Counter", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break