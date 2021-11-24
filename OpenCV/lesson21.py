import cv2
import numpy as np

img = cv2.imread('src/floor.jpg', 0)
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)

ret, img_th = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
cv2.imshow('img_th', img_th)

kernel = np.ones((3, 3), dtype=np.uint8)
img_d = cv2.dilate(img_th, kernel)
img_e = cv2.erode(img_th, kernel)
cv2.imshow('img_d', img_d)
cv2.imshow('img_e', img_e)

img_c = cv2.morphologyEx(img_th, cv2.MORPH_CLOSE, kernel)
cv2.imshow('img_c', img_c)
cv2.waitKey(0)
cv2.destroyAllWindows()