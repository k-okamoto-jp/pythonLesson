import cv2
import sys

cap = cv2.VideoCapture('movie/Cosmos.mp4')
if cap.isOpened() is False:
    sys.exit()
ret, frame = cap.read()
h, w = frame.shape[:2]
fourcc = cv2.VideoWriter_fourcc(*'XVID')
dst = cv2.VideoWriter('output/test.avi', fourcc, 30.0, (w, h))

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    cv2.imshow('img', frame)
    dst.write(frame)
    if cv2.waitKey(30) == 27:
        break
cv2.destroyAllWindows()
cap.release
pass
