import cv2
import numpy as np


def empty(value):
    # print(value)
    pass

def stack_image(scale, images):
    rows = len(images)
    cols = len(images[0])
    rows_available = isinstance(images[0], list)
    width = images[0][0].shape[1]
    height = images[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if images[x][y].shape[:2] == images[0][0].shape[:2]:
                    images[x][y] = cv2.resize(images[x][y], (0, 0), None, scale, scale)
                else:
                    images[x][y] = cv2.resize(images[x][y], (images[0][0].shape[1], images[0][0].shape[0]),
                                                None, scale, scale)
                if len(images[x][y].shape) == 2: images[x][y] = cv2.cvtColor(images[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows
        hor_con = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(images[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if images[x].shape[:2] == images[0].shape[:2]:
                images[x] = cv2.resize(images[x], (0, 0), None, scale, scale)
            else:
                images[x] = cv2.resize(images[x], (images[0].shape[1], images[0].shape[0]), None, scale, scale)
            if len(images[x].shape) == 2: images[x] = cv2.cvtColor(images[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(images)
        ver = hor
    return ver

# create New Window
window_name = "Track Bars"
cv2.namedWindow(window_name)
cv2.resizeWindow(window_name, 640, 240)

# create a new trackbar
# cv2.createTrackbar("Hue Min ", window_name, 0, 179, empty)  | Here first using this we find the values
# cv2.createTrackbar("Hue Max ", window_name, 179, 179, empty)
# cv2.createTrackbar("Sat Min ", window_name, 0, 255, empty)
# cv2.createTrackbar("Sat Max ", window_name, 255, 255, empty)
# cv2.createTrackbar("Val Min ", window_name, 0, 255, empty)
# cv2.createTrackbar("Val Max ", window_name, 255, 255, empty)


cv2.createTrackbar("Hue Min ", window_name, 0, 179, empty) # Here these values are choose fron tracker
cv2.createTrackbar("Hue Max ", window_name, 33, 179, empty)
cv2.createTrackbar("Sat Min ", window_name, 73, 255, empty)
cv2.createTrackbar("Sat Max ", window_name, 255, 255, empty)
cv2.createTrackbar("Val Min ", window_name, 147, 255, empty)
cv2.createTrackbar("Val Max ", window_name, 255, 255, empty)

# img = cv2.imread("E:/Computer Vision/OpenCV/Learn/Resources/lambo_2.jpg")

# img = cv2.resize(img, (300, 200))
while True:
    img = cv2.imread("E:/Computer Vision/OpenCV/Learn/Resources/lambo_2.jpg")
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    h_min = cv2.getTrackbarPos("Hue Min ", window_name)
    h_max = cv2.getTrackbarPos("Hue Max ", window_name)

    s_min = cv2.getTrackbarPos("Sat Min ", window_name)
    s_max = cv2.getTrackbarPos("Sat Max ", window_name)

    v_min = cv2.getTrackbarPos("Val Min ", window_name)
    v_max = cv2.getTrackbarPos("Val Max ", window_name)
    print(f"({h_min} - {h_max}) | ({s_min} - {s_max}) | ({v_min} - {v_max})")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(img_hsv, lower, upper)

    img_result = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("Image", img)
    # cv2.imshow("HSV Image", img_hsv)
    # cv2.imshow("Mask Image", mask)
    # cv2.imshow("Result Image", img_result)

    img_stack = stack_image(0.8, ([img, img_hsv], [mask, img_result]))

    cv2.imshow("Output ", img_stack)

    cv2.waitKey(1)