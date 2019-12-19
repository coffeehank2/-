import cv2
import numpy as np

image = cv2.imread("C:\\workspace\\Python\\cytus-ii-free-new-239.jpg")

cv2.imshow("img", image)
cv2.waitKey(0)

t1, thd_bin = cv2.threshold(image, 127,255,cv2.THRSH_NINARY)
cv2.imshow("thd_bin", thd_bin)
cv2.waitKey(0)

t2, thd_bin_inv = cv2.threshold(image, 127,255,cv2.THRSH_NINARY_INV)
cv2.imshow("thd_bin_inv", thd_bin_inv)
cv2.waitKey(0)

thd_bin_adaptive = cv2.adaptiveThreshold(image, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRSH_BIYARY, 5, 3)
cv2.imshow("thd_bin_adaptive", thd_bin_adaptive)
cv2.waitKey(0)

t3, thd_bin_otsu = cv2.threshold(image, 0, 255, cv2.THRSH_NINARY_INV+cv2.THRESH_OTSU)
cv2.imshow("thd_bin_otsu", thd_bin_otsu)
cv2.waitKey(0)

cv2.destoryAllWindows()