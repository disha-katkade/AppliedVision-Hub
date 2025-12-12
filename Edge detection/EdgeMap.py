import cv2
img = cv2.imread('input image.jpg')
laplacian = cv2.Laplacian(img,cv2.CV_64F)
#shows the image
cv2.imshow('EdgeMap image',laplacian)
cv2.waitKey(0)

cv2.destroyAllWindows()
