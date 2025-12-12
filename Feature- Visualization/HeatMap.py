import matplotlib.pyplot as plt
import cv2
img = cv2.imread('input image.jpg') #write image path here
plt.imshow(img,cmap = 'hot')

plt.show()
