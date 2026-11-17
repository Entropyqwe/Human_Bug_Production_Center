# ROS 2 Humble + PyTorch(CUDA) + Ultralytics YOLO 一体镜像
# 构建:  docker build -t humble-yolo .
# 运行见 README / 方案文档第 7 章
FROM ros:humble

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1

# ROS 侧工具 + 系统 OpenCV（rqt_image_view 用于可视化，image_tools 用于摄像头发布）
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-pip \
        python3-opencv \
        ros-humble-image-tools \
        ros-humble-rqt-image-view \
    && rm -rf /var/lib/apt/lists/*

# PyTorch CUDA 版（cu121 wheel 自带 CUDA 运行时，宿主机只需装好驱动）
RUN pip3 install --no-cache-dir \
        --index-url https://download.pytorch.org/whl/cu121 \
        torch torchvision torchaudio

# Ultralytics（含 YOLOv8 训练/推理/跟踪）
RUN pip3 install --no-cache-dir ultralytics

WORKDIR /ros2_ws
COPY yolo_node.py /ros2_ws/yolo_node.py
COPY video_publisher.py /ros2_ws/video_publisher.py

CMD ["bash"]
