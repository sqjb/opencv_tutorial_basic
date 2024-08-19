import cv2
import numpy as np


image = cv2.imread("./data/xp.png", cv2.IMREAD_GRAYSCALE)
r, im = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("test", np.hstack([image, im]))
cv2.waitKey(0)
cv2.destroyAllWindows()
