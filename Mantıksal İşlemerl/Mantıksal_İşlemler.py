import cv2
import numpy as np
import matplotlib.pyplot as plt

#resimler np.uint-8 tipinde verilerdir#
#resimler aslında matrislerdir ve bunlar üzerinde toplama çıkarma#
#işlemi yapabilmek işin satır ve sütunları eşit olmalıdır#

"""
x = np.uint8([120])
y = np.uint8([25])

z = cv2.add(x,y)

print(z)


img1 = np.zeros((300,300,3), np.uint8) + 255
cv2.circle(img1,(150,150),50,(255,0,0),-1)

img2 =np.zeros((300,300,3), np.uint8) + 255 #buradaki 3 kanal verisini girmezsem her seyi siyah yada beyaz algılar
cv2.line(img2,(0,0),(300,300),(0,255,0),5)
#iki resim arasında toplama yaptıgımız için ikisi de aynı matris degeri yani  (300,300) olarak aldık

cv2.imshow("img2",img2)
cv2.imshow("img1",img1)

dst = cv2.addWeighted(img1,0.1,img2,0.9, 0) #buradaki 0.7 ve 0.3 tuvalin yogunluklarıdır ve toplamları 1 olmak zorundadır girilen tuval degerlerinin
cv2.imshow("DST",dst) #iki resmi üst üste topladık


cv2.waitKey(0)
"""

#şimdi ve veya gibi mantıksal operatorleri resimlere uygulayacagız

img1 = np.zeros((400,400), dtype=np.uint8)
white = (255,255,255)
cv2.rectangle(img1,(75,75),(325,325),white,-1)


img2 = np.zeros((400,400), dtype=np.uint8)
cv2.circle(img2,(200,200),150,white,-1)


bitWiseAnd = cv2.bitwise_and(img1,img2)
bitWiseOr = cv2.bitwise_or(img1,img2)
bitWiseXor = cv2.bitwise_xor(img1,img2)
bitWiseNot = cv2.bitwise_not(img1,img2)

titles = ["Rectangle","Circle","Bitwise And","Bitwise Or","Bitwise Xor","Bitwise Not"]
images = [img1,img2,bitWiseAnd,bitWiseOr,bitWiseXor,bitWiseNot]

for i in range (6):
    plt.subplot(2,3,i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_RGB2BGR)) #plt.imshow görüntüleri rgb formatta görüntüler
    plt.title(titles[i])
    #x ve y koordinatlarındaki değerleri görmek istemedigimizin için alttaki iki komutu kullandık sadce resim görmek istiyoruz

    plt.xticks([])
    plt.yticks([])

plt.show()
#hepsini tek tek imshow ile görüntülemek yerine matplot kullanarak aynı pencere içerisinde görüntüleyecegiz

cv2.waitKey(0)

















