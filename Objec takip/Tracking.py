import cv2
import numpy as np

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

tracker = cv2.TrackerMOSSE_create()
success, img = cap.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img,bbox)

def drawBox():
    pass

while True:

    timer = cv2.getTickCount()
    success, img = cap.read()
    success, bbox = tracker.update(img)

    if success:
        drawBox()
    else:
        cv2.putText(img, "Lost", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)

    cv2.putText(img, str(int(fps)), (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    cv2.imshow("Tracking", img)

    if   cv2.waitKey(1) & 0XFF == ord('q'):
        break
