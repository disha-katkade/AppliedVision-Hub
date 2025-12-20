#Blurring an image

import cv2
img = cv2.imread('D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals/cube.jpg')
cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
blur_image = cv2.medianBlur(img,13)
cv2.imshow('blur image',blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()