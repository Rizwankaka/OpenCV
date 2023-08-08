# face detection using OpenCv

import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# read the image 
img= cv2.imread('image4.jpg')

# detect faces 
faces=face_cascade.detectMultiScale(img,1.3,5)

# draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img,(x, y),(x+w, y+h),(255, 0, 0), 2)

# display the output
cv2.imshow('img', img)
cv2.waitKey()