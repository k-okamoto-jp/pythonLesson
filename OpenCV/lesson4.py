import cv2

img = cv2.imread('src/grapes.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)

size = (300, 200)  # tuple (width, height) vice versa
img_resize = cv2.resize(img, size)
print(img_resize.shape)
cv2.imshow('resize', img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_area = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
img_linear = cv2.resize(img, size, interpolation=cv2.INTER_LINEAR)
cv2.imshow('area', img_area)
cv2.imshow('linear', img_linear)
cv2.waitKey(0)
cv2.destroyAllWindows()