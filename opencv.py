
# Convert recorded video to greyscale

import cv2

# Create a VideoCapture object and pass the path to your video file 
cap=cv2.VideoCapture('Video.mp4')

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly ret is True 
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here. Here we convert the frame to grayscale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    # The 'q' button is set as the break 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything done, release the VideoCapture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
