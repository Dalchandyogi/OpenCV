import  cv2
import numpy as np

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

def get_contours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if 500 < area < 50000:  # filter by area
            cv2.drawContours(img_counter, [cnt], -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))

            obj_cor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if obj_cor == 3:
                object_type ="Triangle"
            elif obj_cor == 4:
                aspect_ratio = w/float(h)
                if 0.90 < aspect_ratio < 1.5:
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif obj_cor > 4 or obj_cor < 9:
                object_type = "Circle"
            else:object_type="None"

            cv2.rectangle(img_counter, (x,y), (x+w, y+h), (0,0,0), 2)
            cv2.putText(img_counter, object_type,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0,0,0), 1)



path = r"E:/Computer Vision/OpenCV/Learn/Resources/shapes.png"

img = cv2.imread(path)
img_blank = np.zeros_like(img)

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_grey, (7,7), 1)
img_canny = cv2.Canny(img_blur, 150, 200)


img_counter = img.copy()

get_contours(img_canny)

image_stack = stack_image(0.7, ([img, img_grey, img_blur], [img_canny, img_counter, img_blank]))

cv2.imshow("Output", image_stack)

cv2.waitKey(0)