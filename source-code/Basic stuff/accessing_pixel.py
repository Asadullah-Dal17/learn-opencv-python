import cv2 as cv 

# reading image 
img = cv.imread('../../images/shapes_image.png')

# getting the pixel value x =100, y=100 location in images
blue,green, red = img[100,100]

print('blue:', blue, 'green:', green, 'red: ',red)

print('------------')
# Reading 5x5 region of images, from 0 t0 5 pixel(row, column)
counter =0
for row in range(3):
    for column in range(3):
        counter+=1
        print(counter, img[row,column], end=' ')
    print()