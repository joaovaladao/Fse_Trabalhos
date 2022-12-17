# -*- coding: utf-8 -*-

#Global variables
import sys
import RPi.GPIO as GPIO
import board
import adafruit_dht
import time
import threading
from menu import menu
from global_variables import sala_1, sala_2
from sensores import mod_sensor_de_presenca, mod_sensor_de_fumaca, mod_sensor_de_janela, mod_sensor_de_porta, read_temp_humidity
from listen_server import control_mensages_to_server

flag = True

def initialize_settup(sala):
    # Initialize settings
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 

    # leds
    #GPIO.setup([18, 23], GPIO.OUT)
    GPIO.setup([sala.lampada_1, sala.lampada_2, sala.ar_condicionado, sala.projetor], GPIO.OUT)
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

    if sala.lampada_1 == 18:
        return adafruit_dht.DHT22(board.D4, use_pulseio=False)

    elif sala.lampada_1 == 26:
        return adafruit_dht.DHT22(board.D18, use_pulseio=False)


def control_thread(sala, dhtDevice):
    while(1):
        read_temp_humidity(sala, dhtDevice)
        time.sleep(2)   

def main():
    global flag

    sala_exec = sys.argv[-1]
    if sala_exec == '1':
        sala_exec = sala_1
    elif sala_exec == '2':
        sala_exec = sala_2

    host = sys.argv[-2]

    dhtDevice = initialize_settup(sala_exec)

    while(1):
        if flag == False:
            break
        thread1 = threading.Thread(target=control_thread, args=(sala_exec, dhtDevice,))
        thread1.start()
        thread2 = threading.Thread(target=control_mensages_to_server, args=(sala_exec, host,))
        thread2.start()
        menu(sala_exec)

    thread1.join()
    thread2.join()
    sys.exit()



# Call the function
if __name__ == '__main__':
    main()