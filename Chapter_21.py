import cv2 as cv 
import numpy as np

# Function to handle trackbar positions
def slider(pos):
    pass

path = 'image4.jpg'
img = cv.imread(path)

# Resize the image
img = cv.resize(img, (640, 480))

# Convert to HSV (Hue, Saturation, Value)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Create the window for trackbars
cv.namedWindow('Bars')
cv.resizeWindow('Bars', 900, 300)

# Create trackbars
cv.createTrackbar('Hue Min.', 'Bars', 0, 179, slider)
cv.createTrackbar('Hue Max.', 'Bars', 179, 179, slider)
cv.createTrackbar('Sat Min.', 'Bars', 0, 255, slider)
cv.createTrackbar('Sat Max.', 'Bars', 255, 255, slider)
cv.createTrackbar('Val Min.', 'Bars', 0, 255, slider)
cv.createTrackbar('Val Max.', 'Bars', 255, 255, slider)

while True:
    # Get the current trackbar positions
    hue_min = cv.getTrackbarPos('Hue Min.', 'Bars')
    hue_max = cv.getTrackbarPos('Hue Max.', 'Bars')
    sat_min = cv.getTrackbarPos('Sat Min.', 'Bars')
    sat_max = cv.getTrackbarPos('Sat Max.', 'Bars')
    val_min = cv.getTrackbarPos('Val Min.', 'Bars')
    val_max = cv.getTrackbarPos('Val Max.', 'Bars')
    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)

    # Create lower and upper bounds for color detection
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    # Create a mask and apply it to the image
    mask_img = cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img, img, mask=mask_img)

    # Show the original and masked images
    cv.imshow('Original', img)
    cv.imshow('HSV', hsv_img)
    cv.imshow('Mask', mask_img)
    cv.imshow('Final Output', out_img)

    # Exit the loop when 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break   

cv.destroyAllWindows()


