#Görüntülerdeki gürültüleri azaltmak için morfolojik işlemler kullanılır
#erosion,dilation,opening,closing işlemlerinin ne olduguna bir göz atalım
#MORFOLOJİK İŞLEMLER HER ZAMAN BİNARY RESİMLER ÜZERİNDE YAPILIR

import cv2
import numpy as np

img = cv2.imread("closing.png")
kernel = np.ones((5, 5), np.uint8) #ones parantezi içerisi her zaman tek sayı olmalıdır
#kernel bir tür matristir ve kernel ne kadar büyük olursa resim o kadar bozunuma uğrar, gürültüleri eleyebildigim kadar yüksek olmalıdır

erosion = cv2.erode(img, kernel, iterations=3) #erosion ile resmi zayıflatma işlemi uygulanır#
dilation = cv2.dilate(img, kernel, iterations=1)#dilation ile resmi genişletme işlemi uygulanır#
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) #resimlerin dışında kalan gürültüleri temizlemek için kullanılır
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) #resimlern içinde kalan gürültüleri temizlemek için kullanılır

cv2.imshow("Original",img)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)
cv2.waitKey(0)
cv2.destroyAllWindows()