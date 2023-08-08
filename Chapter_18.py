# How to change the perspective image 

import cv2 as cv 
import numpy as np 

img= cv.imread('warp.png')
print(img.shape)

# defining points 
point1= np.float32([[233, 196], [82, 471], [522,169], [715, 482]])

width=800
height=900
width, height=800,900

point2=np.float32([[0,0], [800,0], [0, height], [width, height]])

matrix=cv.getPerspectiveTransform(point1, point2)
out_img=cv.warpPerspective(img, matrix, (width, height))

# out_img=cv.resize

cv.imshow('Original', img)
cv.imshow('transformed', out_img)
cv.imwrite('warp_perspective.png', out_img)
cv.waitKey(0)
cv.destroyAllWindows()