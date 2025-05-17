import cv2 as cv
import numpy as np
from numpy.ma.core import resize

img = cv.imread('images/53605263f8b46b402d56b640442bca24.jpg')
cv.imshow('Sonequa', img)

# translate image
def translate(img, x, y,):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# shifting:
# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -90)
cv.imshow('Rotate Twice',rotated_rotated)

# resizing
resized = cv.resize(img, (600,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resizing', resized)


# flipping
# flipCode - 0, 1, -1
flip =cv.flip(img, 1)
cv.imshow('Flip', flip)

# cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)