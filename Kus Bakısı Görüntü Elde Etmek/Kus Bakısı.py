import cv2
import numpy as np

img = cv2.imread("s-d99c92418acd8f23a5bfa27e3a0c8229a2b7ee89.jpg")

width, height = 250, 350
pts1 = np.float32([[569, 164], [824, 230], [398, 445], [743, 585]])
pts2 = np.float32([[0, 0],[width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, matrix, (width, height))


for x in range(0, 4):
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 15, (0, 100, 255), cv2.FILLED)

cv2.imshow("Original Image", img)
cv2.imshow("Output",output)
cv2.waitKey(0)

