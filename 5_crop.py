import cv2
if __name__ == '__main__':
    image = cv2.imread("./data/flower.webp")
    cropped = image[80:280,120:350]
    cv2.putText(image,f"original {image.shape}", (10, image.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX, 0.5 ,
                color=(0,255,0), thickness=2)
    cv2.putText(cropped, f"cropped {cropped.shape}", (10, cropped.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.1,
                color=(0, 255, 0), thickness=2)
    cv2.imshow(f"original {image.shape}", image)
    cv2.imshow(f"cropped {cropped.shape}", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()