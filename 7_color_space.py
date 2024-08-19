import cv2
import numpy as np


def rgb():
    indoor = cv2.imread("./data/cube-indoor.png")
    outdoor = cv2.imread("./data/cube-outdoor.png")
    b, g, r = cv2.split(indoor)
    b1, g1, r1 = cv2.split(outdoor)
    cv2.imshow("indoor", indoor)
    cv2.imshow("B-in", b)
    cv2.imshow("G-in", g)
    cv2.imshow("R-in", r)
    cv2.imshow("outdoor", outdoor)
    cv2.imshow("B-out", b1)
    cv2.imshow("G-out", g1)
    cv2.imshow("R-out", r1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def lab():
    image = cv2.imread("./data/cube-outdoor.png")
    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(image_lab)
    cv2.imshow("original", image)
    cv2.imshow("L", l)
    cv2.imshow("A", a)
    cv2.imshow("B", b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ycbcr():
    image = cv2.imread("./data/cube-indoor.png")
    image_crcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(image_crcb)
    cv2.imshow("original", image)
    cv2.imshow("Y", y)
    cv2.imshow("Cr", cr)
    cv2.imshow("Cb", cb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def yuv():
    image = cv2.imread("./data/cube-indoor.png")
    image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(image_yuv)
    images = np.hstack([y, u, v])
    cv2.imshow("src",image)
    cv2.imshow("yuv", images)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def hsv():
    image = cv2.imread("./data/cube-indoor.png")
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(image_hsv)

    cv2.imshow("original", image)
    images = np.hstack([h, s, v])
    cv2.imshow("hsv", images)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    #rgb()
    #lab()
     yuv()
    # hsv()
    # hsv()
