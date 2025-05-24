import cv2 as cv
import numpy as np

img = cv.imread('images/f1648f7be469a9744343bfee84a9cf49 (1).jpg')
cv.imshow('Face', img)

# edge detection
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# laplacian method
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Lap', lap)

# sobel method
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('combined sobel', combine_sobel)








cv.waitKey(0)