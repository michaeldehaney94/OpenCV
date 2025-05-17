import cv2 as cv

# read image
img = cv.imread('images/968full-jamila-velazquez.jpg')

# show the image
cv.imshow('Jamila', img)

cv.waitKey(0)

# read video
capture = cv.VideoCapture('videos/plant.mp4')

# use while loop to read video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()