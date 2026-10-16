#写python必须进行引入包名，包名是不需要分号的
import cv2

cv2.namedWindow('new',cv2.WINDOW_NORMAL)
cv2.resizeWindow('new',1920,1080)
cv2.imshow('new',0)
#加入waitKeyEx来保证窗口不会自动消失
cv2.waitKey(0)
#未操作之前一直显示

cv2.destroyAllWindows()