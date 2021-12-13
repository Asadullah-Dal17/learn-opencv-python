import cv2 as cv 

img = cv.imread('../../images/shapes_image.png')
cv.imshow('img', img)
cv.waitKey(0)
# reducing the size of img by half  define by fx for width , fy for height
resized_img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
cv.imshow('resized image', resized_img)
cv.waitKey(0)