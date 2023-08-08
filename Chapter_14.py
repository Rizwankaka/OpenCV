# How to draw lines, and shapes in python 

import cv2 as cv 
import numpy as np


# Draw a canvas 0 is for black
img= np.zeros((600,600))
img1=np.ones((600,600))

# print size 
print('The size of our canvas is:', img.shape)
# print(img)

# adding colors to the canvas 
colored_img=np.zeros((600,600,3), np.uint8) # color channel addition 

colored_img[:]= 255, 0, 255 # color complete image 

colored_img[150:230, 100:500]= 255, 168, 155 # part of image to be colored 

# adding line 
cv.line(colored_img, (0, 0), (colored_img.shape[0], colored_img.shape[1]), (255, 0, 0), 3) # crossed line
cv.line(colored_img, (20, 20), (300, 300), (255, 255, 50), 3) # part line 

# adding rectangle 
cv.rectangle(colored_img, (50,100), (300,400), (255, 255, 255), 3) # 3 at last is thickness of line
cv.rectangle(colored_img, (50,100), (300,400), (255, 255, 255), 100) # increase the thickness..see
cv.rectangle(colored_img, (50,100), (300,400), (255, 255, 255), cv.FILLED) # fill the rectangle

# adding circle 
cv.circle(colored_img,(400, 300),50, (255, 100, 0), 5)
cv.circle(colored_img,(400, 300),50, (255, 100, 0), cv.FILLED) # fill the circle 

# adding text 
cv.putText(colored_img, "Learning Artificial Intelligence", (200,500), cv.FONT_HERSHEY_DUPLEX,1, (255, 255, 0), 1)

# cv.imshow('black', img)
# cv.imshow('white', img1)
cv.imshow('Colored', colored_img)
cv.waitKey(0)
cv.destroyAllWindows()

