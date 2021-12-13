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
    
    # Defing the point for circle 
    x = 300 
    y =300
    # draw the circle
    cv.circle(frame, center=(x, y), radius=100, color=(255,255,255), thickness=20,lineType=cv.LINE_AA)
    
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