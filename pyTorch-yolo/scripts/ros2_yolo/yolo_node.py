# ROS2 Humble + YOLOv8 检测节点（不依赖 cv_bridge，避免 pip/OpenCV 版本冲突）
#
# 订阅: /image_raw (sensor_msgs/Image)
# 发布: /yolo/image_annotated (带框图像)  /yolo/detections (文本摘要)
#
# 运行（容器内）:
#   python3 yolo_node.py --ros-args -p model_path:=/models/best.pt -p conf:=0.3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from ultralytics import YOLO
import numpy as np


class YoloNode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.declare_parameter('model_path', 'yolov8n.pt')
        self.declare_parameter('conf', 0.25)
        self.declare_parameter('save_video', '')   # 非空则保存带框视频（无 GUI 也能验收）

        model_path = self.get_parameter('model_path').get_parameter_value().string_value
        self.conf = self.get_parameter('conf').get_parameter_value().double_value
        self.save_path = self.get_parameter('save_video').get_parameter_value().string_value

        self.model = YOLO(model_path)
        self.writer = None
        self.pub_img = self.create_publisher(Image, '/yolo/image_annotated', 10)
        self.pub_det = self.create_publisher(String, '/yolo/detections', 10)
        self.sub = self.create_subscription(Image, '/image_raw', self.on_image, 10)
        self.get_logger().info(f'YOLO 节点就绪 | model={model_path} conf={self.conf}')

    def on_image(self, msg: Image):
        # 手动转换，不用 cv_bridge（pip 的 opencv 与系统 opencv 版本易冲突）
        frame = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1)
        if msg.encoding in ('rgb8', 'rgb'):       # 统一成 BGR（ultralytics/OpenCV 约定）
            frame = frame[:, :, ::-1].copy()

        results = self.model(frame, conf=self.conf, verbose=False)
        r = results[0]
        annotated = r.plot()                       # BGR ndarray

        det = ';'.join(
            f'{self.model.names[int(c)]}:{float(s):.2f}'
            for c, s in zip(r.boxes.cls, r.boxes.conf)
        )
        self.pub_det.publish(String(data=det))

        out = Image()
        out.header.stamp = msg.header.stamp
        out.header.frame_id = msg.header.frame_id
        out.height, out.width = annotated.shape[:2]
        out.encoding = 'bgr8'
        out.step = out.width * 3
        out.data = annotated.tobytes()
        self.pub_img.publish(out)

        if self.save_path:
            import cv2
            if self.writer is None:
                self.writer = cv2.VideoWriter(
                    self.save_path, cv2.VideoWriter_fourcc(*'mp4v'), 25.0,
                    (out.width, out.height))
            self.writer.write(annotated)


def main():
    rclpy.init()
    node = YoloNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
