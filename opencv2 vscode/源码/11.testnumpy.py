import numpy as np#将这个库名字改为np方便后续操作
import cv2
 #a=np.array([1,2,3])

# b=np.array([[1,2,3],[4,5,6]])
# print(a)
# print(b)

#zeros
# import numpy as np
c=np.zeros((480,640,3),np.uint8)#对于显示器来说是有三个颜色组成
#!创建了一个480*640*3的画布，并且全部采用8位无符号整数，范围为0-255
#*关于np.zero，是将整个画布初始化，使得三个通道都为0，也就是黑色
# print(c)
#定义ones矩阵
# d=np.ones((8,8,3),np.uint8)
# print(c)
#定义full矩阵
# e=np.full。。。


#定义单位矩阵identity
# f=np.identity(8)#8*8的一个矩阵表格
# print(f)


#numpy基本操作
#检索与赋值[y,x]
#每个元素访问的时候数组从零开始
#表示多通道时[y,x,channel]channel是通道数
#检索

print(c[100,100])
#*读取第100行第100列的像素，并且将之打印出来，用来检测刚刚的创建是不是正确的
count=0
#*作为计时器，用于后续的循环
#*对于像素的操作是采用循环操作每一个像素
while count<200:
#*修改的目的是画出一个竖线，而在竖线中，列数是不变的，所以用循环数代替行数来不断对像素点进行赋值
    c[count,100, 0]=255
    count=count+1
c[100,100]=255
#*单独修改第100行和100列的像素，原本是三通道，这种写法直接对三个通道进行赋值
#可以对矩阵中某个值直接进行读取操作
cv2.imshow('img',c)
key=cv2.waitKey(0)
if key&0xFF==ord('q'):
    cv2.destroyAllWindows()

#!显示蓝色的原因是在openai中采用的色彩空间是BGR，第一个通道是表示蓝色的
#!在opencv中0代表蓝色，1代表绿色，2代表红色，而0到255只是对各自通道的颜色深度的界定
#c[count,100, 0]=255在这里得到界定，是说初始的色彩就是0，也就是蓝色