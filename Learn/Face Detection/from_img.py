import cv2

# Image path
img_path = r"E:/Computer Vision/OpenCV/Learn/Resources/faces.jpg"

cascade_path = r"E:/Computer Vision/OpenCV/Learn/cascades/haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(cascade_path)

# Read image
img = cv2.imread(img_path)

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_grey, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (w+x, h+y), (255,0,0), 1)

# Check if image loaded successfully
if img is None:
    print("Error: Could not read the image. Check the path.")
else:
    cv2.imshow("image", img)
    cv2.waitKey(0)
