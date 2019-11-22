# -*- coding: utf-8 -*-

# 以下是最常用的读取视频流的方法
import cv2

# 根据摄像头设置IP及rtsp端口
url = 'rtsp://32.91.106.12:554'

# 读取视频流
cap = cv2.VideoCapture(url)
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(frame.shape[0], frame.shape[1], frame.shape[2])
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
