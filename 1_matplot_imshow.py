from PIL import Image
import matplotlib.pyplot as plt

img_rgb = Image.open('./data/food.png').convert("RGB")
img_rgba = Image.open("./data/food.png")
plt.subplot(1, 2, 1), plt.imshow(img_rgb)
plt.subplot(1, 2, 2), plt.imshow(img_rgba)
plt.show()
