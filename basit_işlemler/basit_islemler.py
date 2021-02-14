#piksel kavramı üzerinden ilerleyerek uygulamalar yapacagız
#ROU = REGION OF INTEREST


import cv2
import numpy as np

img = cv2.imread("images.jpg")

face = img[0:90, 80:200] #0:90 y ekseni  80:200 x ekseni
cv2.imshow("image", img)
cv2.imshow("ROI", face)
#cift tırnak arasına girilen isim istedigimiz pencere adıdır
#burada ROI kavramını kullanmayı denedik
#amaç çalışacagımız kişinin veya resmin yüz bölgesini ele alarak işlem yapmak

cv2.waitKey(0)
cv2.destroyAllWindows()

#1-Piksellerin sakladıkları renk degerlerini görmek


#color = img[150,200] #girdigimiz koordinat resmin sahip oldugu boyuttan daha büyük olmamalı
#belirledigimiz aralıktaki istedigimiz renk yogunlukları görmek için kullanırız

#blue = img[150 ,200 ,0] #buradaki 0 color dizisinin ilk elemanına erişmek için konuldu
#green =img[150,200, 1]
#red =img[150,200,2]
#shape = img.shape #resmin sahip oldugu boyutları bastırır


#print("Color:",color)
#print("Blue:",blue)
#print("Green:",green)
#print("Red:",red)

#print("Shape:",shape) #şu ana kadarki komutlarla resmin sahip oldugu herhangi bir pikseldeki renk değerlerine
#nasıl erişebilecegimizi gösterdik

#şimdide eriştigimiz renk değerini nasıl değiştirecegimizi görelim

#img[150,200,0] = 200
#print(img[150,200,0])


#red2 = img.item(150,200,2) #img.item ile 150,200 deki piksel değerine erişip o değeri red2 ye eşitleyebilirim
#print(red2)

#img.itemset((150,200,2),200)
#print(img[150,200,2])

