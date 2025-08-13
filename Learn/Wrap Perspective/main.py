import cv2
import numpy as np

img = cv2.imread("E:/Computer Vision/OpenCV/Learn/Resources/cards.jpg")
resize_img = cv2.resize(img, (550, 611))

width, height = 250, 350

pts1 = np.float32([[79, 330], [257, 330], [79, 578], [255, 574]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

single_card = cv2.warpPerspective(resize_img, matrix, (width, height))

cv2.imshow("Cards", resize_img)
cv2.imshow("Single Card", single_card)
cv2.waitKey(0)