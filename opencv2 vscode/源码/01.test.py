import cv2
import numpy as np

img=cv2.imdecode(np.fromfile(r"C:\Users\23832\Pictures\Screenshots\屏幕截图 2026-10-16 155713.png",dtype=np.uint8),cv2.IMREAD_COLOR)

cv2.imshow('img',img)
cv2.waitKey(0)
#保证在不操作的情况下，图片可以一直存在

#np.fromfile(r"C:\Users\23832\Pictures\Screenshots\屏幕截图 2026-10-16 155713.png",dtype=np.uint8),cv2.IMREAD_COLOR)
#将文件都城NUmpy数组，- dtype=np.uint8：按图片常用的 8 位无符号整数读取。
#cv2.IMREAD_COLOR告诉 OpenCV 按彩色图片解码。它通常作为第二个参数传给 cv2.imdecode()。