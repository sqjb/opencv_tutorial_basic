import cv2
import matplotlib.pyplot as plt
image = cv2.imread("./data/text.jpg", cv2.IMREAD_GRAYSCALE)

if __name__ == '__main__':
    hist = cv2.calcHist([image],[0], None, [256],[0,255])
    # ostu directly..
    th1, r1 = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)


    plt.subplot(1,5,1), plt.title("original"), plt.imshow(image)
    plt.subplot(1, 5, 2), plt.title("hist"), plt.hist(image)
    plt.subplot(1, 5, 3), plt.title("cv2.hist"), plt.plot(hist)
    plt.subplot(1, 5, 4), plt.title(f"ostu {th1}"), plt.imshow(r1)
    plt.show()