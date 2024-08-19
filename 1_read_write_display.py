import cv2

if __name__ == '__main__':
    # img_path = "./data/food.png"
    #
    # # 默认
    # img_default = cv2.imread(img_path)
    # # 灰度
    # img_grayscale = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    # # 彩色
    # img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
    # # 保留透明度
    # img_unchanged = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    #
    #
    # # 不同的窗口画图
    # cv2.imshow(f"default, shape={img_default.shape}", img_default)
    # cv2.imshow(f"grayscale,shape={img_grayscale.shape}", img_grayscale)
    # cv2.imshow(f"color,shape={img_color.shape}", img_color)
    # cv2.imshow(f"unchanged,shape={img_unchanged.shape}", img_unchanged)
    #
    # # 写图片
    # # cv2.imwrite('test.jpg',img_grayscale)
    #

    image_default = cv2.imread("./data/food.png")
    image_unchanged = cv2.imread("./data/food.png", cv2.IMREAD_UNCHANGED)

    # 对比前三个通道数据是否相同
    bgr_compare = (image_default == image_unchanged[:, :, 0:3]).all()
    print(f"bgr通道对比结果: {bgr_compare}")

    alpha = image_unchanged[:,:,3] / 255

    image_unchanged[:, :, 0] = image_unchanged[:, :, 0] * alpha
    image_unchanged[:, :, 1] = image_unchanged[:, :, 1] * alpha
    image_unchanged[:, :, 2] = image_unchanged[:, :, 2] * alpha

    cv2.imshow(f"default,shape:{image_default.shape}", image_default)
    cv2.imshow(f"unchanged, shape:{image_unchanged.shape}", image_unchanged)
    while True:
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
    cv2.destroyAllWindows()
    print('quit normally..')
