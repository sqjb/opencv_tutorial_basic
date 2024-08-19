import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 原图
    image = cv2.imread("./data/messi5.jpg")
    h, w = image.shape[:2]

    # rotation
    M = cv2.getRotationMatrix2D((w / 2, h / 2), 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))

    # rotation with scaler = 1.2
    M = cv2.getRotationMatrix2D((w / 2, h / 2), 45, 1.5)
    rotated_scaler = cv2.warpAffine(image, M, (w, h))

    # resize
    resized = cv2.resize(image, (w, h), None, fx=0.5, fy=0.8, interpolation=cv2.INTER_LINEAR)

    # 平移 translation
    M = np.float32([
        [1, 0, 50],
        [0, 1, -30]
    ])
    translated = cv2.warpAffine(image, M, (w, h))

    # shear
    pts1 = np.float32([[0, h], [w, h], [w, 0]])
    pts2 = np.float32([[0, h], [w, h], [w + 50, 0]])
    M = cv2.getAffineTransform(pts1, pts2)
    sheared = cv2.warpAffine(image, M, (int(w * 1.5), int(h * 1.5)))

    # shear + translation
    pts1 = np.float32([[0, h], [w, h], [w, 0]])
    pts2 = np.float32([[0, h + 50], [w, h + 50], [w + 50, 50]])
    M = cv2.getAffineTransform(pts1, pts2)
    shear_translation = cv2.warpAffine(image, M, (int(w * 1.5), int(h * 1.5)))

    # reflection
    M = np.float32([
        [-1, 0, w],
        [0, 1, 0]
    ])
    reflection_x = cv2.warpAffine(image, M, (w, h))

    # reflection
    M = np.float32([
        [1, 0, 0],
        [0, -1, h]
    ])
    reflection_y = cv2.warpAffine(image, M, (w, h))

    # 绘制
    plt.subplot(3, 3, 1), plt.title('original'), plt.imshow(image)
    plt.subplot(3, 3, 2), plt.title("rotate,angle=45"), plt.imshow(rotated)
    plt.subplot(3, 3, 3), plt.title("rotate,fx,fy=1.5"), plt.imshow(rotated_scaler)
    plt.subplot(3, 3, 4), plt.title("scale,fx=0.5,fy=0.8"), plt.imshow(resized)
    plt.subplot(3, 3, 5), plt.title("translation (50,-30)"), plt.imshow(translated)
    plt.subplot(3, 3, 6), plt.title("shear"), plt.imshow(sheared)
    plt.subplot(3, 3, 7), plt.title("shear and translation"), plt.imshow(shear_translation)
    plt.subplot(3, 3, 8), plt.title("reflection for x-axis"), plt.imshow(reflection_x)
    plt.subplot(3, 3, 9), plt.title("reflection for y-axis"), plt.imshow(reflection_y)

    plt.show()
