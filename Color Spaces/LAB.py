#Import cv2 module
import cv2
#Read the image
img = cv2.imread('input image.jpg')  #paste input image path

#convert to YCrCb color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

#shows the image
cv2.imshow('LAB image',img)
cv2.waitKey(0)

cv2.destroyAllWindows()

