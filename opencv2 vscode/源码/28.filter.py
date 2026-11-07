import cv2 as cv
import numpy as np

# =====================
# 1. 生成一张测试图
# =====================
# 创建一个 300x400 的灰度图，背景是黑色
img = np.zeros((300, 400), dtype=np.uint8)

# 画一个白色矩形，模拟一个规则物体
cv.rectangle(img, (80, 60), (320, 240), 255, -1)

# 画一个白色圆形，方便观察边缘是否被模糊
cv.circle(img, (200, 150), 70, 255, -1)

# 2. 添加椒盐噪声
# 椒盐噪声：图像中随机出现纯黑(0)或纯白(255)的噪点
# 它常由传感器异常、传输错误等引起
prob = 0.05  # 噪声比例，5% 的像素会被污染
noisy_sp = img.copy()

# 生成随机掩码：True 表示这个位置要加噪声
mask = np.random.rand(*img.shape) < prob

# 一半位置变成白点（盐），一半变成黑点（椒）
salt_mask = mask & (np.random.rand(*img.shape) > 0.5)
pepper_mask = mask & ~salt_mask

noisy_sp[salt_mask] = 255    # 盐噪声：白点
noisy_sp[pepper_mask] = 0    # 椒噪声：黑点

# 3. 添加高斯噪声
# 高斯噪声：每个像素都叠加一个服从高斯分布的随机值，实际上是因为某些传感器噪声或光照变化引起的
# 它更接近真实相机传感器噪声
img_float = img.astype(np.float64)
noise = np.random.normal(0, 25, img.shape)  # 均值0，标准差25
noisy_gauss = img_float + noise

# 像素值必须限制在 0~255
noisy_gauss = np.clip(noisy_gauss, 0, 255).astype(np.uint8)


# 4. 均值滤波
# 原理：用邻域像素的平均值替代中心像素
# 优点：简单、快
# 缺点：容易把边缘也一起模糊掉
mean_filter = cv.blur(noisy_sp, (5, 5))
#滤波核大小 (5,5) 表示邻域是 5x5 的方形区域，必须是奇数

# 5. 高斯滤波（自然过渡）
# 原理：邻域加权平均，离中心越近的像素权重越大
# 比均值滤波更自然，是最常用的平滑滤波
gaussian_filter = cv.GaussianBlur(noisy_gauss, (5, 5), 0)
# 参数 (5,5) 是核大小，必须是奇数
# 第三个参数 0 表示 OpenCV 自动计算标准差

# 6. 中值滤波（针对极端性）
# 原理：取邻域像素的中值替代中心像素
# 对椒盐噪声效果最好，因为极端黑白点会被排序后剔除
median_filter = cv.medianBlur(noisy_sp, 5)
# 核大小 5 必须是奇数：3、5、7、9...，是相乘形式的矩阵


# 7. 双边滤波
# 原理：同时考虑空间距离和像素相似度
# 能在去噪的同时尽量保留边缘，但速度较慢
bilateral_filter = cv.bilateralFilter(noisy_gauss, 9, 75, 75)
# 9：邻域直径
# 75：颜色相似度阈值，越大允许更多不同颜色参与
# 75：空间距离阈值，越大滤波范围越广

# =====================
# 8. 自定义卷积核：锐化
# =====================
# 滤波不一定是模糊，也可以增强边缘
# 这个核会增强中心像素，削弱周围像素，从而锐化图像
sharpen_kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
], dtype=np.float32)

sharpened = cv.filter2D(noisy_gauss, -1, sharpen_kernel)
# -1 表示输出图像深度与原图相同

# =====================
# 9. 显示结果
# =====================
cv.imshow("Original", img)
cv.imshow("Salt & Pepper Noise", noisy_sp)
cv.imshow("Gaussian Noise", noisy_gauss)
cv.imshow("Mean Filter (on SP)", mean_filter)
cv.imshow("Gaussian Filter (on Gauss)", gaussian_filter)
cv.imshow("Median Filter (on SP)", median_filter)
cv.imshow("Bilateral Filter (on Gauss)", bilateral_filter)
cv.imshow("Sharpen (on Gauss)", sharpened)

cv.waitKey(0)
cv.destroyAllWindows()