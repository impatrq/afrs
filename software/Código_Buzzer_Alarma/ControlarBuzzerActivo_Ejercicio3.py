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
# solicitamos al usuario que introduzca los segundos de duracion total
segundos_d=int(input("duracion del sonido (segundos): " ))
# solicitamos al usuario el tiempo del sonido activo
tiempo_sonido=float(input("duracion del sonido intermitente (segundos): "))
# solicitamos al usuario el tiempo del sonido en pausa
tiempo_silencio=float(input("duracion del silencio intermitente (segundos): "))
# guardo en una variable el momento actual en segundos
inicio=time.time()
# guardo en una variable el momento actual mas los segundos de duracion
final=time.time()+segundos_d
# mientras la primera variable no supere a la segunda se repite el bucle
while inicio<final:
    # enviamos la orden de encender el timbre
    GPIO.output(18, True)
    # con esta orden mantenemos el sonido el tiempo indicado
    time.sleep(tiempo_sonido)
    # enviamos la orden de apagar el timbre
    GPIO.output(18, False)
    # con esta orden mantenemos el silencio el tiempo indicado
    time.sleep(tiempo_silencio)
    # actualizo la variable para controlar el tiempo que ha pasado
    inicio=time.time()
else:
    # si la primera variable no es inferior a la segunda 
    # se ha superado el tiempo y paramos el sonido
    GPIO.output(18, False)