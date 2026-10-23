#“透视变换”就可以把一个矩形变成一个梯形（就像你斜着看一张纸，它看起来就是梯形的）。
#!另外一种解释就是，把原来的一种坐标系转换为另外一种坐标系

#!透视变换API：warp Perspective(img,M,dsize,...)

#M是变换矩阵
#dsize是目标图像大小

#!获得变换矩阵的方式：getPersectiveTransform(src,dst)
#*此时需要的是四个点而不是三个点(图片四个角的四个点)

import cv2
import numpy as np
a=cv2.imread('C:/Users/23832/Desktop/Sample picture/1792283418441.jpeg')
#!需要打两个中括号
src=np.float32([[100,1100],[200,123],[300,234],[100,450]])
dst=np.float32([[0,0],[300,200],[400,300],[200,500]])
M=cv2.getPerspectiveTransform(src,dst)
N=cv2.warpPerspective(a,M,(2160,2880))

cv2.imshow('aa',a)
cv2.imshow('b',N)
cv2.waitKey(0)