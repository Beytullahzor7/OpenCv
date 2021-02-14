#TRACKBAR = RGB kızakları olusturarak pencere rengi ile oynamaktır

import  cv2
import numpy as np

def nothing(x):
    pass


canvas = np.zeros((512,512,3), dtype=np.uint8)
cv2.namedWindow("image") #oluşturacagımız pencereye bir ad vermek için bu fonk. kullarız

cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

#anahtar ancak açık oldugu durumlarda trackbar değişmesini istersek bir switch oluştururuz
cv2.createTrackbar("Switch", "image", 0, 1, nothing)

while True:  #trackbar üzerindeki değerleri devamlı olarak cekmek için bu döngüyü oluşturduk
    cv2.imshow("image",canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'): #eğer q ya basarsak döngüyü durdururuz
        break

    s = cv2.getTrackbarPos("Switch","image")
    r = cv2.getTrackbarPos("R","image") #trackbardan çektigimiz degerleri tek tek kaydetmek için bu fonk. kullandık
    g = cv2.getTrackbarPos("G","image")
    b = cv2.getTrackbarPos("B","image")

    if s == 1:

        canvas[:] = [b, g, r] #r,g,b olarak çektigim değerleri tuvale yansıtmak için bu komutu kullandı
    else:

        canvas[0, 0, 0]
cv2.destroyAllWindows()

