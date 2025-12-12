#Read an image, store, change the color, show it, write in a file
import cv2
path = 'input image.jpg'   #write input image path here
img2 = cv2.imread(path)
#img = cv2.imread(path,0) --- gray
#img1 = cv2.imread(path,-1) --- unchanged
#img2 = cv2.imread(path,1)
while(True):
    cv2.imshow('color image',img2)
    a = input('Do you break? y/n')
    if a== 'y':
        break
file = input('Enter the image name to be saved')

cv2.imwrite(file+'.jpg',img2)
