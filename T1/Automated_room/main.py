#Global variables
import RPi.GPIO as GPIO
from menu import menu
from sala import sala

sala_1 = sala(18, 23, 24, 25, 8, 7, 1, 12, 16, 20, 21, 26)

def initialize_settup(sala):
    # Initialize settings
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 

    # leds
    GPIO.setup([18, 23], GPIO.OUT)

    # sensor de presença
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(7, GPIO.BOTH, callback=mod_sensor_de_presenca, bouncetime = 300)

def mod_sensor_de_presenca(GPIO_pin):

    if sala_1.get_estado_sensor_presenca() == 0:
        sala_1.set_estado_sensor_presenca(1)
        print('\nsensor de presença ativado')

    elif sala_1.get_estado_sensor_presenca() == 1:
        sala_1.set_estado_sensor_presenca(0)
        print('\nsensor de presença desativado')
    


def main():

    initialize_settup(sala_1)

    # sala_1.control_lampadas(2,1)

    while(1):
        menu(sala_1)



# Call the function
if __name__ == '__main__':
    main()