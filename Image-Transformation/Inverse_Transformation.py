#Linear Transformation
import cv2
import  matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals/cube.jpg',0)
img_inverse = 255 - img

fig = plt.figure(figsize=(15,5))
ax = fig.add_subplot(121)
plt.title('Original', fontsize=18)
plt.imshow(img,cmap = 'gray')
ax = fig.add_subplot(122)
plt.imshow(img_inverse,cmap='gray')
ax.set_title('Inverse Transform',fontsize = 18)
plt.show()