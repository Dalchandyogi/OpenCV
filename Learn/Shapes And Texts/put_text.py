import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.putText(img, "Open CV", (200, 206), cv2.FONT_HERSHEY_DUPLEX, 1.8, (255, 130, 199), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
