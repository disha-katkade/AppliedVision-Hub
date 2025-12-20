import cv2
from matplotlib import pyplot as plt
import PIL as pillow
import numpy as np

img = cv2.imread('D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals/sample image.jpg')
# plt.imshow(img)
# plt.show()

# imagem = cv2.bitwise_not(img)   #arithmetic operators flips binary 0 to 1 and vice versa
# plt.imshow(imagem)
# cv2.imwrite('output.jpeg',imagem)
# plt.show()

# how arithmetric operator actually changes the image
from PIL import Image  #pillow library
from numpy import array  #to convert image into image matrix - array function is used
im1 = Image.open("D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals/sample image.jpg")
ar1 = array(im1)
print(ar1)

im2 = Image.open("Output.jpeg")
ar2 = array(im2)
print(ar2)
