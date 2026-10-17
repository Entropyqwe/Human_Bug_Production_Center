import cv2

tracker = cv2.legacy.TrackerKCF_create()
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
if not ret:
    print("无法读取摄像头！")
    cap.release()
    exit()


# selectROI 会返回一个元组 (x, y, w, h)
bbox = cv2.selectROI("Select Target", frame, fromCenter=False, showCrosshair=True)

tracker.init(frame, bbox)
cv2.destroyWindow("Select Target") 

print("跟踪开始！按 q 键退出。")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    success, bbox = tracker.update(frame)

    if success:
        # bbox 是浮点数，需要转成整数
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)
        cv2.putText(frame, "KCF Tracking", (p1[0], p1[1]-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost!", (100, 200), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("KCF Tracker", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()