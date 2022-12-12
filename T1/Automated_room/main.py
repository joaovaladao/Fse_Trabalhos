#Global variables
import RPi.GPIO as GPIO
from menu import menu
from sala import sala
from sensores import mod_sensor_de_presenca, mod_sensor_de_fumaca, mod_sensor_de_janela, mod_sensor_de_porta

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

    # sensor de fumaça
    GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(1, GPIO.BOTH, callback=mod_sensor_de_fumaca, bouncetime = 300)

    # sensor de janelas
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(12, GPIO.BOTH, callback=mod_sensor_de_janela, bouncetime = 300)

    # sensor de janelas
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(16, GPIO.BOTH, callback=mod_sensor_de_porta, bouncetime = 300)


def main():

    initialize_settup(sala_1)

    while(1):
        menu(sala_1)



# Call the function
if __name__ == '__main__':
    main()