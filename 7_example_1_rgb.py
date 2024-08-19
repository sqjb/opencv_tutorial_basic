import cv2
import numpy as np

image = cv2.imread("./data/cd.jpg")
image1 = cv2.resize(image, (800, 600))
image_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)


def onchange_val(r):
    im1 = np.stack([image_gray, image_gray, image_gray], axis=2)
    bgr_min = np.array([
        cv2.getTrackbarPos("B-min", "seg"),
        cv2.getTrackbarPos("G-min", "seg"),
        cv2.getTrackbarPos("R-min", "seg"),
    ])
    bgr_max = np.array([
        cv2.getTrackbarPos("B-max", "seg"),
        cv2.getTrackbarPos("G-max", "seg"),
        cv2.getTrackbarPos("R-max", "seg"),
    ])
    mask = cv2.inRange(image1, bgr_min, bgr_max)
    for c in range(3):
        im1[:, :, c] = np.where(mask == 255, image1[:, :, c], im1[:, :, c])
    cv2.imshow("seg", im1)


def onchange_start(val):
    if val == 1:
        im1 = np.stack([image_gray, image_gray, image_gray], axis=2)
        bgr_min = np.array([
            cv2.getTrackbarPos("B-min", "seg"),
            cv2.getTrackbarPos("G-min", "seg"),
            cv2.getTrackbarPos("R-min", "seg"),
        ])
        bgr_max = np.array([
            cv2.getTrackbarPos("B-max", "seg"),
            cv2.getTrackbarPos("G-max", "seg"),
            cv2.getTrackbarPos("R-max", "seg"),
        ])
        mask = cv2.inRange(image1, bgr_min, bgr_max)
        for c in range(3):
            im1[:, :, c] = np.where(mask == 255, image1[:, :, c], im1[:, :, c])
        cv2.imshow("seg", im1)
    elif val == 0:
        cv2.imshow("seg", image1)
    else:
        print("error")


def refresh():
    image_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    im1 = np.stack([image_gray, image_gray, image_gray], axis=2)
    bgr_min = np.array([
        cv2.getTrackbarPos("B-min", "seg"),
        cv2.getTrackbarPos("G-min", "seg"),
        cv2.getTrackbarPos("R-min", "seg"),
    ])
    bgr_max = np.array([
        cv2.getTrackbarPos("B-max", "seg"),
        cv2.getTrackbarPos("G-max", "seg"),
        cv2.getTrackbarPos("R-max", "seg"),
    ])
    mask = cv2.inRange(image1, bgr_min, bgr_max)
    for c in range(3):
        im1[:, :, c] = np.where(mask == 1, image1[:, :, c], im1[:, :, c])


cv2.namedWindow("seg", flags=cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("R-min", "seg", 0, 255, onchange_val)
cv2.createTrackbar("R-max", "seg", 0, 255, onchange_val)
cv2.createTrackbar("G-min", "seg", 0, 255, onchange_val)
cv2.createTrackbar("G-max", "seg", 0, 255, onchange_val)
cv2.createTrackbar("B-min", "seg", 0, 255, onchange_val)
cv2.createTrackbar("B-max", "seg", 0, 255, onchange_val)
cv2.createTrackbar("start", "seg", 0, 1, onchange_start)
cv2.setMouseCallback("seg", on_mouse_click)
cv2.imshow("seg", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
