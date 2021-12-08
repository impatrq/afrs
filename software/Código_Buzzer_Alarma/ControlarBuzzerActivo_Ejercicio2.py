#############################################
#_____https://frambuesa-pi.blogspot.com/____#
#___https://github.com/frambuesa-pi/python__#
#############################################
# importamos la libreria GPIO
import RPi.GPIO as GPIO
# importamos la libreria time
import time
# desactivamos mensajes de error
GPIO.setwarnings(False)
# indicamos el uso de  la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BCM)
# indicamos que el GPIO18 es de salida de corriente
GPIO.setup(18,GPIO.OUT)
# solicitamos al usuario que introduzca los segundos de duracion
segundos_d=int(input("duracion del sonido (segundos): " ))
# guardo en una variable el momento actual en segundos
inicio=time.time()
# guardo en una variable el momento actual sumando los segundos de duracion
final=time.time()+segundos_d
# enviamos la orden de encender el timbre
GPIO.output(18, True)
# bucle, mientras la primera variable no supere a la segunda se repite el bucle
while inicio<=final:    
    # actualizo la variable para controlar el tiempo que ha pasado
    inicio=time.time()
else:
    # si la primera variable no es inferior a la segunda 
    # se ha superado el tiempo y paramos el sonido
    GPIO.output(18, False)
