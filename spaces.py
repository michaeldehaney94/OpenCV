import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/ea11a59953bc7d1dd0df7edef995ff89.jpg')
cv.imshow('Woman', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#  BGR to L.A.B
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)