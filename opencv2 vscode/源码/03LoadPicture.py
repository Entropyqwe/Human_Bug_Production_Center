import cv2

cv2.namedWindow('new',cv2.WINDOW_NORMAL)
img=cv2.imread("C:/Users/23832/Desktop/Sample picture/mmexport1792039269282.jpg")
cv2.imshow('new',img)
#加入waitKeyEx来保证窗口不会自动消失
cv2.waitKey(0)
#未操作之前一直显示

cv2.destroyAllWindows()