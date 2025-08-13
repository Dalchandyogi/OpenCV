import cv2

# Image path
img_path = r"/Learn/Resources\i.jpeg"

# Read image
img = cv2.imread(img_path)

# Check if image loaded successfully
if img is None:
    print("Error: Could not read the image. Check the path.")
else:
    cv2.imshow("image", img)
    cv2.waitKey(0)
