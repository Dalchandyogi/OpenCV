import  cv2
import numpy as np

img_path = r"E:\Computer Vision\OpenCV\Learn\Resources\lena.jpeg"

img = cv2.imread(img_path)
kernel = np.ones((5, 5), np.uint8)

# Make Image Grey
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Make Image Blur
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

# Make img Canny
img_canny = cv2.Canny(img, 200, 200)

# Make Dialation Image
img_dialation = cv2.dilate(img_canny, kernel, iterations=1)

# Eroded Image
img_eroded = cv2.erode(img_dialation, kernel, iterations=1)

cv2.imshow("Gray Image", img_gray)
cv2.imshow("Blur Image", img_blur)
cv2.imshow("Canny Image", img_canny)
cv2.imshow("Dialation Image", img_dialation)
cv2.imshow("Eroded Image", img_eroded)
cv2.waitKey(0)