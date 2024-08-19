import cv2

image = cv2.imread("./data/food.png", cv2.IMREAD_UNCHANGED)

# 保存为 jpeg
cv2.imwrite("./data/food.jpeg", image)
cv2.imwrite("./data/food-10.jpeg", image,[cv2.IMWRITE_JPEG_QUALITY, 10])

# 保存为 png
cv2.imwrite("./data/food1.png", image, )
cv2.imwrite("./data/food1-10.png", image, [cv2.IMWRITE_PNG_COMPRESSION, 10])

# webp
cv2.imwrite("./data/food.webp", image)
cv2.imwrite("./data/food-10.webp",image,[cv2.IMWRITE_WEBP_QUALITY, 10])
