#from main import sala_1
import RPi.GPIO as GPIO
from sala import sala

sala_1 = sala(18, 23, 24, 25, 8, 7, 1, 12, 16, 20, 21, 26)
sala_2 = sala(26, 19, 13, 6, 5, 0, 11, 9, 10, 22, 27, 18)

def mod_sensor_de_presenca(GPIO_pin):
    if GPIO_pin == 7:
        sala_atual = sala_1
    else:
        sala_atual = sala_2

    if sala_atual.get_estado_sensor_presenca() == 0:
        sala_atual.set_estado_sensor_presenca(1)
        print('\nsensor de presença ativado')

    elif sala_atual.get_estado_sensor_presenca() == 1:
        sala_atual.set_estado_sensor_presenca(0)
        print('\nsensor de presença desativado')
    
def mod_sensor_de_fumaca(GPIO_pin):
    if GPIO_pin == 1:
        sala_atual = sala_1
    else:
        sala_atual = sala_2

    if sala_atual.get_estado_sensor_fumaca() == 0:
        sala_atual.set_estado_sensor_fumaca(1)
        # print('\nsensor de fumaça ativado')
        sala_atual.fire_alarm()

    elif sala_atual.get_estado_sensor_fumaca() == 1:
        sala_atual.set_estado_sensor_fumaca(0)
        print('\nsensor de fumaça foi desativado')

def mod_sensor_de_janela(GPIO_pin):
    if GPIO_pin == 12:
        sala_atual = sala_1
    else:
        sala_atual = sala_2

    if sala_atual.get_estado_sensor_janela() == 0:
        sala_atual.set_estado_sensor_janela(1)
        print('\nsensor de janela ativado')

    elif sala_atual.get_estado_sensor_janela() == 1:
        sala_atual.set_estado_sensor_janela(0)
        print('\nsensor de janela desativado')
    
def mod_sensor_de_porta(GPIO_pin):
    if GPIO_pin == 16:
        sala_atual = sala_1
    else:
        sala_atual = sala_2

    if sala_atual.get_estado_sensor_porta() == 0:
        sala_atual.set_estado_sensor_porta(1)
        print('\nsensor de porta ativado')

    elif sala_atual.get_estado_sensor_porta() == 1:
        sala_atual.set_estado_sensor_porta(0)
        print('\nsensor de porta desativado')