import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while 1:

    if cv2.waitKey(1) == ord('q'):
        break

    # Take frame
    success, frame = cam.read()
    # make it grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # get rid of noise on image by using blur
    img = cv2.medianBlur(gray_frame, 37)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=40)

    if not circles is None:
        circles = np.uint16(np.around(circles))

        # Obtain best circle
        max_r, max_i = 0, 0
        for i in range(len(circles[:, :, 2][0])):
            if circles[:, :, 2][0][i] > 50 and circles[:, :, 2][0][i] > max_r:
                max_i = i
                max_r = circles[:, :, 2][0][i]
        x, y, r = circles[:, :, :][0][max_i]
        print(x, y, r)
        print(frame.shape)

        # Take square field
        if y > r and x > r:
            square = frame[y - r:y + r, x - r:x + r]

            # Average color of square
            color_of_square = np.average(square[square.shape[0] * 1 // 8:square.shape[0] * 7 // 8,
                                                square.shape[1] * 1 // 8:square.shape[1] * 7 // 8])
            print(color_of_square)

            # Left side of square
            zone_1 = square[square.shape[0] * 2 // 8:square.shape[0] * 6 // 8,
                     square.shape[1] * 1 // 8:square.shape[1] * 3 // 8]
            cv2.imshow("zone 1", zone_1)

            # Right side of square
            zone_2 = square[square.shape[0] * 2 // 8:square.shape[0] * 6 // 8,
                     square.shape[1] * 5 // 8:square.shape[1] * 7 // 8]
            cv2.imshow("zone 2", zone_2)

            # Upper side of square
            zone_3 = square[square.shape[0] * 1 // 8:square.shape[0] * 3 // 8,
                     square.shape[1] * 3 // 8:square.shape[1] * 5 // 8]
            cv2.imshow("zone 3", zone_3)

        # Mark circle
        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 0, 0), 3)
            cv2.circle(frame, (i[0], i[1]), i[2], (255, 255, 255), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow("camera", frame)

cv2.destroyAllWindows()
cam.release()
