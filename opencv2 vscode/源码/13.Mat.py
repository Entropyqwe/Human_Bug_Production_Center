#Mat从应用上看就是矩阵，从实现的角度上
#可以直接通过矩阵的方式进行访问，用numpy来调用

#*每一个Mat包括两部分，头部（Header）和数据（Data）
# class CV_EXPORTS Mat{
# public:

# ...

# int dims;//维数
# int rows,cols;//行列数
# uchar *data;//存储数据的指针
#int  *refcount；//引用计数，防止内存泄漏

#Mat拷贝
# 拷贝的两个header是不一样的，就是说只会有一部分图像的属性进行了拷贝，而图像的其他内容也就是数据内容是公用的
#这样一来，通过单纯复制头部的浅拷贝可以做到所占空间小，同时修改互不影响的作用
#数据通过指针指向的是同一个地址、
#定义一个MatA


# Mat A
# A=imread(file,IMREAD_COLOR)
# MatB（A）
#*此过程将A的头部复制给B

#*Mat的深拷贝（将头部和数据都复制一遍，完全切断与原体ide联系）
# cv::Mat::clone()
# cv::Mat::copyTo()
#!上面两种是在C语言中的深拷贝实现方式
#!copy()是针对python语言实现深拷贝
import cv2
import numpy as np
img=cv2.imread('C:/Users/23832/Desktop/Sample picture/mmexport1792039269282.jpg')
#!以下为浅拷贝
# img2=img
# img[10:100,10:100]=[0,0,255]
# cv2.imshow('img',img)
# cv2.imshow('img2',img2)
#!以下为深拷贝
img3=img.copy()
img[10:100,10:100]=255
#这里相当于把图像分成了两部分，而由于前面已经进行了深拷贝工作，修改只是在复制本上面进行修改
cv2.imshow('img',img)
cv2.imshow('img3',img3)
cv2.waitKey(0)


