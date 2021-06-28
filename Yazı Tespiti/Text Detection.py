import cv2
import math

path = 'images.png'
img = cv2.imread(path)
pointsLists = []

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointsLists.append([x,y])
        print(pointsLists)
        #print(x,y)

def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getAngle(pointsLists):
    pt1,pt2,pt3 = pointsLists[-3:]
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1,pt3)
    angR = math.atan((m2-m1)/(1+m2*m1))
    angD = round(math.degrees(angR))
    print(angD)


while True:
    if len(pointsLists) %3 == 0 and len(pointsLists) != 0:
        getAngle(pointsLists)

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints)
    if  cv2.waitKey(1) % 0xFF == ord('q'):
        pointLists = []
        img = cv2.imread(path)

