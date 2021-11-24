import cv2

img = cv2.imread('src/buildings.jpg')
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)

img_blur = cv2.blur(img, (3, 3))
cv2.imshow('img_blur', img_blur)

img_ga = cv2.GaussianBlur(img, (9, 9), 2)
cv2.imshow('img_ga', img_ga)

img_me = cv2.medianBlur(img, 5)
cv2.imshow('img_me', img_me)

img_bi = cv2.bilateralFilter(img, 20, 30, 30)
cv2.imshow('img_bi', img_bi)

cv2.waitKey(0)
cv2.destroyAllWindows()