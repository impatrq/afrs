import RPi.GPIO as GPIO                             #Libraries
import time
 
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18                                   # sensor 1 arreglar**
GPIO_ECHO = 24

GPIO_TRIGGER1 = 11                                  # sensor 2 arreglar**
GPIO_ECHO1 = 22

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)                  # setear entradas del sensor 1
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)                 # setear entradas del sensor 2
GPIO.setup(GPIO_ECHO1, GPIO.IN)

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
 
    return distance

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
 
    return distance1

dist = distance()                                   # Sensor del cuello 
print ("Distancia medida = %.1f cm" % dist)         # esto no es necesario
if dist > 20:
    cont =+ 1
    if cont > 5:
        print ("alarma")
    cont = 0 
    dist1 = distance2()                             # Sensor de la cabeza
    print ("Distancia medida = %.1f cm" % dist1)    # esto no es necesario
    if dist1 > 15:
        cont1 =+ 1
        if cont1 > 5:
            print ("alarma")
        else:
            cont1 = 0
            # seguir con el codigo...