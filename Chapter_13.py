# Basic functions or manipulation in open cv 

import cv2 as cv 
import numpy as np

img=cv.imread('image5.jpg')

# Resize
resized_img= cv.resize(img, (450, 250))

# Gray 
gray_img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Blurred image 
blurred_img= cv.GaussianBlur(img, (23, 23), 0)

# Edge detection
edge_img= cv.Canny(img, 53,53)

# Thickness of lines 
mat_kernel= np.ones((3,3), np.uint8)
dilated_img= cv.dilate(edge_img, (mat_kernel), iterations=1)

# Make thinner outline 
ero_img= cv.erode(dilated_img, mat_kernel, iterations=1)

# Cropping we will use numpy library not openCV
print("This size of our image is:", img.shape)
cropped_img=img[0:600, 0:600]

# cv.imshow('Original', img)
# cv.imshow("Resized", resized_img)
# cv.imshow("Gray", gray_img)
# cv.imshow("Blurr", blurred_img)
# # make black and white image 
# cv.imshow("Edge", edge_img)
# cv.imshow("Dilated", dilated_img)
# cv.imshow("Erosion", ero_img)
cv.imshow("Cropped", cropped_img)

cv.waitKey(0)
cv.destroyAllWindows()
