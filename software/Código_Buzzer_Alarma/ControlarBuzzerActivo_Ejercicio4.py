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
# definimos una funcion que recibe tres parametros y que genera con un
# bucle el sonido intermitente
def encender_timbre(tiempo_total,tiempo_activo,tiempo_pausa):
    # guardo en una variable el momento actual en segundos
    inicio=time.time()
    # guardo en una variable el momento actual mÃ¡s los segundos de duracion
    final=time.time()+tiempo_total
    # mientras la primera variable no supere a la segunda se repite el bucle
    while inicio<final:
        # enviamos la orden de encender el timbre
        GPIO.output(18, True)
        # con esta orden mantenemos el sonido el tiempo indicado
        time.sleep(tiempo_activo)
        # enviamos la orden de apagar el timbre
        GPIO.output(18, False)
        # con esta orden mantenemos el silencio el tiempo indicado
        time.sleep(tiempo_pausa)
        # actualizo la variable para controlar el tiempo que ha pasado
        inicio=time.time()
    else:
        # si la primera variable no es inferior a la segunda 
        # se ha superado el tiempo y paramos el sonido
        GPIO.output(18, False)
#
# creamos bucle infinito que solicita los datos al usuario para ejecutar
# la funcion
while(True):
    # solicitamos al usuario que introduzca los segundos de duracion
    segundos_d=int(input("duracion del sonido (segundos): " ))
    # solicitamos al usuario el tiempo del sonido activo
    tiempo_sonido=float(input("duracion del sonido intermitente (segundos): "))
    # solicitamos al usuario el tiempo del sonido en pausa
    tiempo_silencio=float(input("duracion del silencio intermitente (segundos): "))
    # llamamos a la funcion que enciende el timbre con los valores
    encender_timbre(segundos_d,tiempo_sonido,tiempo_silencio)