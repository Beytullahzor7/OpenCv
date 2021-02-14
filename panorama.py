import cv2
import os

mainFolder = 'Images/Images'
myFolders = os.listdir(mainFolder)
print(myFolders)

for folder in myFolders:
    path = mainFolder + '/' + folder
    images = []
    myList = os.listdir(path)
    print(f' Total no of images  detected {len(myList)}')
    for imgName in myList:
        currentImg = cv2.imread(f'{path}/{imgName}')
        currentImg = cv2.resize(currentImg,(0,0),None,0.2,0.2)
        images.append(currentImg)

    stitcher = cv2.Stitcher.create()
    (status,result) = stitcher.stitch(images)

    if (status == cv2.Stitcher_OK):
        print('Panorama Oluşturuldu!')
        cv2.imshow(folder,result)
        cv2.waitKey(1)
    else:
        print('Panorama Oluşturulamadı!')

cv2.waitKey(0)
