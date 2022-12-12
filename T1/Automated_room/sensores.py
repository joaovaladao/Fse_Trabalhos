#from main import sala_1
import RPi.GPIO as GPIO
from sala import sala

sala_1 = sala(18, 23, 24, 25, 8, 7, 1, 12, 16, 20, 21, 26)

def mod_sensor_de_presenca(GPIO_pin):

    if sala_1.get_estado_sensor_presenca() == 0:
        sala_1.set_estado_sensor_presenca(1)
        print('\nsensor de presença ativado')

    elif sala_1.get_estado_sensor_presenca() == 1:
        sala_1.set_estado_sensor_presenca(0)
        print('\nsensor de presença desativado')
    
def mod_sensor_de_fumaca(GPIO_pin):

    if sala_1.get_estado_sensor_fumaca() == 0:
        sala_1.set_estado_sensor_fumaca(1)
        print('\nsensor de fumaça ativado')

    elif sala_1.get_estado_sensor_fumaca() == 1:
        sala_1.set_estado_sensor_fumaca(0)
        print('\nsensor de fumaça desativado')

def mod_sensor_de_janela(GPIO_pin):

    if sala_1.get_estado_sensor_janela() == 0:
        sala_1.set_estado_sensor_janela(1)
        print('\nsensor de janela ativado')

    elif sala_1.get_estado_sensor_janela() == 1:
        sala_1.set_estado_sensor_janela(0)
        print('\nsensor de janela desativado')
    
def mod_sensor_de_porta(GPIO_pin):

    if sala_1.get_estado_sensor_porta() == 0:
        sala_1.set_estado_sensor_porta(1)
        print('\nsensor de porta ativado')

    elif sala_1.get_estado_sensor_porta() == 1:
        sala_1.set_estado_sensor_porta(0)
        print('\nsensor de porta desativado')