import cv2
import numpy as np

image = cv2.imread("./data/objs.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = 100
canny_thr1 = 100
canny_thr2 = 200


def updateThreshold(*para):
    th = para[0]
    _, im = cv2.threshold(gray, th, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("binary image", im)


def updateThr1(*para):
    g = cv2.GaussianBlur(gray, (5, 5), sigmaX=0, sigmaY=0)
    c = cv2.Canny(g, para[0], canny_thr2)
    cv2.imshow("canny", c)


def updateThr2(*para):
    g = cv2.GaussianBlur(gray, (5, 5), sigmaX=0, sigmaY=0)
    c = cv2.Canny(g, canny_thr1, para[0])
    cv2.imshow("canny", c)


_, bim = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)
gau = cv2.GaussianBlur(gray,(5,5),sigmaX=0,sigmaY=0)
canny = cv2.Canny(gau, canny_thr1, canny_thr2)
contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
drawed = cv2.drawContours(image.copy(),contours, -1, (0,255,0), 2, hierarchy=hierarchy, maxLevel=1)
cv2.imshow("test", image)
cv2.imshow("gray", gray)
cv2.imshow("binary image", bim)
cv2.imshow("canny", canny)
cv2.imshow("drawed", drawed)
cv2.createTrackbar("threshold", "binary image", threshold, 255, updateThreshold)
cv2.createTrackbar("threshold1", "canny", canny_thr1, 255, updateThr1)
cv2.createTrackbar("threshold2", "canny", canny_thr2, 255, updateThr2)
cv2.waitKey(0), cv2.destroyAllWindows()
