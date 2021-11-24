import cv2
import numpy as np

img = cv2.imread('src/Lena.jpg', 0)
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)

kernel = np.ones((3, 3)) / 9.0
print(kernel)

img_ke1 = cv2.filter2D(img, -1, kernel)

cv2.imshow('img_ke1', img_ke1)

kernel2 = np.zeros((3, 3))
kernel2[0, 0] = 1
kernel2[1, 0] = 2
kernel2[2, 0] = 1
kernel2[0, 2] = -1
kernel2[1, 2] = -2
kernel2[2, 2] = -1
print(kernel2)

img_ke2 = cv2.filter2D(img, -1, kernel2)
cv2.imshow('img_ke2', img_ke2)

cv2.waitKey(0)
cv2.destroyAllWindows()