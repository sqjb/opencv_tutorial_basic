import cv2

if __name__ == '__main__':
    image_path = './data/messi5.jpg'
    image = cv2.imread(image_path)
    h, w = image.shape[0], image.shape[1]
    #
    # 画线
    cv2.line(image,(0,0),(100,100),(0,0,255),thickness=3)

    # 画圆
    center = (50, int(h/2))
    cv2.circle(image, center, 50, (0,255,0), thickness=3)

    # 实心圆
    center1 = (150, int(h/2))
    cv2.circle(image, center1, 50, (255,0,0), thickness=-1)

    # 矩形
    rec_p1 = (200,int(h/2)-50)
    rec_p2 = (300,int(h/2)+50)
    cv2.rectangle(image,rec_p1,rec_p2,(255,255,0), thickness=2)

    # 椭圆
    cv2.ellipse(image,(350, int(h/2)), (50,30),0,0,360,(0,255,255),3)

    # 半圆
    cv2.ellipse(image,(450, int(h/2)), (50,30),20,180,360,(0,0,255),-1)

    # 文字
    cv2.putText(image, "i am Messi!!!", (10, h-10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), thickness=3)

    cv2.imshow("annotation", image)
    cv2.waitKey(0)