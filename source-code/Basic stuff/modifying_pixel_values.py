import cv2 as cv 
import numpy as np 

# reading the image for dir 
img = cv.imread('../../images/shapes_image.png')
cv.imshow('img', img)
cv.waitKey(0)

# modifying the pixel values x =0 to 300, y 0 to 300
for row in range(300):
    for column in range(300):
        img[row,column]=[0,255,0] #color replaceing every pixel

cv.imshow('modified', img)
cv.waitKey(0)

# modifying the pixel values x =0 to 300, y 0 to 300
for row in range(300):
    for column in range(300):
        img[row,column]=[255,255,0] #color replaceing every pixel

cv.imshow('modified2', img)
cv.waitKey(0)