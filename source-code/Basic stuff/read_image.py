# importing the modules 
import cv2 as cv 

# providing the image path /location of images in dir
img_path = '../../images/shapes_image.png'

# reading images from dirctory 
img = cv.imread(img_path)

# showing the image with windows, this function takes, window-name and mat object or img 
cv.imshow('img', img)

# in order to control the time, makes window wait til we quit, cv.waitKey function is used 
cv.waitKey(0) # this function takes waiting time in millseconds, 0 means wait forever, or until we press key on keyboard

# closing the opened windows
cv.destroyAllWindows()