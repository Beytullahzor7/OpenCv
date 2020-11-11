#Opencv ve numpy fonk. kullanarak çizim yapmak ve ekrana yazı yazdırmak

import cv2
import numpy as np

#şimdi çizim yapacagımız tuvali olusturuyoruz
#bu aşamada numpy kütüphanesinin bize sagladıgı bazı özellikleri kullanıcaz

canvas = np.zeros((512,512,3),dtype=np.uint8) + 255 # (0,0,0) + 255 = (255,255,255)
#belirledigim büyüklükteki bir alana beyaz renk degerleri doldurmak
#np.zeros fonk  ekranı siyah piksellerle doldurur daha sonra biz ekranı manipüle ederek ekranı beyaza çeviririz

#cv2.line(canvas,(0,0),(512,512),(255,0,0),5) #bilgisayarlarda (0,0) noktası sol üst noktadır
#1. parantez baslangıç
#2. parantez bitiş
#3. parantez renk degerleri
#4. parantez çizgi kalınlıgı
#cv2.rectangle(canvas,(150,150),(320,320),(0,255,0),-1) #dikdörtgen çizimi
#cv2.circle(canvas,(150,150),50,(0,0,255),3) #çember elde etmek

font = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_TRIPLEX
font3 = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(canvas, "OpenCV", (10,100), font3, 4,(245, 158, 66), 5 , cv2.LINE_AA )

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()



