import cv2
import numpy as np


image = cv2.imread("C:\\workspace\\Python\\blending_figure\\11.jpg")

cv2.imshow("img", image)
cv2.waitKey(0)

(B, G, R) = cv2.split(image)
merged_image = cv2.merge([B, G, R])

cv2.imshow("RED", R)
cv2.waitKey(0)

cv2.imshow("GREEN", G)
cv2.waitKey(0)

cv2.imshow("BLUE", B)
cv2.waitKey(0)

cv2.imshow("MERGED", merged_image)
cv2.waitKey(0)

cv2.imwrite("/workspace/Python/blending_figure/new_merged.jpg", merged_image)

# python C:\workspace\Python\chplit.py