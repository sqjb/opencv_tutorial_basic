import cv2
import numpy as np

image = cv2.imread("./data/lena.jpg")

kernel3 = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])
sharp_img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel3)

images = np.hstack([image, sharp_img])
cv2.imshow('sharpening ', images)

cv2.waitKey()
cv2.destroyAllWindows()