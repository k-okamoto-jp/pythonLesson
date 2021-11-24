import cv2
import matplotlib.pyplot as plt
# %matplotlib inline

img_gray = cv2.imread('src/Lena.jpg', 0)
hist2 = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist2, color='gray')


img_eq = cv2.equalizeHist(img_gray)
hist_e = cv2.calcHist([img_eq], [0], None, [256], [0, 256])
plt.plot(hist_e, color='black')
plt.show()

cv2.imshow('img', img_gray)
cv2.imshow('eq', img_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()
