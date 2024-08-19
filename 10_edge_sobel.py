import cv2
import numpy as np

image = cv2.imread("./data/tiger.jpg", cv2.IMREAD_GRAYSCALE)
edge = cv2.Sobel(image,ddepth=-1,dx=1,dy=1,ksize=3)

cv2.namedWindow("sobel", cv2.WINDOW_NORMAL)
cv2.imshow("sobel",np.hstack([image, edge]))
cv2.waitKey()
cv2.destroyAllWindows()