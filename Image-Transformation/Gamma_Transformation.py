#Gamma Transformation
import cv2
import  matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('input image.jpg',0)
img1 = img/255.0
img_power_law_transformation = cv2.pow(img1,1.8) #to change the size of the figure

fig = plt.figure(figsize=(15,5))
ax = fig.add_subplot(121)
plt.title('Original', fontsize=18)
plt.imshow(img,cmap = 'gray')
ax = fig.add_subplot(122)
plt.imshow(img_power_law_transformation,cmap='gray')
ax.set_title('Power Law Transform',fontsize = 18)

plt.show()
