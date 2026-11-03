import cv2
import numpy as np
img = cv2.imread('C:/Users/23832/Desktop/Sample picture/mmexport1792039269282.jpg')
if img is None:
    print("无法读取图像，请检查文件路径。")
else:
    gaussian_blur = cv2.GaussianBlur(img, (5, 5), 1.5)

    cv2.imshow('Original', img)
    cv2.imshow('Gaussian Filter (5x5)', gaussian_blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()