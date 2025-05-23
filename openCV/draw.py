import cv2 as cv
import numpy as np

blank = np.zeros((500, 500,3), dtype='uint8')
cv.imshow('Blank', blank)

# img = cv.imread('images/495452c76e063bff.jpeg')
# cv.imshow('Girl', img)

# #  paint the blank image a certain color
# blank[200:300,300:400] = 0,0,255
# cv.imshow('Green', blank)

# draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('rectangle', blank)

#  draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# draw a line
cv.line(blank, (100,250),(300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# write text on an image
cv.putText(blank, 'Hello Michael!', (225,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)


cv.waitKey(0)