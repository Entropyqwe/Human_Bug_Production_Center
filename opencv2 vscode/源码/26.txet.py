import cv2 as cv
import numpy as np

# ===================== 1. 自动生成一张带"瑕疵"的合成图 =====================
# 创建一张 400x800 的纯黑底图
canvas = np.zeros((400, 800, 1), dtype=np.uint8)

# 画一个大的白色矩形（作为"前景主体"）
canvas[50:350, 50:350] = 255
# 画一个圆形
cv.circle(canvas, (600, 200), 100, 255, -1)

# 人为添加瑕疵（模拟真实图像中的噪点和裂缝）
# 1. 在主体周围画几个小白点（白色噪点）
canvas[30:40, 30:40] = 255
canvas[300:310, 300:310] = 255
# 2. 在主体内部画几个小黑点（黑色噪点/孔洞）
canvas[100:110, 100:110] = 0
# 3. 画一条断开的线（裂缝）
canvas[370:380, 50:350] = 255
cv.circle(canvas, (200, 375), 10, 0, -1)  # 在直线上抠一个洞

# 把这张"烂图"作为我们的原图，并给它加上文字标签
img_original = canvas.copy()
cv.putText(img_original, 'Original (原图)', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, 127, 2)

# ===================== 2. 创建结构元素（印章） =====================
# 创建一个 7x7 的十字形印章（奇数尺寸，十字形能很好地保留线条和轮廓）
kernel = cv.getStructuringElement(cv.MORPH_CROSS, (7, 7))

# ===================== 3. 批量计算 7 种形态学效果 =====================
# 1. 腐蚀：让物体变瘦，吃掉白点
img_erode = cv.erode(img_original, kernel, iterations=1)
cv.putText(img_erode, 'Erosion (腐蚀)', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, 127, 2)

# 2. 膨胀：让物体变胖，填补黑洞
img_dilate = cv.dilate(img_original, kernel, iterations=1)
cv.putText(img_dilate, 'Dilation (膨胀)', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, 127, 2)

# 3. 开运算：先腐后膨，去掉白点，主体不变
img_open = cv.morphologyEx(img_original, cv.MORPH_OPEN, kernel)
cv.putText(img_open, 'Opening (开运算)', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, 127, 2)

# 4. 闭运算：先膨后腐，填补黑洞，主体不变
img_close = cv.morphologyEx(img_original, cv.MORPH_CLOSE, kernel)
cv.putText(img_close, 'Closing (闭运算)', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, 127, 2)

# 5. 形态学梯度：膨胀图减去腐蚀图，提取边缘
img_grad = cv.morphologyEx(img_original, cv.MORPH_GRADIENT, kernel)
cv.putText(img_grad, 'Gradient (梯度)', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, 127, 2)

# 6. 顶帽：原图减去开运算图，提取白点
img_tophat = cv.morphologyEx(img_original, cv.MORPH_TOPHAT, kernel)
cv.putText(img_tophat, 'Top Hat (顶帽)', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, 127, 2)

# 7. 黑帽：闭运算图减去原图，提取黑洞
img_blackhat = cv.morphologyEx(img_original, cv.MORPH_BLACKHAT, kernel)
cv.putText(img_blackhat, 'Black Hat (黑帽)', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, 127, 2)

# ===================== 4. 并排拼接并显示 =====================
# 水平拼接：原图 | 腐蚀 | 膨胀 | 开运算
row1 = cv.hconcat([img_original, img_erode, img_dilate, img_open])
# 水平拼接：闭运算 | 梯度 | 顶帽 | 黑帽
row2 = cv.hconcat([img_close, img_grad, img_tophat, img_blackhat])
# 垂直拼接两行
final_result = cv.vconcat([row1, row2])

# 弹出一个窗口显示结果
cv.imshow('Morphological Operations Comparison', final_result)
print("请按任意键关闭窗口...")
cv.waitKey(0)
cv.destroyAllWindows()