import cv2
import numpy as np


image = cv2.imread("C:\\workspace\\Python\\blending_figure\\11.jpg")

cv2.imshow("img", image)
cv2.waitKey(0)

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("img", shifted_image)
cv2.waitKey(0)

(h, w) = image.shape[:2]
center = (w//2, h//2)


M = cv2.getRotationMatrix2D(center, 135, 1.0)
rorate_image = cv2.warpAffine(image, M, (w, h))
cv2.imshow("img", rorate_image)
cv2.waitKey(0)


new_w, new_h = 100, 200
resize_image = cv2.resize(image, (new_w, new_h), cv2.INTER_AREA)
cv2.imshow("img", resize_image)
cv2.waitKey(0)


filpped_image = cv2.flip(image, -1)
cv2.imshow("img", filpped_image)
cv2.waitKey(0)

cropped_image = image[0:50, 0:50]
cv2.imshow("img", cropped_image)
cv2.waitKey(0)

cv2.imwrite("/workspace/Python/blending_figure/new_image.jpg", cropped_image)

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


# python C:\workspace\Python\tran.py
