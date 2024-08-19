import cv2

image = cv2.imread("./data/text.jpg", cv2.IMREAD_GRAYSCALE)
windowName = "adaptive thresholding"
blockSize = 11
parameter = 3
#method = cv2.ADAPTIVE_THRESH_MEAN_C
method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C


def updateBlockSize(*params):
    global blockSize
    blockSize = params[0]
    r1 = cv2.adaptiveThreshold(image, 255, method, cv2.THRESH_BINARY, blockSize, parameter)
    cv2.imshow(windowName, r1)


def updateParameter(*params):
    global parameter
    parameter = params[0]
    r2 = cv2.adaptiveThreshold(image, 255, method, cv2.THRESH_BINARY, blockSize, parameter)
    cv2.imshow(windowName, r2)


if __name__ == '__main__':
    cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
    r = cv2.adaptiveThreshold(image, 255, method, cv2.THRESH_BINARY, blockSize, parameter)
    cv2.createTrackbar("blocksize", windowName, blockSize, 100, updateBlockSize)
    cv2.createTrackbar("c", windowName, parameter, 255, updateParameter)
    cv2.imshow(windowName, r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
