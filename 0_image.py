import cv2 as cv2
import numpy

# 读取图像
image_path = "./data/messi5.jpg"  # 请替换为实际图像路径
image = cv2.imread(image_path)

# 检查图像是否成功读取
if image is None:
    print("无法读取图像，请检查路径。")
else:
    # # 获取某个像素点的值
    # x, y = 100, 150
    # pixel_value = image[y, x]
    #
    # # 打印图像信息
    # print("存储图片的数据结构为:", type(image))
    # print(f"图像大小：{image.shape}")
    # print(f"像素值（{x}, {y}）：{pixel_value}")
    #
    # # 显示图像
    # cv2.imshow('Image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    ch1 = image.copy()
    ch1[:, :, 1:3] = 0

    ch2 = image.copy()
    ch2[:, :, 0:3:2] = 0

    ch3 = image.copy()
    ch3[:, :, 0:2] = 0

    cv2.imshow("im1", ch1)
    cv2.imshow("im2", ch2)
    cv2.imshow("im3", ch3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
