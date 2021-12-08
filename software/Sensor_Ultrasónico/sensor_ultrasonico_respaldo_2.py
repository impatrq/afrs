import RPi.GPIO as GPIO
import time

TRIG = 4
ECHO = 17

# Indicar que se usa el esquema de numeración de pines
# de BCM (Broadcom SOC channel), es decir los números de
# pines GPIO (General-Purpose Input/Output).
GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)

# Establecer que ECHO es un canal de entrada.
GPIO.setup(ECHO, GPIO.IN)

print ("Medición de distancias en progreso")

try:
    while True:

        # Apagar el pin activador y permitir un par de
        # segundos para que se estabilice.
        GPIO.output(TRIG, GPIO.LOW)
        print ("Esperando a que el sensor se estabilice")
        time.sleep(2)

        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        print ("Iniciando eco")
        while True:
            pulso_inicio = time.time()
            if GPIO.input(ECHO) == GPIO.HIGH:
                break
        while True:
            pulso_fin = time.time()
            if GPIO.input(ECHO) == GPIO.LOW:
                break

        # La medición del tiempo es en segundos.
        duracion = pulso_fin - pulso_inicio

        # Calcular la distancia usando la velocidad del
        # sonido y considerando que la duración incluye
        # la ida y vuelta.
        distancia = (34300 * duracion) / 2

        # Imprimir resultado.
        print ("Distancia: %.2f cm") % distancia

finally:
    # Reiniciar todos los canales de GPIO.
    GPIO.cleanup()