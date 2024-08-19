import cv2
import numpy
import numpy as np


def draw_text(src: cv2.Mat, text: str, shape: numpy.shape = None):
    _shape = shape if shape is not None else src.shape
    cv2.putText(src, f"{text} {_shape}", (10, src.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255),
                thickness=2)


def sampling(src: cv2.Mat, scaler_x: float, scaler_y: float, inter: int, text: str) -> cv2.Mat:
    h, w = src.shape[0], src.shape[1]
    w1 = int(w * scaler_x)
    h1 = int(h * scaler_y)
    resize_image = cv2.resize(src, (w1, h1), interpolation=inter)

    # add padding if needed
    padding_left = int((w - w1)/2) if w > w1 else 0
    padding_right = w - padding_left - w1 if padding_left > 0 else 0
    padding_top = int((h - h1) / 2) if h > h1 else 0
    padding_bottom = h - padding_top - h1 if padding_top > 0 else 0

    image = cv2.copyMakeBorder(resize_image, padding_top, padding_bottom, padding_left, padding_right,
                               cv2.BORDER_CONSTANT)
    draw_text(image, text, resize_image.shape)
    return image


if __name__ == '__main__':

    img = cv2.imread("./data/baboon.jpg")
    h, w = img.shape[0], img.shape[1]
    fx, fy = 0.5,0.5  # 缩放倍率
    #
    # 1. 原始图像
    img1 = img.copy()
    if fx >1.0 or fy > 1.0:
        w1,h1 = int(w*fx),int(h*fy)
        padding_left = int((w1-w)/2) if  w1 > w else 0
        padding_right = w1 - padding_left - w if padding_left >0 else 0
        padding_top = int((h1-h)/2) if h1 > h else 0
        padding_bottom = h1 - padding_top - h if padding_top > 0 else 0
        img1 = cv2.copyMakeBorder(img1, padding_top, padding_bottom, padding_left, padding_right,
                                   cv2.BORDER_CONSTANT)
    draw_text(img1, "original")
    # 2. nearest
    img2 = sampling(img, fx, fy, cv2.INTER_NEAREST, "nearest")
    # 3. cubic 三次插值
    img3 = sampling(img, fx,fy,cv2.INTER_CUBIC,"cubic")
    # 4. area
    img4 = sampling(img, fx, fy, cv2.INTER_AREA, "area")
    # 5. linear
    img5 = sampling(img, fx, fy, cv2.INTER_LINEAR, "linear")
    # 6. lancos4
    img6 = sampling(img, fx, fy, cv2.INTER_LANCZOS4, "lancos4")

    images = np.vstack([
        np.hstack([img1,img2,img3]),
        np.hstack([img4,img5,img6])
    ])

    cv2.imwrite("Sampling Compare.jpg", images)
    cv2.imshow("Sampling Compare", images)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
