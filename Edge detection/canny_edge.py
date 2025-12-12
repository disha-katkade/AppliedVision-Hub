# importing necessary libraries
import cv2
import matplotlib.pyplot as plt

# image reading and preproceesing
img = cv2.imread("input image path.jpg")   #write image path here
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(3,3),0)
#cv2.imshow("Original Image", img)
cv2.imshow("Original Image",imgRGB)

# canny edge detection
edges = cv2.Canny(image = img_blur, threshold1=100, threshold2=200)
edges = cv2.cvtColor(edges,cv2.COLOR_BGR2RGB)
cv2.imshow("Edges",edges)

cv2.waitKey(0)

cv2.destroyAllWindows()

