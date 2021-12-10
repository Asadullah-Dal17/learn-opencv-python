import cv2 as cv

img  = cv.imread('../images/shapes_image.png') #reading image from dir
# converting color image into grayscale image 
gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('colored', img)
cv.imshow('GrayScale', gray_scale)
cv.waitKey(0)

