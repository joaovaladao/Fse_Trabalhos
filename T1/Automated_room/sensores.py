# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

from global_variables import sala_1, sala_2


def mod_sensor_de_presenca(GPIO_pin):
    if GPIO_pin == 7:
        sala_atual = sala_1
    else:
        sala_atual = sala_2

    if sala_atual.estado_sensor_presenca == 0:
        sala_atual.set_estado_sensor_presenca(1)
        on_off = get_seguranca_alarme(sala_atual)
        print('\nsensor de presença ativado')
        if on_off == True:
            sala_atual.fire_alarm()
        else:
            if sala_atual.estado_lampada_1 == 0 and sala_atual.estado_lampada_2 == 0:
                sala_atual.controll_all_lamps(1)
            else:
                print('\nLampadas já estavam ligadas')
                
    elif sala_atual.estado_sensor_presenca == 1:
        sala_atual.set_estado_sensor_presenca(0)
        print('\nsensor de presença desativado')

    
def mod_sensor_de_fumaca(GPIO_pin):
    if GPIO_pin == 1:
        sala_atual = sala_1
    else:
        sala_atual = sala_2

    if sala_atual.estado_sensor_fumaca == 0:
        sala_atual.set_estado_sensor_fumaca(1)
        sala_atual.fire_alarm()

    elif sala_atual.estado_sensor_fumaca == 1:
        sala_atual.set_estado_sensor_fumaca(0)
        print('\nsensor de fumaça foi desativado')
        sala_atual.check_fire_alarm(0)


def mod_sensor_de_janela(GPIO_pin):
    if GPIO_pin == 12:
        sala_atual = sala_1
    else:
        sala_atual = sala_2

    if sala_atual.estado_sensor_janela == 0:
        sala_atual.set_estado_sensor_janela(1)
        print('\nsensor de janela ativado')
        on_off = get_seguranca_alarme(sala_atual)
        if on_off == True:
            sala_atual.fire_alarm()
        else:
            print('\nTão mexendo na janela mas o alarme ta desligado, então não vou fazer nada...')

    elif sala_atual.estado_sensor_janela == 1:
        sala_atual.set_estado_sensor_janela(0)
        print('\nsensor de janela desativado')

    
def mod_sensor_de_porta(GPIO_pin):
    if GPIO_pin == 16:
        sala_atual = sala_1
    else:
        sala_atual = sala_2

    if sala_atual.estado_sensor_porta == 0:
        sala_atual.set_estado_sensor_porta(1)
        print('\nsensor de porta ativado')
        on_off = get_seguranca_alarme(sala_atual)
        if on_off == True:
            sala_atual.fire_alarm()
        else:
            print('\nTão mexendo na porta mas o alarme ta desligado, então não vou fazer nada...')

    elif sala_atual.estado_sensor_porta == 1:
        sala_atual.set_estado_sensor_porta(0)
        print('\nsensor de porta desativado')

def aumenta_contagem_pessoas(GPIO_pin):
    if GPIO_pin == 20:
        sala_atual = sala_1
    else:
        sala_atual = sala_2

    sala_atual.set_estado_contagem_pessoas(sala_atual.estado_sensor_contagem_pessoas_entrada + 1)

def diminui_contagem_pessoas(GPIO_pin):
    if GPIO_pin == 21:
        sala_atual = sala_1
    else:
        sala_atual = sala_2

    sala_atual.set_estado_contagem_pessoas(sala_atual.estado_sensor_contagem_pessoas_entrada - 1)

def get_seguranca_alarme(sala_atual):   
    return sala_atual.alarme_ativado

def read_temp_humidity(sala, dhtDevice):
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        if temperature_c is not None and humidity is not None:
            sala.set_estado_sensor_temp(temperature_c)
            sala.set_estado_umidade(humidity)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        pass