import cv2
import numpy as np

image = cv2.imread("./data/objs.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def get_edge_and_contours(th1, th2):
    edge = cv2.Canny(gray, th1, th2)
    contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    drawed = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2, hierarchy=hierarchy, maxLevel=1)
    ims = np.hstack([
        np.stack([edge, edge, edge], axis=2),
        drawed
    ])
    return ims


def updateTh1(th1):
    th2 = cv2.getTrackbarPos("th2", "win")
    ims = get_edge_and_contours(th1, th2)
    cv2.imshow("win", ims)


def updateTh2(th2):
    th1 = cv2.getTrackbarPos("th1", "win")
    ims = get_edge_and_contours(th1, th2)
    cv2.imshow("win", ims)


cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.createTrackbar("th1", "win", 100, 255, updateTh1)
cv2.createTrackbar("th2", "win", 100, 255, updateTh2)

cv2.imshow("win", get_edge_and_contours(100, 200))
cv2.waitKey()
cv2.destroyAllWindows()
