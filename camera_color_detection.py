import cv2, time
import numpy as np

# Define camera object. Zero for PC cam
pc_cam = cv2.VideoCapture(0)

# Define resolution functions
def make_1080p():
    pc_cam.set(3, 1920)
    pc_cam.set(4, 1080)

def make_720p():
    pc_cam.set(3, 1280)
    pc_cam.set(4, 720)

def make_480p():
    pc_cam.set(3, 640)
    pc_cam.set(4, 480)

# For specific resolution value
def change_res(width, height):
    pc_cam.set(3, width)
    pc_cam.set(4, height)

# Set res
make_1080p()
# or
change_res(640,480)

# Rescale frame
def rescale_frame(frame, percent):
	width = int(frame.shape[1] * percent / 100)
	height = int(frame.shape[0] * percent / 100)
	dimention = (width,height)
	return cv2.resize(frame, dimention, interpolation = cv2.INTER_AREA)

# Print frame data to text file
def save_on_text(frame):
	sizes = np.shape(frame)
	frame2D=frame.reshape(sizes[0]*sizes[1],3)
	np.savetxt("photo_taken_from_py.txt",frame2D,fmt='%3d')

# Paint frame
def square_frame(frame,point,size):
	for x in range(-size,size+1):
		frame[point[0]+size,point[1]+x] = [0,250,0]
		frame[point[0]-size,point[1]+x] = [0,250,0]
	for x in range(-size,size+1):
		frame[point[0]+x,point[1]+size] = [0,250,0]
		frame[point[0]+x,point[1]-size] = [0,250,0]

# Detect color
def color_detection(frame):
	for x in range(10,frame.shape[0]-10,5):
		for y in range(10,frame.shape[1]-10,5):

			# Color parameters are defined here.
			color = (frame[x,y,0]/2)-(frame[x,y,1]/4)-(frame[x,y,2]/4)
			# Condition to mark that area
			if color>20:
				square_frame(frame,(x,y),5)


# Loop
while True:

	# Take a frame from camera
	check, frame = pc_cam.read()

	# Rescale frame
	frame_rescaled = rescale_frame(frame, 50)

	# Debug
	
	# Modifications 
	color_detection(frame)

	# Display
	cv2.imshow("original",frame)
	cv2.imshow("rescaled",frame_rescaled)

	# Condition to stop (keyboard input)
	if cv2.waitKey(1) == ord('q'):
		break

# Release camera
pc_cam.release()
