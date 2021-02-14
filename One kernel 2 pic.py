import cv2
import numpy as np

img1 = cv2.imread("road.jpg")
img2 = cv2.imread("istockphoto-853681562-612x612.jpg")

print(img1.shape)
print(img2.shape)

width, height = 300, 300
img1 = cv2.resize(img1, (width, height))
img2 = cv2.resize(img2, (width, height))
print(img1.shape)
print(img2.shape)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

horizontal = np.hstack((img1, img2))
vertical = np.vstack((img1, img2))

cv2.imshow("Vertical",vertical)
cv2.imshow("Horizontal",horizontal)

cv2.waitKey(0)