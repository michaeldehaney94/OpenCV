import cv2 as cv

# rescaling resolution function for static video
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# alternative rescaling resolution function for image and live video
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# read image
img = cv.imread('images/968full-jamila-velazquez.jpg')
# show the image
# cv.imshow('Image', img)

resized_img = rescaleFrame(img)
cv.imshow('Image', resized_img)

# cv.waitKey(0)


# read video
capture = cv.VideoCapture('videos/plant.mp4')

# use while loop to read video frame by frame
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()