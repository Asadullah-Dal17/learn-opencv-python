
import cv2 as cv 

img_path = '../images/shapes_image.png'

img = cv.imread(img_path)
print(img.shape)

# drawing circles on the images to differentiate between images 
cv.circle(img, (350, 350), 100,(0,255,0), 50, cv.LINE_AA)
cv.circle(img, (350, 350), 50,(0,255,0), 25, cv.LINE_AA)
cv.circle(img, (350, 350), 25,(0,255,0), 12, cv.LINE_AA)
cv.circle(img, (350, 350), 12,(0,255,0), 6, cv.LINE_AA)
cv.circle(img, (350, 350), 3,(0,255,0), 1, cv.LINE_AA)

# writing the image in dir 

cv.imshow('img', img)

cv.waitKey(0) 
cv.destroyAllWindows()