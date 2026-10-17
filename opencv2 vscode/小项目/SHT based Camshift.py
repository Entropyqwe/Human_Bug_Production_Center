import cv2
import numpy as np

# 打开摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头")
    raise SystemExit

# 读取第一帧，用鼠标框选头部
ret, frame = cap.read()
if not ret:
    print("无法读取摄像头画面")
    cap.release()
    raise SystemExit

cv2.namedWindow("Select head", cv2.WINDOW_NORMAL)
roi = cv2.selectROI("Select head", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select head")

x, y, w, h = roi
if w == 0 or h == 0:
    print("没有选择跟踪区域")
    cap.release()
    cv2.destroyAllWindows()
    raise SystemExit

# 保存选中的头部区域，并建立颜色直方图
track_window = (x, y, w, h)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
roi_hsv = hsv[y:y + h, x:x + w]

mask = cv2.inRange(
    roi_hsv,
    np.array((0., 30., 20.)),
    np.array((180., 255., 255.))
)
roi_hist = cv2.calcHist([roi_hsv], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# CamShift 参数
term_crit = (
    cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
    10,
    1
)

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法读取摄像头画面")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    back_project = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # 根据颜色分布估计头部的新位置
    ret_box, track_window = cv2.CamShift(
        back_project,
        track_window,
        term_crit
    )

    # 画出跟踪框
    points = cv2.boxPoints(ret_box)
    points = np.intp(points)
    cv2.polylines(frame, [points], True, (0, 255, 0), 2)
    cv2.putText(
        frame,
        "Head tracking - press q to quit",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.imshow("Head tracking", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
