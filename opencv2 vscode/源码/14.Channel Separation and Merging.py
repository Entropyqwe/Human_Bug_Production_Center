#*通道的分离与合并
#!split(mat)分割的意思，输入的类型是一个mat类型的图像，有几个通道分离几个通道
#!merge((ch1,ch2,....))此为通道的合并，ch是通道数的意思，将几个通道合并在一起
import cv2
import numpy as np


img=np.zeros((480,640,3),np.uint8)

b,g,r=cv2.split(img)
b[10:100,10:100]=255
#!相当与b的数据单独拷贝了一份，也就是深拷贝
g[10:100,10:100]=255

img2=cv2.merge((b,g,r))
cv2.imshow('img',img)
cv2.imshow('b',b)
cv2.imshow('img2',img2)
cv2.waitKey(0)