# -*- coding: utf-8 -*-

#Global variables
import RPi.GPIO as GPIO
from menu import menu
from global_variables import sala_1, sala_2
from sensores import mod_sensor_de_presenca, mod_sensor_de_fumaca, mod_sensor_de_janela, mod_sensor_de_porta

# sala_1 = sala(18, 23, 24, 25, 8, 7, 1, 12, 16, 20, 21, 26)
# sala_2 = sala(26, 19, 13, 6, 5, 0, 11, 9, 10, 22, 27, 18)

def initialize_settup(sala):
    # Initialize settings
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 

    # leds
    #GPIO.setup([18, 23], GPIO.OUT)
    GPIO.setup([sala.lampada_1, sala.lampada_2], GPIO.OUT)
    GPIO.setup(sala.alarme, GPIO.OUT)

    # sensor de presença
    GPIO.setup(sala.sensor_presenca, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(sala.sensor_presenca, GPIO.BOTH, callback=mod_sensor_de_presenca, bouncetime = 300)

    # sensor de fumaça
    GPIO.setup(sala.sensor_fumaca, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(sala.sensor_fumaca, GPIO.BOTH, callback=mod_sensor_de_fumaca, bouncetime = 300)

    # sensor de janelas
    GPIO.setup(sala.sensor_janela, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(sala.sensor_janela, GPIO.BOTH, callback=mod_sensor_de_janela, bouncetime = 300)

    # sensor de porta
    GPIO.setup(sala.sensor_porta, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(sala.sensor_porta, GPIO.BOTH, callback=mod_sensor_de_porta, bouncetime = 300)


def main():

    initialize_settup(sala_2)

    while(1):
        menu(sala_2)



# Call the function
if __name__ == '__main__':
    main()