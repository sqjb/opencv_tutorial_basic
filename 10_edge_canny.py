import cv2
import numpy as np

image = cv2.imread("./data/tiger.jpg", cv2.IMREAD_GRAYSCALE)
# canny
canny = cv2.Canny(image, 100, 200)
cv2.namedWindow("test", cv2.WINDOW_NORMAL)
cv2.imshow("test",np.hstack([image, canny]))
cv2.waitKey()
cv2.destroyAllWindows()
