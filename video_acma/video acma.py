import cv2
import numpy as np

frameWidth = 640
frameHeight = 360

cap = cv2.VideoCapture("C:/Users/Monster/Opencv/video_acma/video.mp4")


while True:

    success,img = cap.read()
    cv2.imshow("Video",img)

    if cv2.waitKey(1) % 0XFF == ord('q'):
        break