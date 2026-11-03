
#!关于图像卷积的API
#filter2D(src, ddepth, kernel, dst[, anchor, delta, borderType) → dst
# src: 输入图像
# ddepth: 输出图像的深度一般填为-1，即与原图像相比不发生位深的变化
# dst: 输出图像
# anchor: 锚点，卷积核的中心点
# kernel: 卷积核

import cv2
import numpy as np

img=cv2.imread('C:/Users/23832/Desktop/Sample picture/mmexport1792039269282.jpg')
dst=cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25)
#np.ones((5,5),np.float32)/25先创建一个5*5的矩阵，矩阵中每一个元素都是1，随后每个元素都除以25
cv2.imshow('dst',dst)
cv2.imshow('img',img)
cv2.waitKey(0)

#!该代码使原图像变模糊的原因：
# 卷积核创建了一个5*5的矩阵，其中每个元素都是1
# 归一化处理：都除以25，并且使得所有元素之和为1
# 卷积操作：函数将这个卷积核在原图像上面滑动，直到完整覆盖原图像的每一个像素点，是在每个5*5的区域里面取平均值
# 所以变模糊了