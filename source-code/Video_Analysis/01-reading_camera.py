import cv2 as cv 

# selecting camera by choosing the number 
CAMERA_NUMBER = 0
# create camera object 
cap = cv.VideoCapture(CAMERA_NUMBER)

while True:
    # getting frame(ret) available or not and frame its self.
    ret, frame = cap.read()
    if not ret:
        break
    cv.imshow('frame', frame)
    # define key to close the program
    key = cv.waitKey(1)
    if key ==ord('q'):
        # when 'q' press on Key board the program will quit 
        break
# close the camera 
cap.release()
# close all the windows
cv.destroyAllWindows()