import cv2
import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
    image = cv2.imread("./data/cube-outdoor.png")
    # 选取过滤颜色
    bgr = [40, 158, 16]
    threshold = 35

    # BGR
    minBGR = np.array(bgr) - threshold
    maxBGR = np.array(bgr) + threshold
    maskBGR = cv2.inRange(image, minBGR, maxBGR)
    resultBGR = cv2.bitwise_and(image, image, mask=maskBGR)

    # HSV
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]
    minHSV = np.array([hsv[0]-threshold, hsv[1]-threshold, hsv[2]-threshold])
    maxHSV = np.array([hsv[0]+threshold, hsv[1]+threshold, hsv[2]+threshold])
    maskHSV = cv2.inRange(imageHSV, minHSV, maxHSV)
    resultHSV = cv2.bitwise_and(imageHSV, imageHSV, mask=maskHSV)
    resultHSV2BGR = cv2.cvtColor(resultHSV, cv2.COLOR_HSV2BGR)

    # ycb
    imageYCB = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    ycb = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2YCrCb)[0][0]
    minYCB = np.array([ycb[0]-threshold, ycb[1]-threshold, ycb[2]-threshold])
    maxYCB = np.array([ycb[0]+threshold, ycb[1]+threshold, ycb[2]+threshold])
    maskYCB = cv2.inRange(imageYCB, minYCB, maxYCB)
    resultYCB = cv2.bitwise_and(imageYCB, imageYCB, mask=maskYCB)
    resultYCB2BGR = cv2.cvtColor(resultYCB, cv2.COLOR_YCrCb2BGR)

    # lab
    imageLAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lab = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2LAB)
    minLAB = np.array(lab, dtype=np.int32) - threshold
    maxLAB = np.array(lab, dtype=np.int32) + threshold
    maskLAB = cv2.inRange(imageLAB, minLAB, maxLAB)
    resultLAB = cv2.bitwise_and(imageLAB, imageLAB, mask=maskLAB)
    resultLAB2BGR = cv2.cvtColor(resultLAB, cv2.COLOR_LAB2BGR)

    images = np.hstack([resultBGR, resultHSV, resultYCB, resultLAB])
    cv2.imshow("result", images)
    cv2.waitKey()
    cv2.destroyAllWindows()
