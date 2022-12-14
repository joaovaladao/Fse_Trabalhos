import json
import socket

dict_mensagem_teste = {
    'Sala 1': {
        'lampada_1': 18, 'estado_lampada_1' : 0, 'lampada_2' : 23, 'estado_lampada_2' : 0, 'ar_condicionado' : 24, 'estado_ar_condicionado' : 0,
        'projetor' : 25, 'estado_projetor' : 0, 'alarme' : 8, 'estado_alarme' : 0, 'sensor_presenca' : 7, 'estado_sensor_presenca' : 0,
        'sensor_fumaca' : 1, 'estado_sensor_fumaca' : 0, 'sensor_janela' : 12, 'estado_sensor_janela' : 0, 'sensor_porta' : 16, 'estado_sensor_porta' : 0,
        'sensor_contagem_pessoas_entrada' : 20, 'estado_sensor_contagem_pessoas_entrada' : 0, 'sensor_contagem_pessoas_saida' : 21, 'estado_sensor_contagem_pessoas_saida' : 0,
        'sensor_temp' : 4, 'estado_sensor_temp' : 0, 'umidade' : 0
    }
}

def send_to_server(dict_mensagem):
    # Create a socket object
    s = socket.socket()

    # Get the local machine name
    host = socket.gethostname()

    # Reserve a port for your service
    port = 12345

    # Connect to the server
    s.connect((host, port))

    # Send a message to the server
    infos_servidor_central_enviado = json.dumps(dict_mensagem).encode('utf-8')
    s.sendall(infos_servidor_central_enviado)

    # s.sendall("Hello! This is a message from the client.")

    # Receive a reply from the server
    response = s.recv(1024)

    # Print the received message
    print(response)

    # Close the connection
    s.close()

send_to_server(dict_mensagem_teste)
