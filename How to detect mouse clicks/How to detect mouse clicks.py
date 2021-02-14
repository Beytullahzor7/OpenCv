import cv2
import numpy as no


def MouseClicks(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

img = cv2.imread("Skiing-Around-the-World-Volume-2-400x400.jpg")
cv2.imshow("Original Image", img)
cv2.setMouseCallback("Original Image", MouseClicks)

cv2.waitKey(0)