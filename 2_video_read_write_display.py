import cv2


# 视频读取和播放
def read_and_display():
    # 创建videocapture 对象
    vid_capture = cv2.VideoCapture('data/Megamind.avi')

    if not vid_capture.isOpened():
        print("Error opening the video file")
    else:
        # 获取视频的FPS
        fps = vid_capture.get(cv2.CAP_PROP_FPS)
        print('Frames per second : ', fps, 'FPS')

        # 获取视频帧数
        frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
        print('Frame count : ', frame_count)

        while True:
            # 读取视频帧
            ret, frame = vid_capture.read()
            if ret:
                cv2.imshow('Frame', frame)
                key = cv2.waitKey(int(1 / fps * 1000))

                if key == ord('q'):
                    break
            else:
                break

    # 内存释放
    vid_capture.release()
    cv2.destroyAllWindows()


# 视频编码与保存
def video_write():
    # 创建videocapture 对象
    vid_capture = cv2.VideoCapture('data/Megamind.avi')

    if not vid_capture.isOpened():
        print("Error opening the video file")
    else:
        # 获取视频帧的size
        frame_width = int(vid_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(vid_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_size = (frame_width, frame_height)
        fps = 20



        # MJPG -> avi
        fourcc = cv2.VideoWriter.fourcc(*'MPG4')

        # 创建 writer对象
        output = cv2.VideoWriter('test.avi', fourcc, fps, frame_size)

        while True:
            # 读取视频帧
            ret, frame = vid_capture.read()
            if ret:
                output.write(frame)
            else:
                break

    # 内存释放
    vid_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # 读取和播放
    # read_and_display()

    # 写视频
    video_write()
