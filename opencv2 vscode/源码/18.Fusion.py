
#!只有两张图的属性是一样的才可以进行溶合
#!图像的溶合
#*addWeighted(A,alpha,B,bate,gamma)
#alpha和beta是权重，alpha是结果融合后A图像占的权重，bate是结果融合后B占的权重，总占比为1
#gamma为静态权重
import cv2
import numpy as np

a=cv2.imread('C:/Users/23832/Desktop/Sample picture/1792283418441.jpeg')
b=cv2.imread('C:/Users/23832/Desktop/Sample picture/1792283384650.jpeg')

print(a.shape)
print(b.shape)

result=cv2.addWeighted(a,0.7,b,0.3,0)
cv2.imshow('add',result)
cv2.waitKey(0)