import cv2
import copy

#  can't read with imread
img = cv2.imread('src/Blob.png')
img_g = cv2.imread('src/Blob.png', 0)

# img = mpimg.imread(
#     r'C:\Users\IPM\PycharmProjects\pythonProject\OpenCV\src\Blob.png')
# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)
cv2.imshow('img_g', img_g)

ret, img_bi = cv2.threshold(img_g, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('img_bi', img_bi)

contours, hierarchy = cv2.findContours(
    img_bi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contour = cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow('img_contour', img_contour)

cv2.waitKey(0)
cv2.destroyAllWindows()
