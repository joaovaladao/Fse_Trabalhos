# -*- coding: utf-8 -*-

from time import sleep
import RPi.GPIO as GPIO

class sala:

    def __init__(self, 
    lampada_1, 
    lampada_2, 
    ar_condicionado, 
    projetor, 
    alarme, 
    sensor_presenca, 
    sensor_fumaca, 
    sensor_janela,
    sensor_porta, 
    sensor_contagem_pessoas_entrada, 
    sensor_contagem_pessoas_saida, 
    sensor_temp,
    estado_lampada_1 = 0,
    estado_lampada_2 = 0,
    estado_ar_condicionado = 0,
    estado_projetor = 0,
    estado_alarme = 0,
    estado_sensor_presenca = 0,
    estado_sensor_fumaca = 0,
    estado_sensor_janela = 0,
    estado_sensor_porta = 0,
    estado_sensor_contagem_pessoas_entrada = 0,
    estado_sensor_contagem_pessoas_saida = 0,
    estado_sensor_temp = 0,
    alarme_ativado = False,
    umidade = 0,
    ):

        self.lampada_1 = lampada_1
        self.lampada_2 = lampada_2
        self.ar_condicionado = ar_condicionado
        self.projetor = projetor
        self.alarme = alarme
        self.sensor_presenca = sensor_presenca
        self.sensor_fumaca = sensor_fumaca
        self.sensor_janela = sensor_janela
        self.sensor_porta = sensor_porta
        self.sensor_contagem_pessoas_entrada = sensor_contagem_pessoas_entrada
        self.sensor_contagem_pessoas_saida = sensor_contagem_pessoas_saida
        self.sensor_temp = sensor_temp
        self.estado_lampada_1 = estado_lampada_1
        self.estado_lampada_2 = estado_lampada_2
        self.estado_ar_condicionado = estado_ar_condicionado
        self.estado_projetor = estado_projetor
        self.estado_alarme = estado_alarme
        self.estado_sensor_presenca = estado_sensor_presenca
        self.estado_sensor_fumaca = estado_sensor_fumaca
        self.estado_sensor_janela = estado_sensor_janela
        self.estado_sensor_porta = estado_sensor_porta
        self.estado_sensor_contagem_pessoas_entrada = estado_sensor_contagem_pessoas_entrada
        self.estado_sensor_contagem_pessoas_saida = estado_sensor_contagem_pessoas_saida
        self.estado_sensor_temp = estado_sensor_temp
        self.alarme_ativado = alarme_ativado


    def set_estado_lampada_1(self, estado):
        self.estado_lampada_1 = estado

    def set_estado_lampada_2(self, estado):
        self.estado_lampada_2 = estado

    def set_estado_sensor_presenca(self, estado):
        self.estado_sensor_presenca = estado

    def set_estado_sensor_fumaca(self, estado):
        self.estado_sensor_fumaca = estado

    def set_estado_sensor_janela(self, estado):
        self.estado_sensor_janela = estado

    def set_estado_sensor_porta(self, estado):
        self.estado_sensor_porta = estado

    def set_estado_seguranca_alarme(self, estado):
        self.alarme_ativado = estado

    def set_estado_sensor_temp(self, temperatura):
        self.estado_sensor_temp = temperatura

    def set_estado_umidade(self, umidade):
        self.umidade = umidade 
    

    def controll_lamps(self, lampada, ligado):
        print('lampada: ', lampada)
        if lampada == 1:
            led = self.lampada_1

        elif lampada == 2:
            led = self.lampada_2

        if ligado == 1: 
            GPIO.output(led, GPIO.HIGH)
        elif ligado == 0: 
            GPIO.output(led, GPIO.LOW)

    def controll_all_lamps(self, ligado):
        if ligado == 1:
            GPIO.output(self.lampada_1, GPIO.HIGH)
            GPIO.output(self.lampada_2, GPIO.HIGH)

            self.estado_lampada_1 = 1
            self.estado_lampada_2 = 1

        elif ligado == 0:
            GPIO.output(self.lampada_1, GPIO.LOW)
            GPIO.output(self.lampada_2, GPIO.LOW)

            self.estado_lampada_1 = 0
            self.estado_lampada_2 = 0

    def control_air_conditioner(self, ligado):
        if ligado == 1:
            GPIO.output(self.ar_condicionado, GPIO.HIGH)
            self.estado_ar_condicionado = 1

        elif ligado == 0:
            GPIO.output(self.ar_condicionado, GPIO.LOW)
            self.estado_ar_condicionado = 0
    
    def control_projector(self, ligado):
        if ligado == 1:
            GPIO.output(self.projetor, GPIO.HIGH)
            self.estado_projetor = 1

        elif ligado == 0:
            GPIO.output(self.projetor, GPIO.LOW)
            self.estado_projetor = 0

    def get_all_sensors(self, sala): 

        print('------------Sensores------------')
        print('sensor de presença: ', self.estado_sensor_presenca)       
        print('sensor de fumaça: ', self.estado_sensor_fumaca)
        print('sensor de janela: ', self.estado_sensor_janela)
        print('sensor de porta: ', self.estado_sensor_porta)
        # print('sensor de contagem de pessoas na entrada: ', self.sensor_contagem_pessoas_entrada)
        # print('sensor de contagem de pessoas na saida: ', self.sensor_contagem_pessoas_saida)
        # print('sensor de temperatura: ', self.sensor_temp)

    def fire_alarm(self):
        print('ALARME ACIONADO')
        GPIO.output(self.alarme, GPIO.HIGH)
        self.estado_alarme = 1

    def check_fire_alarm(self, turn_off):
        if turn_off == 0:
            GPIO.output(self.alarme, GPIO.LOW)
            self.estado_alarme = 0
