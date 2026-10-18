import cv2

cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cap=cv2.VideoCapture(0)

# 先读取第一帧，使用摄像头实际尺寸创建视频文件
ret,frame=cap.read()
height = frame.shape[0]
width = frame.shape[1]
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
vw=cv2.VideoWriter(r'C:\Users\23832\Desktop\out.avi',fourcc,25,(width,height))
if not vw.isOpened():
    print('视频文件创建失败')
    cap.release()
    exit()

#获取视频设备
    #从摄像头读取视频帧，后面的read会返回两个值，一个是状态，一个是帧数
while True:
    if not ret:
        print('读取视频帧失败')
        break
#将视频在窗口中展示
    cv2.imshow('Video',frame)
    #再设定一次尺寸，例子：cv2,resizewinndow('video),640*480
    vw.write(frame)
    key=cv2.waitKey(24)#不可以使用0，不然就不循环了（括号内是毫秒）
    if(key&0xFF==ord('q')):
        break
    ret,frame=cap.read()
#释放Capture
cap.release()
vw.release()
cv2.destroyAllWindows()
print('视频已保存到桌面：out.avi')
