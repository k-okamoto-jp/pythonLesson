import cv2
import numpy as np

img = cv2.imread('src/Bus.jpg')
img_mask = cv2.imread('src/Mask.jpg', 0)
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)
cv2.imshow('img_mask', img_mask)

thresh = 1
ret, img_bin = cv2.threshold(img_mask, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow('img_bin', img_bin)

img_dst = cv2.inpaint(img, img_bin, 3, cv2.INPAINT_NS)
cv2.imshow('img_dst', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()