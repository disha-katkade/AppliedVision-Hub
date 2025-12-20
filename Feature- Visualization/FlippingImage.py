import cv2
from matplotlib import pyplot as plt

#reading the image
img = cv2.imread('D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals/cube.jpg')
# name = '0penCV python image'
# plt.title(name)
# plt.imshow(img)
# plt.show()

#Flipping the image horizontally
# horizontal_flip = cv2.flip(img,1)
# name ='OpenCV python flip image horizontally'
# plt.title(name)
# plt.imshow(horizontal_flip)
# plt.show()

#flipping the image vertically
# vertical_flip = cv2.flip(img,0)
# name = 'OpenCV python flip image vertically'
# plt.title(name)
# plt.imshow(vertical_flip)
# plt.show()

#flipping the image horizontally and vertically
vertical_horizontal_flip = cv2.flip(img,-1)
name = 'OpenCV python flip image Both horizontally and vertically'
plt.title(name)
plt.imshow(vertical_horizontal_flip)
plt.show()

