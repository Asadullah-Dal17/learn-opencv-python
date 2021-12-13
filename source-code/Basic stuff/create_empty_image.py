import cv2 as cv 
import numpy as np 
img = np.zeros((200,200,3), dtype =np.uint8)
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()