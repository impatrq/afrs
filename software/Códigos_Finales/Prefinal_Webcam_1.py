import cv2
import time

def webcam1():
    cap = cv2.VideoCapture(0)

    haar_file = (cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(haar_file)

    leido, frame = cap.read()
    if leido == True:
	    cv2.imwrite("foto.png", frame)
    else:
        cap.release()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
	    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 1)
    cv2.imshow('OpenCV', frame)
    cont = 0
    if (len(faces) == 0):
        print("No detecto rostro")
        cont = cont +1
    else:
        print("Detecto rostro")
    return cont

def webcam2():
    frame = cv2.imread('foto.png')
    cont = 0
    haar_file = (cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
    eye_cascade = cv2.CascadeClassifier(haar_file)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    for (x, y, w, h) in eyes:
	    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 1)
    cv2.imshow('OpenCV', frame)
    
    if (len(eyes)>0):
        print("Detecto ojos")
    else:
        print("No detecto ojos")
        cont = cont + 1

    return cont

cont2 = 0
cont3 = 0

while True:
    key = cv2.waitKey(10)
    cam1 = webcam1()
    cam2 = webcam2()
    time.sleep(1)                              # reducir desps de probar 
    if cam1 == 1:
        cont2 = cont2 + 1
        print (cont2)
        if cam2 == 1:
            cont3 = cont3 + 1
            if cont2 == 5:
                print ("alarmashe")
                cont2 == 0
                if cont3 == 5:
                    print ("alarmashe2")
                    cont3 = 0
                    if key == 27:
                        break 

