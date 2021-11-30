import cv2 as cv 
import numpy as np

print(f'opencv_version: {cv.__version__}')

img = np.zeros((500,500, 3), dtype=np.uint8)
cv.putText(img, f'version: {cv.__version__}', (100, 250), cv.FONT_HERSHEY_PLAIN, 2.4, (0,255,0), 2, cv.LINE_AA)
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()