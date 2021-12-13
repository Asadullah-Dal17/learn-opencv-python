import cv2 as cv 


img = cv.imread('../../saved_image/save_image.png')
cv.imshow('img', img)
cv.waitKey(0)
# selecting points or coordinates of images to crop, or pixels
starting_x =10
ending_x =200

starting_y =10
ending_y =250
# croping the region
crop_region = img[starting_y : ending_y , starting_x : ending_x]
cv.imshow('cropped region', crop_region)
cv.waitKey(0)