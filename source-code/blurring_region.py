import cv2 as cv 

img =cv.imread('../images/shapes_image.png')

cv.imshow('img', img)
cv.waitKey(0)
# define the Region of interests pixels coordinates 
min_x = 20
max_x = 300
min_y =30
max_y = 400
# cropping the image 
ROI  = img [min_y: max_y, min_x: max_x] # selected Region of image,(Region of intererst)
cv.imshow('ROI', ROI)
cv.waitKey(0)
