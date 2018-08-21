import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened() :
    status, frame = cap.read()

    cv2.rectangle(frame, (100, 100), (300, 300), (0, 75, 140), 3)
    cv2.imshow('current', frame)
    if cv2.waitKey(30) & 0xFF == ord('q') :
        break

cv2.destroyAllWindows()
cap.release()




