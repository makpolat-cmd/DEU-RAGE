import cv2
import numpy as np
from scipy.stats import itemfreq


def save_on_text(frame):
	sizes = np.shape(frame)
	frame2D=frame.reshape(sizes[0]*sizes[1],3)
	np.savetxt("photo_taken_from_py.txt",frame2D,fmt='%3d')

"""
def get_dominant_color(image, n_colors):
    pixels = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    flags, labels, centroids = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    palette = np.uint8(centroids)
    return palette[np.argmax(itemfreq(labels)[:, -1])]
"""

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv2.VideoCapture(0) 
cv2.namedWindow('camera')
cv2.setMouseCallback('camera', onMouse)

# Read and process frames in loop
success, frame = cameraCapture.read()


while success and not clicked:
    #cv2.waitKey(1)
    success, frame = cameraCapture.read()

    if cv2.waitKey( 1 ) == ord( 'q' ):
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 37)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,
                              1, 50, param1=120, param2=40)

    if not circles is None:
        circles = np.uint16(np.around(circles))
        max_r, max_i = 0, 0
        
        for i in range(len(circles[:, :, 2][0])):
            if circles[:, :, 2][0][i] > 50 and circles[:, :, 2][0][i] > max_r:
                max_i = i
                max_r = circles[:, :, 2][0][i]
        x, y, r = circles[:, :, :][0][max_i]
        
        if y > r and x > r:
            square = frame[y-r:y+r, x-r:x+r]

            #print(square)

            save_on_text(square)


            zone_0 = square[square.shape[0]*2//8:square.shape[0]
                            * 6//8, square.shape[1]*1//8:square.shape[1]*3//8]
            cv2.imshow('Zone0', zone_0)
            zone_0_color = np.mean(zone_0)

            zone_1 = square[square.shape[0]*1//8:square.shape[0]
                            * 3//8, square.shape[1]*3//8:square.shape[1]*5//8]
            cv2.imshow('Zone1', zone_1)
            zone_1_color = np.mean(zone_1)

            zone_2 = square[square.shape[0]*2//8:square.shape[0]
                            * 6//8, square.shape[1]*5//8:square.shape[1]*7//8]
            cv2.imshow('Zone2', zone_2)
            zone_2_color = np.mean(zone_2)

            #if img>=100:
                #print("STOP")
                
            #if zone_1_color >100 & zone_2_color >100 & zone_3_color>100:
                #print("STOP")
            
            red = np.mean(zone_1[:,:,2])
            blue = np.mean(zone_1[:,:,1])
            green = np.mean(zone_1[:,:,0])
            
            print(red)
            print(blue)
            print(green)
            
            if red > 150 and blue < 150 and green<100 :
                print("STOP")
            elif zone_1_color > 100:
                if (zone_0_color) > (zone_2_color):
                    print("RIGHT")
                else:
                    print("LEFT")
            else:
                if (zone_1_color) < (zone_0_color) and (zone_1_color) < (zone_2_color):
                    print("FORWARD")
                    
                    #elif sum(zone_0_color) < sum(zone_2_color):
                        #print("FORWARD AND LEFT")
                    #else:
                        #print("FORWARD AND RIGHT")


        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    cv2.imshow('camera', frame)


cv2.destroyAllWindows()
cameraCapture.release()# -*- coding: utf-8 -*-

