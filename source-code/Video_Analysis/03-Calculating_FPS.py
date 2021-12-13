import cv2 as cv 
import time 

# selecting camera by choosing the number 
CAMERA_NUMBER = 0
# create camera object 
cap = cv.VideoCapture(CAMERA_NUMBER)

# starting time here 
start_time = time.time()

# create frame counter 
frame_counter =0
while True:
    # getting frame(ret) available or not and frame its self.
    ret, frame = cap.read()

    if not ret:
        break
    # starting counting frame here 
    frame_counter +=1
    # calculating the Frame Per Seconds 
    fps = frame_counter/(time.time() - start_time)
    print(f'FPS : {fps}')
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