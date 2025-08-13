import  cv2

vid_path = r"/Learn/Resources\vid.mp4"

cap = cv2.VideoCapture(vid_path)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break