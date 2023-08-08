#edge detection
import cv2
cap=cv2.VideoCapture(0) # built-in camera

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # add edge detection
    edges=cv2.Canny(frame, threshold1=50, threshold2=200)

    # Display the resulting frame
    cv2.imshow('Video', edges)
    
    # The 'q' button is set as the break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# destroy all the windows 
cv2.destroyAllWindows()