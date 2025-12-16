#import numpy and opencv
import numpy as np
import cv2
#read the image
img = cv2.imread("D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals2/clahe1.jpg",0)
#lab = cv2.cvtColor(bgr,cv2.COLOR_BGR2LAB)
#lab_planes = cv2.split(lab)

#A CLAHE object is created with a clip limit of 2.0
#and a tile grid size of 8x8 pixels.
#this limits contrast enhancement to prevent noise
clahe = cv2.createCLAHE(clipLimit= 2.0, tileGridSize= (8,8)) 

#apply() method is used to process the loaded image
# out = contrast enhanced output image
out = clahe.apply(img)
#lab = cv2.merge(lab_planes)
#bgr = cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)

#saving the enhanced image
cv2.imwrite('clahe_2.jpg',out)
#displaying the image as 'CLAHE image' in a output window
cv2.imshow('CLAHE image',out)
cv2.waitKey(0)
cv2.destroyAllWindows()