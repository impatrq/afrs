import cv2

haar_file = (cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

while True:
    (_, im) = webcam.read()
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x,y), (x+w, y+h), (0, 0, 255), 1)

    cv2.imshow('OpenCV', im)

    key = cv2.waitKey(10)
    if key == 27:
        break