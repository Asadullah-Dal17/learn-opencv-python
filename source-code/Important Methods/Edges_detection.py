import cv2 as cv 

img = cv.imread('../../images/shapes_image.png')
cv.imshow('img', img)
cv.waitKey(0)
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_scale', grayscale_img)
cv.waitKey(0)
# detecting Edges in the gray scale images 
edges_img = cv.Canny(grayscale_img, 30, 200)
cv.imshow("edges", edges_img)
cv.waitKey(0)
