import cv2 as cv
import numpy as np

# 1. 读图
img = cv.imread("C:/Users/23832/Desktop/Sample picture/1792283418441.jpeg") 

if img is None:
    print("图片读取失败，请检查路径")
    exit()

# 2. 转灰度
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 3. 二值化：目标物体要变成白色，背景是黑色
_, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# 4. 找轮廓
contours, hierarchy = cv.findContours(
    thresh,
    cv.RETR_EXTERNAL,
    cv.CHAIN_APPROX_SIMPLE
)

# 5. 复制一张图用来画轮廓
result = img.copy()

# 6. 画所有轮廓，并打印每个轮廓的面积
for i, cnt in enumerate(contours):
    area = cv.contourArea(cnt)
    print(f"轮廓 {i} 的面积 = {area:.2f}")

    # 只画面积大于 500 的轮廓，过滤小噪声
    if area > 500:
        cv.drawContours(result, [cnt], -1, (0, 255, 0), 2)

# 7. 画面积最大的轮廓
if contours:
    largest = max(contours, key=cv.contourArea)
    cv.drawContours(result, [largest], -1, (0, 0, 255), 3)

    # 画最大轮廓的外接矩形
    x, y, w, h = cv.boundingRect(largest)
    cv.rectangle(result, (x, y), (x + w, y + h), (255, 0, 0), 2)

    print(f"最大轮廓面积 = {cv.contourArea(largest):.2f}")

# 8. 显示结果
cv.imshow("original", img)
cv.imshow("result", result)
cv.waitKey(0)
cv.destroyAllWindows()