import cv2 as cv 

img =cv.imread('../../images/shapes_image.png')

Blurred_img = cv.blur(img, (33,33))
cv.imshow('img', img)
cv.waitKey(0)
cv.imshow('Blurred Image', Blurred_img)
cv.waitKey(0)