import cv2
import numpy as np

image = cv2.imread("./data/lena.jpg")

bilateral_filter = cv2.bilateralFilter(src=image, d=9, sigmaColor=75, sigmaSpace=75)
ims = np.hstack([image, bilateral_filter])
cv2.imshow("test",ims)
cv2.waitKey(0)
cv2.destroyAllWindows()