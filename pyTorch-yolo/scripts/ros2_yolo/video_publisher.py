#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把本地视频文件循环发布到 /image_raw，供 yolo_node 离线测试。
用法: python3 video_publisher.py /datasets/test.mp4 --fps 15
"""
import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2


class VideoPub(Node):
    def __init__(self, path: str, fps: float):
        super().__init__('video_publisher')
        self.cap = cv2.VideoCapture(path)
        if not self.cap.isOpened():
            raise RuntimeError(f'无法打开视频: {path}')
        self.pub = self.create_publisher(Image, '/image_raw', 10)
        self.timer = self.create_timer(1.0 / fps, self.tick)
        self.get_logger().info(f'发布 {path} @ {fps} FPS → /image_raw（循环播放）')

    def tick(self):
        ok, frame = self.cap.read()
        if not ok:                                   # 播完回到开头
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            return
        msg = Image()
        msg.height, msg.width = frame.shape[:2]
        msg.encoding = 'bgr8'
        msg.step = msg.width * 3
        msg.data = frame.tobytes()
        msg.header.stamp = self.get_clock().now().to_msg()
        self.pub.publish(msg)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'test.mp4'
    fps = 15.0
    if '--fps' in sys.argv:
        fps = float(sys.argv[sys.argv.index('--fps') + 1])
    rclpy.init()
    node = VideoPub(path, fps)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
