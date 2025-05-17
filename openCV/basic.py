import cv2 as cv
from numpy.ma.core import resize

img = cv.imread('images/nathalie-emmanuel-gq-april-2015.jpg')
# cv.imshow('Cat', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# blurring an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# edge cascade / edge detector
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)


# Dilating the image edges to make the edges thicker
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# eroding the image
eroded = cv.erode(canny, (3,3), iterations=1)
# cv.imshow('Eroded', eroded)


# resize image
resized = cv.resize(img, (700, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# cropping an image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)