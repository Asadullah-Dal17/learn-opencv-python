
import cv2 as cv 

img_path = '../../images/shapes_image.png'

img = cv.imread(img_path)
print(img.shape)

# drawing circles on the images to differentiate between images 
cv.circle(img, (350, 350), 100,(0,255,0), 50, cv.LINE_AA)
cv.circle(img, (350, 350), 50,(0,255,0), 25, cv.LINE_AA)
cv.circle(img, (350, 350), 25,(0,255,0), 12, cv.LINE_AA)
cv.circle(img, (350, 350), 12,(0,255,0), 6, cv.LINE_AA)
cv.circle(img, (350, 350), 3,(0,255,0), 1, cv.LINE_AA)

# image save dir path and name of iamges 
save_img_path = '../saved_image/save_image.png'
# saving the images in the directory 
cv.imwrite(save_img_path, img) # files names, mat(images) you want save here we are saving the img a mat object
cv.imshow('img', img)

cv.waitKey(0) 
cv.destroyAllWindows()