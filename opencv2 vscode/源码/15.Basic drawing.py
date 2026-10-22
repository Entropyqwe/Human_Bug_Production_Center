#*一类是画线，画矩形，画圆
#*二类是画椭圆，画多边形，绘制字体（字幕，软字幕与硬字幕）

import cv2
import numpy as np
#*创建一个画布用于绘制图像
img=np.zeros((480,640,3),np.uint8)
#对于画线的时候是使用（x，y）的形式进行
#!画线line（img，开始点，结束点，颜色，线宽，线型...)还有shift按照坐标比例缩放
# cv2.line(img,(10,20),(300,400),(0,0,255),5,20)
# cv2.line(img,(30,600),(100,150),(120,120,0),5,8)
#!画圆circle(img,中心点，半径，颜色(BGR格式)，线宽)：将线宽设置为-1就是实心圆，在线宽后面加上cv2.LINE_AA可以使得画出来的图形更加平滑
cv2.circle(img,(100,200),30,(0,0,255),5,cv2.LINE_AA)
cv2.circle(img,(300,400),40,(120,120,0),5,cv2.LINE_AA)
#!画椭圆ellipse(img,中心点，长宽的一半，角度，从哪个角度开始，到那个角度结束...)
...
#!画多边形polylines(img，点集，是否闭环，颜色，...):点集即使顶点坐标，是否闭环就是是否连线闭合起来
#!填充多边形fillPoly(img,点集，颜色)
pts = np.array([(300,10),(150,100),(450,100)],np.int32)
cv2.polylines(img, [pts], True, (0, 0, 255))
cv2.fillPoly(img,[pts],(255,0,0))
#!绘制文本putText(img,字符串，起始点，字体，字号，...):字符串指的就是输入的文本内容
cv2.putText(img,"Hello World!",(10,400),cv2.FONT_HERSHEY_COMPLEX,3,(120,120,120))

cv2.imshow('draw',img)
cv2.waitKey(0)