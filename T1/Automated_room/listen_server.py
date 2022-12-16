from client_test import output_json, send_to_server, create_socket
from global_variables import sala_1, sala_2

def control_mensages_to_server(sala, host):
    # Create a socket object
    s = create_socket(host)
    sala_str = str(sala.id_sala)
    
    s.sendall(str.encode(sala_str))
    global flag

    while(1):
        try:
            response = s.recv(1024)
            print(type(response))
            print(str(response))

            if str(response) == "b''":
                print("Servidor fechou a conexão, apenas as requições locais podem ser executadas...")
                flag = False
                break

            elif str(response) == "b'Send me your data!'":
                json_dict = output_json(sala)
                send_to_server(json_dict, s)

            elif str(response) == "b'21'":
                sala_1.controll_all_lamps(0)
                sala_1.control_air_conditioner(0)
                sala_1.control_projector(0)

            elif str(response) == "b'22'":
                sala_2.controll_all_lamps(0)
                sala_2.control_air_conditioner(0)
                sala_2.control_projector(0)

            elif str(response) == "b'3'":
                for i in range(2):
                    if i == 0:
                        sala = sala_1
                    elif i == 1:
                        sala = sala_2
                        print('entrou aqui')
                    sala.controll_all_lamps(0)
                    sala.control_air_conditioner(0)
                    sala.control_projector(0)

            json_dict = output_json(sala)
            send_to_server(json_dict, s)
        except:
            pass
        # time.sleep(2)   

    s.close() 