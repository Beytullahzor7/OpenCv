import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)


def empty(a):
    pass
cv2.namedWindow("HSV")

cv2.createTrackbar("HUE min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT max", "HSV", 0, 179, empty)
cv2.createTrackbar("VALUE min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE max", "HSV", 255, 255, empty)




while True:

    _, img = cap.read()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE min", "HSV")
    h_max = cv2.getTrackbarPos("HUE max", "HSV")
    s_min = cv2.getTrackbarPos("SAT min", "HSV")
    s_max = cv2.getTrackbarPos("SAT min", "HSV")
    v_min = cv2.getTrackbarPos("VALUE min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE min", "HSV")
    print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_hsv, lower, upper)
    result = cv2.bitwise_and(img,img, mask=mask )




    cv2.imshow("Original", img)
    cv2.imshow("HSV",img_hsv)
    cv2.imshow("MASK", mask)
    cv2.imshow("Result", result)
    if  cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

