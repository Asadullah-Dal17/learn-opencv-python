import cv2 as cv 

img =cv.imread('../../images/shapes_image.png')

Gaussian_blur = cv.GaussianBlur(img , (33,33), 0)
cv.imshow('img', img)
cv.waitKey(0)
cv.imshow('Gaussain Blur', Gaussian_blur)
cv.waitKey(0)