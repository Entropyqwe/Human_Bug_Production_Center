
#*图像的运算包括图像的加减乘除
#!图像的加法
import cv2
import numpy as np

dog=cv2.imread('C:/Users/23832/Desktop/Sample picture/mmexport1792039269282.jpg')
#必须尺寸一致才能进行加法运算
#图的加法运算就是矩阵的加法运算
print(dog.shape)#先输出这个图的基本信息，根据基本信息大小进行矩阵的运算
img=np.ones((1430, 1280, 3),np.uint8)*100
cv2.imshow('orig',dog)
result=cv2.add(dog,img)
cv2.imshow('result',result)
#!图像的减法
#subtract(A,B),含义是A减B
result2=cv2.subtract(result,img)
cv2.imshow('orig_1',result2)
cv2.waitKey(0)