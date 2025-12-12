import matplotlib.pyplot as plt
import cv2
img = cv2.imread('input image.jpg')  #write input image path here
plt.imshow(img,cmap = 'nipy_spectral')

plt.show()
