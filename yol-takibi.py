import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while 1:

    if cv2.waitKey(1) == ord('q'):
        break

    # Take frame
    success, frame = cam.read()
    # make it grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.medianBlur(gray, 9)
    # get edges of image
    edges = cv2.Canny(gray_frame, 100, 150, apertureSize=3)
    # work on bottom side of image
    line_length = 100

    edges[edges.shape[0] * 0 // 16:edges.shape[0] * 11 // 16, :] = 0
    edges[edges.shape[0] * 14 // 16:edges.shape[0] * 16 // 16, :] = 0
    line_length = 50

    # detect lines
    lines = cv2.HoughLinesP(edges, 2, np.pi/180, 200, minLineLength=line_length, maxLineGap=10, )

    if lines is not None:
        for d in lines:

            x1, y1, x2, y2 = d[0]

            cv2.line(gray, (x1, y1), (x2, y2), (0, 0, 0), 3)
            cv2.line(gray, (x1, y1), (x2, y2), (255, 0, 255), 2)

    cv2.imshow("original", gray)
    cv2.imshow("edges", edges)

cv2.destroyAllWindows()
cam.release()
