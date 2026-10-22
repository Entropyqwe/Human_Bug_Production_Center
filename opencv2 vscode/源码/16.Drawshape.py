
#!通过鼠标进行基本图形的绘制：鼠标回调与基础图形复制
#*当用户选择了L键即选择了画线。此时滑动鼠标即可画线
#*当选择r键就可以画矩形
import cv2
import numpy as np
curshape=0 
startpos=(0,0)
img=np.zeros((480,640,3),np.uint8)
#创图像数据
#创建一个高360，宽640（与正常情况下输入的顺序有所改变）
def mouse_callback(event,x,y,flags,userdata):
#!由于这个回调函数可以直接获取到鼠标点击前和点击后的坐标，所以核心思路是在点击和松开操作之间画一条线
    global curshape,startpos
    if (event&cv2.EVENT_LBUTTONDOWN==cv2.EVENT_LBUTTONDOWN):
        startpos=(x,y)
    elif(event&cv2.EVENT_LBUTTONDOWN==cv2.EVENT_LBUTTONDOWN):
        if curshape==0:
            cv2.linne(img,startpos,(x,y),(0,0,255))
        elif curshape==1:
            cv2.rectangle(img,startpos,(x,y),(0,0,255))
        elif curshape==2:
            a=(x-startpos[0])
            b=(x-startpos[1])
            r=int(a**2+b**2)**0.5
            cv2.circle(img,startpos,r,(0,0,255))
        else:
            print('error')
cv2.namedWindow('drawshape',cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('mouse',mouse_callback,"123")


while True:
    #让窗口一直显示，采取循环模式
    cv2.imshow('mouse',img)
    key=cv2.waitKey(0)&0xFF
    if key==ord('q'):
        break
    elif key==ord('l'):
        curshape=0
    elif key==ord('r'):
        curshape=1
    elif key==ord('c'):
        curshape=2
    cv2.destroyALLWindows()
