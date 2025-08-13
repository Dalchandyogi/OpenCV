import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# img[:] = 255, 230, 0  # img color


# Draw Line
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 3)

# Draw Rectangle
cv2.rectangle(img, (20, 0), (300, 150), (0,0,255), 5)

# Draw Circle
cv2.circle(img, (450, 100), 30, (255, 255, 0), 3)

cv2.imshow("Image", img)

cv2.waitKey(0)
