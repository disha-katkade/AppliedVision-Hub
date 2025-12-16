#import opencv
import cv2
#import numpy
import numpy as np
#read an image using imread
img = cv2.imread("D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals2/clahe1.jpg",0)
#creating a histograms equalization
#of an image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)
#stacking images side-by-side
res = np.hstack((img,equ))
#show image input vs output
cv2.imshow('img',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

