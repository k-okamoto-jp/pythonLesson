import cv2

img = cv2.imread('src/Lena.jpg', 0)
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)

img_canny = cv2.Canny(img, 10, 180)
cv2.imshow('img_canny', img_canny)

img_canny2 = cv2.Canny(img, 100, 200)
cv2.imshow('img_canny2', img_canny2)


cv2.waitKey(0)
cv2.destroyAllWindows()