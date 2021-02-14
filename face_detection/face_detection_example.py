import cv2
import numpy as np

img = cv2.imread("cristiano-ronaldo-lionel-messi-neymar-renderfristajlere-neymar-messi-neymar-ronaldo-png-920_848.png")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors= 7)

print("Faces Detected", len(faces))

for x, y ,w, h in faces:

    cv2.rectangle(img, (x,y), (x+h, y+h), (0,0,255), 4)

cv2.imshow("Face Detected", img)

cv2.waitKey(0)
cv2.destroyAllWindows()