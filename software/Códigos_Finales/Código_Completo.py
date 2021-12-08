import RPI.GPIO as GPIO
import time
import cv2

cont, cont1, cont2, cont3 = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)						# SENSOR DE ALCOHOL
GPIO.setup(5, GPIO.OUT)

GPIO_TRIGGER = 2
GPIO_ECHO = 3
GPIO_TRIGGER1 = 4
GPIO_ECHO1 = 17

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)			# SENSOR ULTRASONICO 1
GPIO.setup(GPIO_ECHO, GPIO.IN)					
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)			# SENSOR ULTRASONICO 2
GPIO.setup(GPIO_ECHO1, GPIO.IN)

def alcohol():
	while True:
		if GPIO.input(11):
			time.sleep(0.1)
			dato = 0
		if GPIO.input(11)!=1:
			dato = 1
			GPIO.output(5, True)
			time.sleep(0.1)
			GPIO.output(5, False)
		return dato
		
def distance(): 
    GPIO.output(GPIO_TRIGGER, True)
 
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:               # guardar tiempo de inicio
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:               # guardar tiempo de llegada
        StopTime = time.time()
 
    tiempototal = StopTime - StartTime              # diferencia entre tiempos
    distance = (tiempototal * 34300) / 2

	if distance < 14:
		print ("Sin problemas (cabeza)")
	else:
		cont + 1

def distance2():
	GPIO.output(GPIO_TRIGGER1, True)

	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER1, False)

	StartTime = time.time()
	StopTime = time.time()

	while GPIO.input(GPIO_ECHO1) == 0:              # guardar tiempo de inicio
		StartTime = time.time()

	while GPIO.input(GPIO_ECHO1) == 1:              # guardar tiempo de llegada
		StopTime = time.time()

	tiempototal = StopTime - StartTime              # diferencia entre tiempos
	distance1 = (tiempototal * 34300) / 2

	if distance1 < 12:
		print ("Todo en orden (cuello)")
	else:
		cont1 + 1
 
def webcam1():
    cap = cv2.VideoCapture(1)

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
    key = cv2.waitKey(10)

    if (len(faces) == 0):
        print("No detecto rostro")
		cont2 + 1
    else:
        print("Detecto rostro")

def webcam2():
    frame = cv2.imread('foto.png')

    haar_file = (cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
    eye_cascade = cv2.CascadeClassifier(haar_file)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    for (x, y, w, h) in eyes:
	    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 1)
    cv2.imshow('OpenCV', frame)
    key = cv2.waitKey(10)

    if (len(eyes)>0):
        print("Detecto ojos")
    else:
        print("No detecto ojos")
		cont3 + 1

def alarma():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18, True)

# correr las funciones ya hechas

alcholimetro=alcohol()			# traemos el dato del sensor de alcoholemia
if alcholimetro == 1: 			# positivo de alcohol
	alarma()
	print ("Detecto alcohol, espere 5 mins")
	time.sleep (5)

else:							# no detecto alcohol, sigue el programa
	print("Sin problemas")
	
while True:
	dist = distance()
	dist1 = distance2()
	webcam1()
	webcam2()
	time.sleep (1)
	if cont == 5:
		alarma()
		print ("Distancia peligrosa (cabeza)")
		cont = 0
	if cont1 == 5:
		alarma()
		print ("Distancia peligrosa (cuello)")
		cont1 = 0
	if cont2 == 5:
		alarma()
		print ("Rostro no detectado")

	if cont3 == 5:
		alarma()
		print ("Ojos no detectados")	


