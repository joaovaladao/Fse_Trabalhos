from client_test import output_json, send_to_server, create_socket
from global_variables import sala_1, sala_2

def turn_all_off(sala):
    sala.controll_all_lamps(0)
    sala.control_air_conditioner(0)
    sala.control_projector(0)

def control_mensages_to_server(sala, host):
    # Create a socket object
    s = create_socket(host)
    sala_str = str(sala.id_sala)
    
    s.sendall(str.encode(sala_str))
    global flag

    while(1):
        try:
            response = s.recv(1024)
            # print(type(response))
            # print(str(response))

            if str(response) == "b''":
                print("Servidor fechou a conexão, apenas as requições locais podem ser executadas...")
                flag = False
                break

            elif str(response) == "b'Send me your data!'":
                json_dict = output_json(sala)
                send_to_server(json_dict, s)

            elif str(response) == "b'21'":
                turn_all_off(sala_1)

            elif str(response) == "b'22'":
                turn_all_off(sala_2)

        except:
            pass

    s.close() 