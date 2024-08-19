import cv2
import numpy as np

image = cv2.imread("./data/text.jpg", cv2.IMREAD_GRAYSCALE)

th, otsu = cv2.threshold(image, 0 ,255,type=cv2.THRESH_OTSU)
cv2.imshow(f"otsu-threshold:{th}", np.hstack([image, otsu]))
cv2.waitKey()
cv2.destroyAllWindows()