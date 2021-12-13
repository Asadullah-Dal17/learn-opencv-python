import cv2 as cv 

# sselecting the path for video file here 
video_file_path = '../../video/test.mp4'
# create camera object 
cap = cv.VideoCapture(video_file_path)

while True:
    # getting frame(ret) available or not and frame its self.
    ret, frame = cap.read()
    if not ret:
        break
    cv.imshow('frame', frame)
    # define key to close the program
    key = cv.waitKey(1)
    if key ==ord('q'):
        # when q is press the program will quit
        break
# close the camera 
cap.release()
# close all the windows
cv.destroyAllWindows()