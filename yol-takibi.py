import cv2
import numpy as np

cam = cv2.VideoCapture(0)

line_counter, Right, Left = 0, 0, 0

while 1:

    if cv2.waitKey(1) == ord('q'):
        break

    # Take frame
    success, frame = cam.read()
    # make it grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.medianBlur(gray, 5)
    # get edges of image
    edges = cv2.Canny(gray_frame, 100, 200, apertureSize=3)

    # work on bottom side of image
    edges[edges.shape[0] * 0 // 16:edges.shape[0] * 11 // 16, :] = 0
    edges[edges.shape[0] * 13 // 16:edges.shape[0] * 16 // 16, :] = 0
    line_length = 1

    # detect lines
    lines = cv2.HoughLinesP(edges, 2, np.pi/180, 100, minLineLength=line_length, maxLineGap=25)

    if lines is not None:

        Left_position, Right_position = 0, 0
        for d in lines:
            x1, y1, x2, y2 = d[0]
            line_counter += 1
            print(line_counter)

            # Check if the line is worth investigating
            if y2-y1 == 0:
                print("Invalid")
                continue
            m = (x2-x1)/(y2-y1)
            if not 0.25 < abs(m) < 4:
                print("Invalid")
                continue

            cv2.circle(frame, (x1, y1), 2, (0, 200, 0), 5)
            cv2.circle(frame, (x2, y2), 2, (0, 200, 0), 5)

            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 0), 3)
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)

            p = (x1 + x2) / 2
            if p < frame.shape[1] / 2:
                Left_position = frame.shape[1] / 2 - p
                Left = True
                print("Left += 1 --> ", Left)
            else:
                Right_position = p - frame.shape[1] / 2
                Right = True
                print("Right += 1 --> ", Right)

            if line_counter > 5:
                line_counter = 0
                isForward = Left and Right
                if isForward:
                    Direction = Left_position - Right_position
                    if -50 < Direction < 50:
                        print("Forward")
                    elif Direction <= -50:
                        print("Turn Right")
                    else:
                        print("Turn Left")
                else:
                    print("Stop")

                Right, Left = False, False



    cv2.imshow("original", frame)
    cv2.imshow("edges", edges)

cv2.destroyAllWindows()
cam.release()
