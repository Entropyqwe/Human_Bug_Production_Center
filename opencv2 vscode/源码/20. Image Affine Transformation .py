
#!仿射变换就是图像旋转，缩放和平移的总和
#*放射的API——warpAffine(src,M,dsize,flags,mode,value)后面不屑就是默认
#M:变换矩阵，disize输出尺寸大小
#flag：与resize中的插值算法一致，mode：边界外推法标志，value：填充边界的值#!一般是用默认预设就好

#*平移矩阵（在矩阵中的每一个像素进行加减法）
import cv2
import numpy as np

a=cv2.imread('C:/Users/23832/Desktop/Sample picture/1792283418441.jpeg')
#!获取到图片中的高度，宽度，通道数
M=np.float32([[1,0,-200],[0,1,200]])
h,w,ch=a.shape
#*改变图像的尺寸
new=cv2.warpAffine(a,M,(int(w/4),int(h/4)))
#M=np.float32([[1,0,100],[0,1,100]])
#!起到设定仿射值的作用，设定为，1行上向右移动100，1列上向下移动100
h,w,ch=new.shape
#*变换矩阵
#getRotationMatrix2D(center, angle, scale)
#!center中心点 angle角度,scale缩放比例
#!旋转的角度为逆时针，中心点是（x,y)
M=cv2.getRotationMatrix2D((100,100), 15, 0.5)

b=cv2.warpAffine(new,M,(w,h))
#!(w,h)是用来衡量输出窗口大小的

#*这里是限制变换的内容，锁定在宽度和高度上

#*变换矩阵
#getRotationMatrix2D(center, angle, scale)
#!center中心点 angle角度,scale缩放比例
cv2.imshow('a',new)
cv2.imshow('b',b)
cv2.waitKey(0)
