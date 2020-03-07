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
change_res(160,120)

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

# Loop
while True:

	# Take a frame from camera
	check, frame = pc_cam.read()

	# Rescale frame
	frame_rescaled = rescale_frame(frame, 50)

	# Debug
	print(np.shape(frame))
	print(np.shape(frame_rescaled))
	
	# Display
	cv2.imshow("original",frame)
	cv2.imshow("rescaled",frame_rescaled)

	# Condition to stop (keyboard input)
	if cv2.waitKey(1) == ord('q'):
		break

# Release camera
pc_cam.release()
