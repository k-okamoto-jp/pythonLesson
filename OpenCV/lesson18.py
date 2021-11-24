import cv2

img = cv2.imread('src/Lena.jpg', 0)
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)

img_sobelx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
print(img_sobelx)
img_sobelx = cv2.convertScaleAbs(img_sobelx)
print(img_sobelx)

cv2.imshow('img_sobelx', img_sobelx)

img_sobely = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)
img_sobely = cv2.convertScaleAbs(img_sobely)
cv2.imshow('img_sobely', img_sobely)

img_lap = cv2.Laplacian(img, cv2.CV_32F)
img_lap = cv2.convertScaleAbs(img_lap)
img_lap *= 2
cv2.imshow('img_lap', img_lap)

img_blur = cv2.GaussianBlur(img, (3, 3), 2)
img_lap2 = cv2.Laplacian(img_blur, cv2.CV_32F)
img_lap2 = cv2.convertScaleAbs(img_lap2)
img_lap2 *= 2
cv2.imshow('img_lap2', img_lap2)


cv2.waitKey(0)
cv2.destroyAllWindows()