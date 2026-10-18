#简介TrackBar:
#是 OpenCV 的滑动条控件，可以让用户通过拖动滑块改变参数，例如亮度、阈值、HSV 颜色范围等
#可以理解为窗口里的“滑动控制器”。它常用于让用户通过鼠标实时调整参数，例如：
#- 二值化阈值
#- 图像亮度
#- HSV 颜色范围
#- 模糊程度
#- 摄像头参数
#- 目标检测的大小范围

#调用API
#createTrackbar,创建...
#getTrackbarPos,获取TB的相关值（当前位置）

#CT(name,winname)，第一个是控件的名字，第二个是窗口的名字
#value:tracbar当前值
#count最小值为0，并且设定一个最大值

#getTrackarPos
#输入参数：name
#输入参数：winname
#输出：当前值

#使用TB
import cv2
import numpy as np

def callback():
    pass
cv2.namedWindow('trackbar',cv2.WINDOW_NORMAL)
#创建trackbar
cv2.createTrackbar('R','trackbar',0,255,callback)
cv2.createTrackbar('G','trackbar',0,255,callback)
cv2.createTrackbar('B','trackbar',0,255,callback)
#创建一个背景图片
img=np.zeros((480,640,3),np.uint8)

while True:
    #获得当前trackbar的值
    r=cv2.getTrackbarPos('R','trackbar')
    b=cv2.getTrackbarPos('G','trackbar')
    g=cv2.getTrackbarPos('B','trackbar')
    #改变背景图片的颜色
    img[:]=[b,g,r]
    cv2.imshow('trckbar',img)
   

    key=cv2.waitKey(10)
    if key&0xFF==ord('q'):
        break

cv2.destroyAllWindows
