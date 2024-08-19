import cv2
import numpy as np

image = cv2.imread("./data/lena.jpg")

# Print error message if image is null
if image is None:
    print('Could not read image')

# Apply identity kernel
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

# Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
blurring = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

images = np.hstack([image, identity, blurring])
cv2.imshow("result",images)
cv2.waitKey()
cv2.destroyAllWindows()
