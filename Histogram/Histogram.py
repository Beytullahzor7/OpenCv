# Histogram bize resimdeki renk yogunluklarıyla ilgili bilgi veren grafiktir.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((200, 200), dtype=np.uint8)

cv2.circle(img, (100,100), 30, 255, -1)
cv2.imshow("Canvas", img)




#print(img.size) #toplam piksel sayısını verir
#print(img.shape) #resmin kaca kaclık oldugunu verir
#print(img)
#print(img.ravel())

plt.hist(img.ravel(), 256, [0,256]) #grafigin x ekseni (0,256) #tüm verileri yatay sekilde ravel fonk ile sıralarız
#her bir renk degerinin 0 dan 255 e kadar renk karsılıgı vardır yani toplamda 256 adet renk degeri vardır
plt.show()

