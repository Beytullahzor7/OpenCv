#Opencv ve numpy fonk. kullanarak çizim yapmak ve ekrana yazı yazdırmak

import cv2
import numpy as np

#şimdi çizim yapacagımız tuvali olusturuyoruz
#bu aşamada numpy kütüphanesinin bize sagladıgı bazı özellikleri kullanıcaz

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255 #(0,0,0) + 255 = (255,255,255)
#belirledigim büyüklükteki bir alana beyaz renk degerleri doldurmak
#np.zeros fonk  ekranı siyah piksellerle doldurur daha sonra biz ekranı manipüle ederek ekranı beyaza çeviririz

cv2.line(canvas,(0,0),(512,512),(255,0,0),5) #bilgisayarlarda (0,0) noktası sol üst noktadır
#1. parantez baslangıç
#2. parantez bitiş
#3. parantez renk degerleri
#4. parantez çizgi kalınlıgı
cv2.rectangle(canvas,(150,150),(320,320),(0,255,0),-1) #dikdörtgen çizimi #-1 ile içi dolu yaptık
cv2.circle(canvas,(150,150),50,(0,0,255),10) #çember elde etmek

font = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_TRIPLEX
font3 = cv2.FONT_HERSHEY_COMPLEX
font4 = cv2.FONT_HERSHEY_COMPLEX_SMALL

cv2.putText(canvas, "OpenCV", (20, 100), font3, 4, (245, 158, 66), 3, cv2.LINE_AA ) # (245, 158, 66) = acık mavi
#tuvale yazı yazdırmak

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()



