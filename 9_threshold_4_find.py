import cv2
import numpy as np

window_name = "find"
image = cv2.imread("./data/text.jpg", cv2.IMREAD_GRAYSCALE)


def find_threshold(thres):
    _, bin = cv2.threshold(image, thres, 255, type=cv2.THRESH_BINARY)
    cv2.imshow(window_name, np.hstack([image, bin]))

cv2.imshow(window_name, np.hstack([image, image]))
cv2.createTrackbar("threshold", window_name, 0, 255, find_threshold)
cv2.waitKey()
cv2.destroyAllWindows()
