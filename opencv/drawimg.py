import cv2

img = cv2.imread('images/dogs.jpg', 3)
print(img)
cv2.imshow('test', img)
cv2.waitKey(0)

print(img.shape)
cv2.line(img, (0, 0), (300, 300), (0, 0, 255), 10)

cv2.destroyAllWindows()
cv2.rectangle(img, (100, 100), (400, 400), (40, 30, 200), 20)
