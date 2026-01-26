import cv2
import numpy as np
src = 'sample image.jpg'  #paste input image path
input_image = cv2.imread(src)
if input_image is None:
    print('Could not load image', input_image)
    exit(0)
blue,green,red = cv2.split(input_image)

#create a dummy 3d array
blue_channel = np.zeros(input_image.shape,input_image.dtype)
green_channel = np.zeros(input_image.shape, input_image.dtype)
red_channel = np.zeros(input_image.shape, input_image.dtype)

#we match each color channel to a 3D dimension:
#blue rendering :[blue;0;0]
#green rendering :[0;green;0]
#red rendering: [0;0;red]

cv2.mixChannels([blue,green,red], [blue_channel],[0,0])
cv2.mixChannels([blue,green,red], [green_channel],[1,1])
cv2.mixChannels([blue,green,red], [red_channel],[2,2])

#Display the three obtained images
cv2.imshow('Blue Channel',blue_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Green Channel',green_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Red Channel',red_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

