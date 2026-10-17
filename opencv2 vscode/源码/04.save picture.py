import cv2

cv2.namedWindow('new',cv2.WINDOW_NORMAL)
img=cv2.imread("C:/Users/23832/Desktop/Sample picture/mmexport1792039269282.jpg")

while True:
    cv2.imshow('new',img)
#加入waitKeyEx来保证窗口不会自动消失
    key=cv2.waitKey(0)
#未操作之前一直显示
    if key==ord('q'):  
        cv2.destroyAllWindows()
        break#必须要跳出循环
    elif key==ord('s'):
        cv2.imwrite('C:/Users/23832/Desktop/saved.jpg')
    ##可以改变图片格式