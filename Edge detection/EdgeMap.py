import cv2
img = cv2.imread('D:/4th year/10th SEM - INTERIM SEM 2025-26/CSE3010/Practicals/cube.jpg')
laplacian = cv2.Laplacian(img,cv2.CV_64F)
#shows the image
cv2.imshow('EdgeMap image',laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()