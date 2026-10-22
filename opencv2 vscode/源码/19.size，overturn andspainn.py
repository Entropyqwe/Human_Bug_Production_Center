"""
第19课：图像的放大、缩小、翻转和旋转

本例继续使用第18课中的两张图片：
    1792283418441.jpeg
    1792283384650.jpeg

运行程序后会依次弹出处理结果窗口，按任意键即可关闭窗口。
"""

import cv2


# 读取第18课使用的两张图片
path_a = "C:/Users/23832/Desktop/Sample picture/1792283418441.jpeg"
path_b = "C:/Users/23832/Desktop/Sample picture/1792283384650.jpeg"

image_a = cv2.imread(path_a)
image_b = cv2.imread(path_b)

# imread 读取失败时会返回 None，先检查路径和文件是否正确
if image_a is None or image_b is None:
    raise FileNotFoundError(
        "图片读取失败，请检查图片路径：\n"
        f"{path_a}\n{path_b}"
    )

print("图片A的尺寸（高、宽、通道）：", image_a.shape)
print("图片B的尺寸（高、宽、通道）：", image_b.shape)


# fx 和 fy 是水平方向、垂直方向的缩放比例。
# 1.5 表示放大到原来的 1.5 倍，0.5 表示缩小到原来的一半。
# INTER_LINEAR 适合普通放大；INTER_AREA 适合缩小，能减少锯齿和摩尔纹。
image_a_big = cv2.resize(
    image_a, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR
)
image_a_small = cv2.resize(
    image_a, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA
)

cv2.imshow("1-Original image A", image_a)
cv2.imshow("2-Scaled up 1.5x", image_a_big)
cv2.imshow("3-Scaled down 0.5x", image_a_small)


# flipCode = 1：沿 y 轴翻转，也就是左右翻转（水平镜像）。
# flipCode = 0：沿 x 轴翻转，也就是上下翻转（垂直镜像）。
# flipCode = -1：同时进行水平和垂直翻转。
image_b_horizontal = cv2.flip(image_b, 1)
image_b_vertical = cv2.flip(image_b, 0)
image_b_both = cv2.flip(image_b, -1)

cv2.imshow("4-Original image B", image_b)
cv2.imshow("5-Horizontal flip", image_b_horizontal)
cv2.imshow("6-Vertical flip", image_b_vertical)
cv2.imshow("7-Horizontal and vertical flip", image_b_both)

# cv2.rotate 不需要自己计算旋转矩阵，适合 90°、180°、270° 的旋转。
image_a_90_clockwise = cv2.rotate(image_a, cv2.ROTATE_90_CLOCKWISE)
image_a_90_counterclockwise = cv2.rotate(
    image_a, cv2.ROTATE_90_COUNTERCLOCKWISE
)
image_b_180 = cv2.rotate(image_b, cv2.ROTATE_180)

cv2.imshow("8-Rotate A 90 degrees clockwise", image_a_90_clockwise)
cv2.imshow(
    "9-Rotate A 90 degrees counterclockwise", image_a_90_counterclockwise
)
cv2.imshow("10-Rotate B 180 degrees", image_b_180)


# getRotationMatrix2D 可以生成任意角度的旋转矩阵。
# angle 为正数时，OpenCV 默认按逆时针方向旋转；scale=1.0 表示不改变大小。
height, width = image_b.shape[:2]
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 30, 1.0)
image_b_30 = cv2.warpAffine(image_b, rotation_matrix, (width, height))

cv2.imshow("11-Rotate B 30 degrees", image_b_30)


# 按任意键关闭所有窗口；destroyAllWindows 可以释放窗口资源。
cv2.waitKey(0)
cv2.destroyAllWindows()
