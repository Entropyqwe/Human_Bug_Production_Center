import cv2

print("正在打开摄像头……")
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:

    if not cap.isOpened():
        print("摄像头打开失败")
    else:
        print("摄像头已打开，正在读取画面……")
        ret, frame = cap.read()
        if ret:
            print(f"读取成功，画面尺寸：{frame.shape}")
            cv2.imshow("Camera", frame)
            key=cv2.waitKey(24)#不可以使用0，不然就不循环了（括号内是毫秒）
            if(key&0xFF==ord('q')):
                    break
cv2.destroyAllWindows()

