import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')

# To capture video from webcam
cap=cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img=cap.read()

    # Detect the faces 
    faces=face_cascade.detectMultiScale(img, 1.3, 5)

    # Draw the rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display 
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k= cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object 
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

