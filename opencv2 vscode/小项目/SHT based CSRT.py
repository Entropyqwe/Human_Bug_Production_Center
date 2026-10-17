import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头")
    raise SystemExit

# 读取第一帧
ret, frame = cap.read()
if not ret:
    print("无法读取摄像头画面")
    cap.release()
    raise SystemExit

# 手动框选头部
cv2.namedWindow("Select head", cv2.WINDOW_NORMAL)
print("请用鼠标框选头部，然后按 Enter 或 Space 确认")
box = cv2.selectROI("Select head", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select head")

x, y, w, h = [int(v) for v in box]
if w <= 0 or h <= 0:
    print("没有选择有效区域")
    cap.release()
    cv2.destroyAllWindows()
    raise SystemExit

tracker = None
tracker_name = ""

if hasattr(cv2, "TrackerCSRT_create"):
    tracker = cv2.TrackerCSRT_create()
    tracker_name = "CSRT"
elif hasattr(cv2, "legacy") and hasattr(cv2.legacy, "TrackerCSRT_create"):
    tracker = cv2.legacy.TrackerCSRT_create()
    tracker_name = "CSRT"
elif hasattr(cv2, "TrackerKCF_create"):
    tracker = cv2.TrackerKCF_create()
    tracker_name = "KCF"
elif hasattr(cv2, "legacy") and hasattr(cv2.legacy, "TrackerKCF_create"):
    tracker = cv2.legacy.TrackerKCF_create()
    tracker_name = "KCF"
else:
    print("当前 OpenCV 没有 CSRT/KCF 跟踪器。请安装：")
    print("python -m pip install opencv-contrib-python")
    cap.release()
    raise SystemExit

tracker.init(frame, (x, y, w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法读取摄像头画面")
        break

    ok, box = tracker.update(frame)

    if ok:
        x, y, w, h = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            f"Tracking: {tracker_name}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )
    else:
        cv2.putText(
            frame,
            "Tracking lost - press r to select again",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

    cv2.putText(
        frame,
        "q: quit   r: reselect head",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )
    cv2.imshow("Head tracking", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("r"):
        # 目标丢失或框选不准时，可以重新选择头部
        cv2.destroyWindow("Head tracking")
        cv2.namedWindow("Select head", cv2.WINDOW_NORMAL)
        new_box = cv2.selectROI("Select head", frame, fromCenter=False, showCrosshair=True)
        cv2.destroyWindow("Select head")
        nx, ny, nw, nh = [int(v) for v in new_box]
        if nw > 0 and nh > 0:
            tracker = cv2.TrackerCSRT_create() if hasattr(cv2, "TrackerCSRT_create") else cv2.legacy.TrackerCSRT_create()
            tracker.init(frame, (nx, ny, nw, nh))

cap.release()
cv2.destroyAllWindows()
