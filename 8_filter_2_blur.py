import cv2
import numpy as np

image = cv2.imread("./data/lena.jpg")

# # customer
# kernel1 = np.ones((5, 5), np.float32) / 25
# im1 = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
#
# # blur()
# im2 = cv2.blur(src=image, ksize=(5, 5))
#
# print((im2 == im1).all())
#
# images = np.hstack([image, im1, im2])


# gaussian
# gb1 = cv2.GaussianBlur(src=image, ksize=(5, 5),
#                        sigmaX=0, sigmaY=0)
# gb2 = cv2.GaussianBlur(src=image, ksize=(5, 5),
#                        sigmaX=0.5, sigmaY=0)
# gb3 = cv2.GaussianBlur(src=image, ksize=(5, 5),
#                        sigmaX=1.5, sigmaY=0)
#
# images = np.hstack([image,gb1,gb2,gb3])

# median
median = cv2.medianBlur(src=image, ksize=5)
images = np.hstack([image, median])

cv2.imshow('gaussian blur', images)
cv2.waitKey()
cv2.destroyAllWindows()
