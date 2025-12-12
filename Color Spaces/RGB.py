#python program to read imgae as RGB
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('input image.jpg')   #input image path
plt.imshow(img)

plt.show()
