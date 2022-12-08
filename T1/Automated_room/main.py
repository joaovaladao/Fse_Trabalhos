#Global variables

from sala import sala

def menu(sala):
    print("1 - Ligar/Desligar uma luz")
    print("2 - Ligar/Desligar todas as luzes")

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
        on_off = int(input())

        if on_off == 0:
            sala_atual.controll_all_lamps(0)
            print('Todas as lampadas foram desligadas')
 
        elif on_off == 1:
            sala_atual.controll_all_lamps(1)
            print('Todas as lampadas foram ligadas')

    else:
        print("Opcao invalida")

def main():
    # Call the function
    sala_1 = sala(18, 23, 24, 25, 8, 7, 1, 12, 16, 20, 21, 26)
    # sala_1.control_lampadas(2,1)

    while(1):
        menu(sala_1)



# Call the function
if __name__ == '__main__':
    main()