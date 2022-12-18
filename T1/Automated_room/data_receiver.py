import json

def data_receiver(data):
    # print(json.loads(data.decode('utf-8')))
    data_decoded = json.loads(data.decode('utf-8'))
    print("---------------------------------------------------")
    print("Sala: " , data_decoded['sala'])
    print("Lampada 1: " , data_decoded['dados'][0]['estado_lampada_1'])
    print("Lampada 2: " , data_decoded['dados'][1]['estado_lampada_2'])
    print("Ar condicionado: " , data_decoded['dados'][2]['estado_ar_condicionado'])
    print("Projetor: " , data_decoded['dados'][3]['estado_projetor'])
    print("Alarme: " , data_decoded['dados'][4]['estado_alarme'])
    print("Sensor de presenca: " , data_decoded['dados'][5]['estado_sensor_presenca'])
    print("Sensor de fumaca: " , data_decoded['dados'][6]['estado_sensor_fumaca'])
    print("Sensor de janela: " , data_decoded['dados'][7]['estado_sensor_janela'])
    print("Sensor de porta: " , data_decoded['dados'][8]['estado_sensor_porta'])
    print("Temperatura: " , data_decoded['dados'][11]['estado_sensor_temp'])
    print("Umidade: " , data_decoded['dados'][12]['umidade'])
    print("Quantidade de pessoas na sala: " , data_decoded['dados'][9]['estado_sensor_contagem_pessoas_entrada'])
    print("---------------------------------------------------" + "\n")
    
def debug_data_receiver(data):
    list_send = []
    for line in data:
        data = json.loads(str(line))
        text = data.to_bytes(length=4, byteorder='big').decode('utf-8')
        list_send.append(text.replace('\x00\x00\x00', ''))
    print(list_send)
# Função para debugar as mensagens recebidas, não é utilizada no programa final