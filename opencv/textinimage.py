import cv2
import numpy as np


img = np.zeros((512, 512, 3))
print(img.shape)

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img, 'dogs', (300, 300), font, 2, (255, 255, 0), 3, cv2.LINE_AA)
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

