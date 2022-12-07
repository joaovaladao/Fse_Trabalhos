from time import sleep
from gpiozero import LED

class sala:

    def __init__(self, 
    lampada_1, 
    lampada_2, 
    ar_condicionado, 
    projetor, 
    alarme, 
    sensor_presenca, 
    sensor_fumaca, 
    sensor_janela_1, 
    sensor_janela_2, 
    sensor_contagem_pessoas_entrada, 
    sensor_contagem_pessoas_saida, 
    sensor_temp):

        self.lampada_1 = LED(lampada_1)
        self.lampada_2 = LED(lampada_2)
        self.ar_condicionado = ar_condicionado
        self.projetor = projetor
        self.alarme = alarme
        self.sensor_presenca = sensor_presenca
        self.sensor_fumaca = sensor_fumaca
        self.sensor_janela_1 = sensor_janela_1
        self.sensor_janela_2 = sensor_janela_2
        self.sensor_contagem_pessoas_entrada = sensor_contagem_pessoas_entrada
        self.sensor_contagem_pessoas_saida = sensor_contagem_pessoas_saida
        self.sensor_temp = sensor_temp

    def control_lampadas(self, lampada, ligado):
        if lampada == 1:
            led = self.lampada_1
        elif lampada == 2:
            led = self.lampada_2

        if ligado == 1:    
            led.on()
        elif ligado == 0:
            led.off()
