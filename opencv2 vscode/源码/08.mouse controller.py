#设置鼠标回调函数
#setMouseCallback(winname,callback,userdata)
#窗口的名字，自己设置的窗口回调函数，给回调参数传一些参数默认是什么都没有
#写自己的回调函数callback(event,x,y,flags,userdata)
#事件：点了什么东西，flags：附加条件
#event：鼠标事件，x，y：鼠标坐标
import cv2
import numpy as np
#导入库
#鼠标回调函数
def mouse_callback(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)
#mouse_callback(1,100,100,16,"666")

cv2.namedWindow('mouse',cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow('mouse',640,480)
#设置鼠标回调
cv2.setMouseCallback('mouse',mouse_callback,"123")

img=np.zeros((360,640,3),np.uint8)
#创图像数据
#创建一个高360，宽640（与正常情况下输入的顺序有所改变）

while True:
    #让窗口一直显示，采取循环模式
    cv2.imshow('mouse',img)
    key=cv2.waitKey(0)
    if key&0xFF==ord('q'):
        break
    cv2.destroyALLWindows()

 #代码总体达成的目标：创建一个纯黑色的画布，并且在上面绑定鼠标事件，当你在画布上点击或操作鼠标时，程序会打印鼠标的坐标和事件信息
