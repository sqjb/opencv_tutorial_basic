import cv2
import numpy as np

data = np.arange(0, 179, 10, dtype=np.uint8)
line = np.repeat(data, 20)
line = line.reshape(1, line.shape[0])
h = np.repeat(line, 400, axis=0)
s = np.zeros(h.shape, dtype=np.uint8)
v = np.zeros(h.shape, dtype=np.uint8)

image = np.stack([h, s, v], axis=2, dtype=np.uint8)
rgb = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)


def onchange_s(val):
    image[:,:,1] = val
    im1 = cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    cv2.imshow("test", im1)


def onchange_v(val):
    image[:, :, 2] = val
    im1 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.imshow("test", im1)


def onmouse(action, x, y, flag, data):
    vals = image[y, x].tolist()
    print(vals)


cv2.namedWindow("test")
cv2.createTrackbar("s", "test", 0, 255, onchange_s)
cv2.createTrackbar("v", "test", 0, 255, onchange_v)
cv2.setMouseCallback("test", onmouse)

cv2.imshow("test", rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
