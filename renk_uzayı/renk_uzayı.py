#RENK UZAYI BİR GÖRÜNTÜNÜN SAHİP OLDUGU RENK ORGANİZASYONLARIDIR

import cv2

img = cv2.imread("muslera.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA) #renk organizasyonu değiştirme fonk.
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #HSV modunu nesneleri takip etmek için old. fazla kullanırız
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#RGB modda piksellerin sahip oldugu renkler karışır ve yeni bir görünüm kazanır

cv2.imshow("BGR",img)
cv2.imshow("RGB",rgb_img)
cv2.imshow("HSV",hsv_img)
cv2.imshow("GRAY",gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

