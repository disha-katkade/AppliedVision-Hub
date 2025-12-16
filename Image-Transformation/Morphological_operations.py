import cv2
import numpy as np
import matplotlib.pyplot as plt
# reading the image
img = cv2.imread('input image.jpg')   #put input image here
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
