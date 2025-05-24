import cv2 as cv

img = cv.imread('images/s-club.jpg')
# cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('grayscale', gray)

# assigning haarcascade xml to a variable
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
# print the number of faces found
# print(f'Number of faces found = {len(faces_rect)}')

# draw rectangle over detected face
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+h,y+h), (0,255,0), thickness=2)

# cv.imshow('Detected Faces', img)



cv.waitKey(0)