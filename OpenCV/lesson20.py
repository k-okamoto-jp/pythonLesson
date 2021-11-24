import cv2
import numpy as np

img = cv2.imread('src/road.jpg')
img_g = cv2.imread('src/road.jpg', 0)
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)
cv2.imshow('img_g', img_g)

img_canny = cv2.Canny(img_g, 300, 450)
cv2.imshow('img_canny', img_canny)

lines = cv2.HoughLines(img_canny, 1, np.pi/180, 100)
print(lines)

for i in lines[:]:
    rho = i[0][0]
    theta = i[0][1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)
cv2.imshow('img', img)

img2 = cv2.imread('src/grapes.jpg')
img2_g = cv2.imread('src/grapes.jpg', 0)
cv2.imshow('img2', img2)

circles = cv2.HoughCircles(
    img2_g, cv2.HOUGH_GRADIENT,
    dp=1, minDist=1, param1=20, param2=35, minRadius=1, maxRadius=30)
print(circles)

for i in circles[0]:
    cv2.circle(img2, (i[0], i[1]), i[2], (255, 0, 0), 1)

cv2.imshow('img2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()