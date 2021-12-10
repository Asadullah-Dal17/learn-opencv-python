import cv2 as cv

img  = cv.imread('../images/shapes_image.png') #reading image from dir
# converting color image into grayscale image 
gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('colored', img)
cv.imshow('GrayScale', gray_scale)
cv.waitKey(0)

# changing BGR image to RGB image 
RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB_img', RGB_img)
cv.waitKey(0)
