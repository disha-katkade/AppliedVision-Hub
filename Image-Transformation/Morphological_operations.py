import cv2
import numpy as np
import matplotlib.pyplot as plt
# reading the image
img = cv2.imread('D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals/cube.jpg')
# setting up the kernel
kernel = np.ones((5,5),np.uint8)
plt.imshow(img)
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # erosion
erosion = cv2.erode(img,kernel)
plt.imshow(erosion)
plt.show()

# dilation
dilation = cv2.dilate(img,kernel)
plt.imshow(dilation)
plt.show()