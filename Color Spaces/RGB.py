#python program to read imgae as RGB
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals/cube.jpg')
plt.imshow(img)
plt.show()