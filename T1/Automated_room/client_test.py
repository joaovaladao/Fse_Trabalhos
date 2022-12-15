import json
import socket
import sys
from global_variables import sala_1, sala_2
from sala import sala

def output_json(sala):

    d = {}
    d['sala'] = sala.id_sala
    d['dados'] = [
        {'lampada_1': sala.lampada_1, 'estado_lampada_1' : sala.estado_lampada_1},
        {'lampada_2' : sala.lampada_2, 'estado_lampada_2' : sala.estado_lampada_2},
        {'ar_condicionado' : sala.ar_condicionado , 'estado_ar_condicionado' : sala.estado_ar_condicionado},
        {'projetor' : sala.projetor, 'estado_projetor' : sala.estado_projetor},
        {'alarme' : sala.alarme , 'estado_alarme' : sala.estado_alarme},
        {'sensor_presenca' : sala.sensor_presenca, 'estado_sensor_presenca' : sala.estado_sensor_presenca},
        {'sensor_fumaca' : sala.sensor_fumaca, 'estado_sensor_fumaca' : sala.estado_sensor_fumaca},
        {'sensor_janela' : sala.sensor_janela, 'estado_sensor_janela' : sala.estado_sensor_janela},
        {'sensor_porta' : sala.sensor_porta, 'estado_sensor_porta' : sala.estado_sensor_porta},
        {'sensor_contagem_pessoas_entrada' : sala.sensor_contagem_pessoas_entrada, 'estado_sensor_contagem_pessoas_entrada' : sala.estado_sensor_contagem_pessoas_entrada},
        {'sensor_contagem_pessoas_saida' : sala.sensor_contagem_pessoas_saida, 'estado_sensor_contagem_pessoas_saida' : sala.estado_sensor_contagem_pessoas_saida},
        {'sensor_temp' : sala.sensor_temp, 'estado_sensor_temp' : sala.estado_sensor_temp},
        {'umidade' : sala.umidade}
    ]

    #print(d)
    return d


# def load_config_json():
#     # Load the preconfigured JSON data from the file
#     with open('config.json') as json_file:
#         config = json.load(json_file)

#         # Access the values from the JSON data
#         sala = config['sala']
#         lampada_1 = config['dados'][0]

#         # Print the values to the console
#         print(f"Name: {sala}")
#         print(f"Pino da lampada 1: {lampada_1}")

def send_to_server(dict_mensagem):
    # Create a socket object
    s = socket.socket()

    # Get the local machine name
    host = sys.argv[-1]

    # Reserve a port for your service
    port = 10495
    s.connect((host, port))

    # Receive a reply from the server
    response = s.recv(1024)
    print(response)

    # Send a message to the server
    infos_servidor_central_enviado = json.dumps(dict_mensagem).encode('utf-8')
    s.sendall(infos_servidor_central_enviado)

    s.close()


while True:
    json_dict = output_json(sala_1)
    send_to_server(json_dict)




