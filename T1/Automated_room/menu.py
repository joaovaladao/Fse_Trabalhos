# -*- coding: utf-8 -*-

def menu(sala):
    print("------------Menu de opcoes------------")
    print("1 - Ligar/Desligar uma luz")
    print("2 - Ligar/Desligar todas as luzes")
    print("3 - Verificar sensores")
    print("4 - Acionar o sistema de seguranca")
    print("5 - Desligar o sistema de seguranca")
    print("6 - Desligar o alarme (sirene), caso esteja acionado")

    sala_atual = sala
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        print("Insira a lampada que deseja ligar/desligar: ")
        lampada = int(input("Lampada: "))

        if sala_atual.estado_lampada_1 == 0:
            sala_atual.controll_lamps(lampada,1)
            if lampada == 1:
                sala_atual.set_estado_lampada_1(1)
            elif lampada == 2:
                sala_atual.set_estado_lampada_2(1)

        elif sala_atual.estado_lampada_1 == 1:
            sala_atual.controll_lamps(lampada,0)
            if lampada == 1:
                sala_atual.set_estado_lampada_1(0)
            elif lampada == 2:
                sala_atual.set_estado_lampada_2(0)

    elif opcao == 2:
        print("Digite o comando desejado:\n0 - Desligar todas as lampadas\n1 - Ligar todas as lampadas\n")
        on_off = int(input("Comando:"))

        if on_off == 0:
            sala_atual.controll_all_lamps(0)
            print('Todas as lampadas foram desligadas')
 
        elif on_off == 1:
            sala_atual.controll_all_lamps(1)
            print('Todas as lampadas foram ligadas')

    elif opcao == 3:
        print("Sensores ativos: ")
        sala_atual.get_all_sensors(sala_atual)

    elif opcao == 4:
        print("Sistema de seguranca ativado")
        sala_atual.set_estado_seguranca_alarme(True)
        print(sala_atual.get_estado_seguranca_alarme())

    elif opcao == 5:
        print("Sistema de seguranca desativado")
        sala_atual.set_estado_seguranca_alarme(False)

    elif opcao == 6:
        if sala_atual.estado_alarme == 0:
            print("Alarme já está desligado")
        elif sala_atual.estado_alarme == 1:
            sala_atual.check_fire_alarm(0)
            print("Alarme desligado")

        


    else:
        print("Opcao invalida")