import cv2

img = cv2.imread('images/dogs.jpg', 3)


print(img.shape)
img3 = cv2.line(img, (0, 0), (300, 300), (0, 0, 255), 10)
cv2.imwrite('images/img3.jpg', img3)

#cv2.ellipse(img3, (200, 200), (100, 400))

img4 = cv2.rectangle(img, (100, 100), (400, 400), (40, 30, 200), 20)
cv2.imwrite('images/img4.jpg', img4)

cv2.imshow('test', img3)

crop_img = img3[0:640, 0:480]  # type: object

cv2.imshow('test2', img4)
cv2.imshow('cropped', crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
