from PIL import Image
import cv2
# image = Image.open("./data/food.png")
# image.show()

image = cv2.imread("./data/food.png",cv2.IMREAD_UNCHANGED)
image_rgba = Image.fromarray(cv2.cvtColor(image,code=cv2.COLOR_BGRA2RGBA))
image_rgba.show()