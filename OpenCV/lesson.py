import cv2
import os

img = cv2.imread('src/Berry.jpg')
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# os.mkdir('./output')
cv2.imwrite('output/test.jpg', img)
pass
