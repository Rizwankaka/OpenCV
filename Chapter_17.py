# Joining two images 

import cv2 as cv 
import numpy as np 

img= cv.imread('image4.jpg')

# stacking same imge 

# #1. Horizontal stack 
# hor_stack= np.hstack((img, img))

#2. Vertical stack 
ver_stack= np.vstack((img, img))

# cv.imshow("Horizontal", hor_stack)
cv.imshow("Vertical", ver_stack)
cv.waitKey(0)
cv.destroyAllWindows()

# you can only stack images with same shape (width, height, color channel)
# we can not resize the stack image (function)
# same number of channels np function
(600, 500, 3)
# you have to define a function to stack multiple images of different sizes and tunes 