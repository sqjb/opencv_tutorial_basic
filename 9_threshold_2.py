import cv2
import numpy as np

thresh = 150
maxVal = 255
image = cv2.imread("./data/text.jpg", cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, thresh, maxVal, cv2.THRESH_BINARY)
_, binary_inv = cv2.threshold(image, thresh, maxVal, cv2.THRESH_BINARY_INV)
_, trunc = cv2.threshold(image, thresh, maxVal, cv2.THRESH_TRUNC)
_, tozero = cv2.threshold(image, thresh, maxVal, cv2.THRESH_TOZERO)
_, tozero_inv = cv2.threshold(image, thresh, maxVal, cv2.THRESH_TOZERO_INV)


ims = np.vstack([np.hstack([image, binary, binary_inv]),
                 np.hstack([trunc, tozero, tozero_inv])])

cv2.namedWindow("compare",cv2.WINDOW_NORMAL)
cv2.imshow("compare", ims)
cv2.waitKey()
cv2.destroyAllWindows()
