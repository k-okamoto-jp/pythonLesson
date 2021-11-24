import cv2

img = cv2.imread('src/floor.jpg', 0)

def onTrackbar(position):
    global threshold
    threshold = position

threshold = 100
cv2.namedWindow('img')
cv2.createTrackbar('track', 'img', threshold, 255, onTrackbar)
while True:
    # ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    img_th = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3,
        threshold)
    cv2.imshow('img', img_th)
    cv2.imshow('src', img)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()
