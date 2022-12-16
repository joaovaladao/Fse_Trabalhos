# -*- coding: utf-8 -*-
import json
import socket
import sys
from menu import menu
from global_variables import sala_1, sala_2

list_connections = [False, False, False, False]

def data_receiver(conn):
    data = b'' + conn.recv(1024)
    print("Received message: " , json.loads(data.decode('utf-8')))
    

def menu_server(conn):
    print("------------Menu do Servidor------------")
    print("1 - Mostrar estado de uma sala específica")
    print("2 - Desligar aparelhos de uma sala específica")
    print("3 - Desligar aparelhos de todas as salas")
    print("0 - Sair")
    print("--------------------------------------")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        print("Insira o numero da sala")
        sala = int(input("Sala: "))
        if sala == 1:
            conn = list_connections[1]
        elif sala == 2:
            conn = list_connections[2]
            
        conn.sendall(str.encode("Send me your data!"))
        data_receiver(conn)

    elif opcao == 2:
        print("Insira o numero da sala")
        sala = int(input("Sala: "))
        if sala == 1:
            conn = list_connections[1]
            conn.sendall(str.encode("21"))
        elif sala == 2:
            conn = list_connections[2]
            conn.sendall(str.encode("22"))

    elif opcao == 3:
        for i in range(1, 3):
            conn = list_connections[i]
            conn.sendall(str.encode("3"))


    elif opcao == 0:
        print('Closing server...')
        conn.sendall(str.encode("0"))
        conn.close()
        exit()        

    else:
        print("Opcao invalida")

# Create a socket object
s = socket.socket()

# Get the local machine name
host = sys.argv[-1]

# Reserve a port for your service
port = 10495

# Bind to the port
s.bind((host, port))
print("Waiting for incoming connections...")

# Listen for incoming connections
s.listen(2)

try:
    for i in range(2):
        # Accept the incoming connection
        conn, addr = s.accept()

        # print(conn.recv(1024).decode('utf-8'))
        list_connections[int(conn.recv(1024).decode('utf-8'))] = conn

        print("Connection from: " + str(addr))
        print("IP de conexão:", conn)

    while True:

        menu_server(conn)

        # dict_salas[conn.recv(1024).decode('utf-8')] = conn
        # start_new_thread(recebe_dados_client, (conn,)) # Thread que recebe os dados dos clientes

except KeyboardInterrupt:
    print('Closing server...')
    # Close the connection
    conn.close()
    exit()

# data = b'' + conn.recv(1024)

# # Print the received message
# print("Received message: " , json.loads(data.decode('utf-8')))

# # Send a reply to the client
# conn.sendall(str.encode("Thank you for sending a message!"))



