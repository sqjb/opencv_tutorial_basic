import cv2
import numpy as np

image = cv2.imread("./data/ts.png")
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
h_filter_1 = [0, 30]
h_filter_2 = [150, 179]


def onchange_val(r):
    im1 = refresh()
    cv2.imshow("seg", np.hstack([image,im1]))


def onchange_start(val):
    if val == 1:
        im1 = np.stack([image_gray, image_gray, image_gray], axis=2)
        cv2.imshow("seg", np.hstack([image,im1]))
    elif val == 0:
        cv2.imshow("seg", np.hstack([image,image]))
    else:
        print("error")


def refresh():
    im1 = np.stack([image_gray, image_gray, image_gray], axis=2)
    h1_min = cv2.getTrackbarPos("h1-min","seg")
    h1_max = cv2.getTrackbarPos("h1-max", "seg")
    h2_min = cv2.getTrackbarPos("h2-min", "seg")
    h2_max = cv2.getTrackbarPos("h2-max", "seg")
    s_min = cv2.getTrackbarPos("s-min", "seg")
    s_max = cv2.getTrackbarPos("s-max", "seg")
    v_min = cv2.getTrackbarPos("v-min", "seg")
    v_max = cv2.getTrackbarPos("v-max", "seg")

    h1_low = np.array([h1_min, s_min, v_min])
    h1_high = np.array([h1_max, s_max, v_max])
    mask_1 = cv2.inRange(image_hsv, h1_low, h1_high)

    h2_low = np.array([h2_min, s_min, v_min])
    h2_high = np.array([h2_max, s_max, v_max])
    mask_2 = cv2.inRange(image_hsv, h2_low, h2_high)

    mask = mask_1 + mask_2
    for c in range(3):
        im1[:, :, c] = np.where(mask == 255, image[:, :, c], im1[:, :, c])
    return im1.copy()


cv2.namedWindow("seg", flags=cv2.WINDOW_NORMAL)
cv2.createTrackbar("h1-min", "seg", 0, 179, onchange_val)
cv2.createTrackbar("h1-max", "seg", 0, 179, onchange_val)
cv2.createTrackbar("h2-min", "seg", 0, 179, onchange_val)
cv2.createTrackbar("h2-max", "seg", 0, 179, onchange_val)
cv2.createTrackbar("s-min", "seg", 0, 255, onchange_val)
cv2.createTrackbar("s-max", "seg", 0, 255, onchange_val)
cv2.createTrackbar("v-min", "seg", 0, 255, onchange_val)
cv2.createTrackbar("v-max", "seg", 0, 255, onchange_val)
cv2.createTrackbar("start", "seg", 0, 1, onchange_start)
cv2.imshow("seg", np.hstack([image,image]))
cv2.waitKey(0)
cv2.destroyAllWindows()
