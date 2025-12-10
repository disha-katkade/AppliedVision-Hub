#Import cv2 module
import cv2
#Read the image
img = cv2.imread('D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals/cube.jpg')

#convert to YCrCb color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#shows the image
cv2.imshow('HSV image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()