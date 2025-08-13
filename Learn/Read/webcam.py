import  cv2

vid_path = r"/Learn/Resources\vid.mp4"

cap = cv2.VideoCapture(0)

cap.set(3, 800) # Set Width
cap.set(4, 480) # Set Height
cap.set(10, 100) # Brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break