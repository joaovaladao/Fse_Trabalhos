# -*- coding: utf-8 -*-
import socket
import sys
from data_receiver import data_receiver

list_connections = [False, False, False, False]          

def menu_server(conn):
    print("------------Menu do Servidor------------")
    print("1 - Mostrar estado de uma sala específica")
    print("2 - Desligar aparelhos de uma sala específica")
    print("3 - Ligar aparelhos de uma sala específica")
    print("4 - Desligar aparelhos de todas as salas")
    print("5 - Ligar/Desligar alarme de uma sala específica")
    print("0 - Sair")
    print("--------------------------------------" + "\n")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        print("Insira o numero da sala")
        sala = int(input("Sala: "))
        if sala == 1:
            conn = list_connections[1]
        elif sala == 2:
            conn = list_connections[2]
            
        conn.sendall(str.encode("Send me your data!"))
        data_rec = b''
        data_rec += conn.recv(1024)
        data_receiver(data_rec)

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
        print("Insira o numero da sala")
        sala = int(input("Sala: "))
        if sala == 1:
            conn = list_connections[1]
            conn.sendall(str.encode("31"))
        elif sala == 2:
            conn = list_connections[2]
            conn.sendall(str.encode("32"))

    elif opcao == 4:
        for i in range(1, 3):
            if i == 1:
                conn = list_connections[i]
                conn.sendall(str.encode("21"))
            elif i == 2:
                conn = list_connections[i]
                conn.sendall(str.encode("22"))

    elif opcao == 5:
        print("Insira o numero da sala")
        sala = int(input("Sala: "))
        if sala == 1:
            conn = list_connections[1]
            conn.sendall(str.encode("41"))
        elif sala == 2:
            conn = list_connections[2]
            conn.sendall(str.encode("42"))


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
port = 10493

s.bind((host, port))
print("Waiting for incoming connections...")

s.listen(2)

try:
    for i in range(2):
        conn, addr = s.accept()
        list_connections[int(conn.recv(1024).decode('utf-8'))] = conn

        print("Connection from: " + str(addr))
        print("IP de conexão:", conn)

    while True:
        menu_server(conn)

except KeyboardInterrupt:
    print('Closing server...')
    conn.close()
    exit()