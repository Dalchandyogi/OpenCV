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


img = cv2.imread("E:/Computer Vision/OpenCV/Learn/Resources/lena.jpeg")
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

stac_images = stack_image(1, ([img, img_grey, img], [img_grey, img, img_grey]))


cv2.imshow("Stack Images",stac_images)

cv2.waitKey(0)