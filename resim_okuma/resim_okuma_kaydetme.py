import cv2

img = cv2.imread("shrek.jpg") #resmi okuma fonk imread
cv2.imwrite("shrek1.jpg", img) #resmi istedigimiz dizine kaydeder

cv2.imshow("Pencere",img) #resmi görüntülemek için cv2.imshow fonk kullandık
cv2.waitKey(0) #actıgımız pencereyi ekranda tutmak için kullanılan fonk. 0 yazmak ben kapatana kadar acık tut demektir ms cinsinden
cv2.destroyAllWindows() #bütün acık pencereleri kapatmak

