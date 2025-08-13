import cv2
img_path = r"E:\Computer Vision\OpenCV\Learn\Resources\lambo.jpeg"

img = cv2.imread(img_path)
print(img.shape)

resize_img = cv2.resize(img, (400, 230))

cv2.imshow("LAMBO", img)
cv2.imshow("Resize Img", resize_img)


cv2.waitKey(0)