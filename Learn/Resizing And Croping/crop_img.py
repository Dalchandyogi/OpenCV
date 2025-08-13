import cv2

img = cv2.imread("E:/Computer Vision/OpenCV/Learn/Resources/lambo.jpeg")
print(img.shape)
crop_img = img[0:200, 0:200]

cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", crop_img)

cv2.waitKey(0)