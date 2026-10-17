"""摄像头手部关键点与骨架显示。按 Q / Esc 退出。"""
import argparse
from pathlib import Path
import time

import cv2
import mediapipe as mp


# 手腕、五根手指与掌部的连接关系，编号对应模型的 21 个关键点。
CONNECTIONS = (
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (0, 17), (17, 18), (18, 19), (19, 20),
)
MODEL = Path(__file__).resolve().with_name("hand_landmarker.task")


def draw_hands(frame, result):
    """将每只手的骨架画在摄像头画面上。"""
    height, width = frame.shape[:2]
    for landmarks in result.hand_landmarks:
        points = [
            (max(0, min(width - 1, int(p.x * width))),
             max(0, min(height - 1, int(p.y * height))))
            for p in landmarks
        ]
        for start, end in CONNECTIONS:
            cv2.line(frame, points[start], points[end], (0, 220, 0), 3, cv2.LINE_AA)
        for index, point in enumerate(points):
            color = (0, 100, 255) if index in (4, 8, 12, 16, 20) else (0, 255, 255)
            cv2.circle(frame, point, 5, color, -1, cv2.LINE_AA)


def main():
    parser = argparse.ArgumentParser(description="摄像头手部骨架显示")
    parser.add_argument("--camera", type=int, default=0, help="摄像头编号，默认 0")
    parser.add_argument("--check", action="store_true", help="检查模型，无需打开摄像头")
    args = parser.parse_args()

    if not MODEL.is_file():
        raise SystemExit("缺少模型：请将 hand_landmarker.task 放在本程序旁边。")

    options = mp.tasks.vision.HandLandmarkerOptions(
        base_options=mp.tasks.BaseOptions(model_asset_path=str(MODEL)),
        running_mode=mp.tasks.vision.RunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5,
    )
    with mp.tasks.vision.HandLandmarker.create_from_options(options) as detector:
        if args.check:
            import numpy as np
            blank = np.zeros((480, 640, 3), dtype=np.uint8)
            result = detector.detect_for_video(
                mp.Image(image_format=mp.ImageFormat.SRGB, data=blank), 0
            )
            draw_hands(blank, result)
            print("检查通过：模型加载、图像推理及绘制函数运行正常。")
            return

        cap = cv2.VideoCapture(args.camera)
        try:
            if not cap.isOpened():
                raise SystemExit("无法打开摄像头，请检查权限或使用 --camera 1。")
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            window = "Hand skeleton - Q to quit"
            cv2.namedWindow(window, cv2.WINDOW_NORMAL)
            last_timestamp = -1
            print("将手放在摄像头前即可显示骨架；按 Q 或 Esc 退出。")
            while True:
                ok, frame = cap.read()
                if not ok:
                    print("摄像头读取失败。")
                    break
                frame = cv2.flip(frame, 1)
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
                timestamp = max(last_timestamp + 1, time.monotonic_ns() // 1_000_000)
                last_timestamp = timestamp
                result = detector.detect_for_video(image, timestamp)
                draw_hands(frame, result)
                cv2.putText(frame, f"Hands: {len(result.hand_landmarks)} | Q: quit",
                            (12, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                            (255, 255, 255), 2, cv2.LINE_AA)
                cv2.imshow(window, frame)
                if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q"), 27):
                    break
                if cv2.getWindowProperty(window, cv2.WND_PROP_VISIBLE) < 1:
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
