import cv2
import copy

#  can't read with imread
img = cv2.imread('src/Blob.png')
img_g = cv2.imread('src/Blob.png', 0)
h, w = img.shape[:2]
print(h, w)
cv2.imshow('img', img)
cv2.imshow('img_g', img_g)

ret, img_bi = cv2.threshold(img_g, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('img_bi', img_bi)

imb_blob = copy.deepcopy(img)
h, w = img_g.shape

nLabels, labelImage, stats, centroids = cv2.connectedComponentsWithStats(
    img_bi
)
print(nLabels, labelImage, stats, centroids)

color = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0]]
for y in range(h):
    for x in range (w):
        if labelImage[y, x] > 0:
            imb_blob[y, x] = color[labelImage[y, x]-1]
for i in range(1, nLabels):
    xc = int(centroids[i][0])
    yc = int(centroids[i][1])
    font = cv2.FONT_HERSHEY_COMPLEX
    scale = 1
    color = (255, 255, 255)
    cv2.putText(imb_blob, str(stats[i][-1]), (xc, yc), font, scale, color)

cv2.imshow('imb_blob', imb_blob)

cv2.waitKey(0)
cv2.destroyAllWindows()
