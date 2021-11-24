import cv2
import matplotlib.pyplot as plt

img = cv2.imread('src/grapes.jpg', 0)
cv2.imshow('img', img)

threshold = 100
ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
print(ret)
cv2.imshow('img_th', img_th)

ret2, img_o = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
print(ret2)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()
cv2.imshow('img_o', img_o)

img_ada = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1)
cv2.imshow('img_ada', img_ada)

cv2.waitKey(0)
cv2.destroyAllWindows()
