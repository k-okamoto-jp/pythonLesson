import cv2

HAAR_FILE = (r'C:\Users\IPM\anaconda3\pkgs\libopencv-4.0.1-hbb9e17c_0\Library'
             r'\etc\haarcascades\haarcascade_frontalface_default.xml')
cascade = cv2.CascadeClassifier(HAAR_FILE)

img = cv2.imread('src/Solvay_conference_1927.jpg')
img_g = cv2.imread('src/Solvay_conference_1927.jpg', 0)
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)

face = cascade.detectMultiScale(img_g)
print(face)
for x, y, w, h in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()