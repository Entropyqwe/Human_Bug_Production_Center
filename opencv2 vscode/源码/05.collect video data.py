import cv2

cv2.namedWindow('video',cv2.WINDOW_NORMAL)
#获取视频设备
cap=cv2.VideoCapture(0)
#建立视频循环
while True:
    #从摄像头读取视频帧，后面的read会返回两个值，一个是状态，一个是帧数
    ret,frame=cap.read()
#将视频在窗口中展示
    cv2.imshow('Video',frame)
    key=cv2.waitKey(1)#不可以使用0，不然就不循环了（括号内是毫秒）
    if(key&0xFF==ord('q')):
        break
#释放Capture
cap.release()
cv2.destroyAllWindows()