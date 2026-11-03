import cv2
import numpy as np
img = cv2.imread('"C:\\Users\\23832\\Desktop\\Sample picture\\lena.gif"')
    mean_blur = cv2.blur(img, (5, 5))
    median_blur = cv2.medianBlur(img, 5)
    cv2.imshow('Mean Filter (5x5)', mean_blur)
    cv2.imshow('Median Filter (5x5)', median_blur)
    cv2.waitKey(0)