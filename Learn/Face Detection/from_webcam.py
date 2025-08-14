import cv2


cascade_path = r"E:/Computer Vision/OpenCV/Learn/cascades/haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(cascade_path)


cap = cv2.VideoCapture(0)

cap.set(3, 800) # Set Width
cap.set(4, 480) # Set Height
cap.set(10, 100) # Brightness



while True:
    success, img = cap.read()
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_grey, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (w + x, h + y), (255, 0, 0), 1)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



