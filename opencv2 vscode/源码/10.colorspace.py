#关于色彩空间的转换
#效果：通过trackbar
import cv2

def callback(value):
    pass
cv2.namedWindow('color',cv2.WINDOW_AUTOSIZE)
img=cv2.imread('C:/Users/23832/Desktop/Sample picture/mmexport1792039269282.jpg')
colorspaces=[cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA,
cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV_FULL]
cv2.createTrackbar('curcolor', 'color', 0, len(colorspaces)-1, callback)

while True:
    v=cv2.getTrackbarPos('curcolor','color')
    cvt_img=cv2.cvtColor(img,colorspaces[v])
    cv2.imshow('color',cvt_img)
    key=cv2.waitKey(10)
    if key&0xFF==ord('q'):
        break
cv2.destroyAllWindows()