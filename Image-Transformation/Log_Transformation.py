#Log Transformation
import cv2
import  matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals/cube.jpg',0)
log = 0.6 *(np.log(1+np.float32(img)))

fig = plt.figure(figsize=(15,5))
ax = fig.add_subplot(121)
plt.title('Original', fontsize=18)
plt.imshow(img,cmap = 'gray')
ax = fig.add_subplot(122)
plt.imshow(log,cmap='gray')
ax.set_title('Log Transform',fontsize = 18)
plt.show()

